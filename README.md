## Script to transfer data from CSV file to Google Sheets

I wrote this script to automate part of my work which requires transfering information from a csv file to a google spreadsheet with some modifications.

### Source - CSV file

|              Column 0             |
|-----------------------------------|
| url_input,text_to_show,text_input |
| url_input,text_to_show,text_input |
| url_input,text_to_show,text_input |

### Output:

|               Column 0               |   Column 1  |
|--------------------------------------|:-----------:|
| =HYPERLINK( url_input, text_to_show) |  text_input |
| =HYPERLINK( url_input, text_to_show) |  text_input |
| =HYPERLINK( url_input, text_to_show) |  text_input |

**Please take note that you need to edit the script to customize your output**

**This is just an example of how you can use Google Sheets API**
