import os
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

__CWD = os.path.dirname(os.path.abspath(__file__))
HYPERLINK_URL = '=HYPERLINK("https://put_here_your_url","text_to_show")'
client_secret = os.path.join(__CWD, 'credentials_file.json')
source_csv = os.path.join(__CWD, 'source.csv')

scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(client_secret, scope)
client = gspread.authorize(credentials)

sheet = client.open_by_key('your_spreadsheet_key').sheet1

with open(source_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for line in csv_reader:
        if line_count == 0:
            # Column names - do nothing
            line_count += 1
        else:
            # This is where you can edit what you want to put in your spreadsheet
            sheet.update_cell(row=line_count, col=1, value=HYPERLINK_URL)
            sheet.update_cell(row=line_count, col=2, value=line[0])
            line_count += 1
    print(f'Processed {line_count} lines')
