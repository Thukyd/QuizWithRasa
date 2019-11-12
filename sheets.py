import gspread
from oauth2client.service_account import ServiceAccountCredentials

###### Configuration Sheets
# set scope for access
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# set up credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("sheet_credentials.json", scope)
client = gspread.authorize(creds)
# get sheets data
sheet = client.open("Learning NLU").sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records

###### Operations
# TODOs
def getValue(self):
    try:
        cell = sheet.cell(1,2).value  # Get the value of a specific cell
        return cell
    except:
        return "Error"