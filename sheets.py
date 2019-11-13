import gspread
from oauth2client.service_account import ServiceAccountCredentials

###### Configuration Sheets
# set scope for access
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# set up credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("./credentials/credentials-spreadsheets.json", scope)
client = gspread.authorize(creds)
# get sheets data
sheet = client.open("Learning NLU").sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records

###### Operations
# TODOs
def getValue():
    try:
        cell = sheet.cell(1,2).value  # Get the value of a specific cell
        return cell
    except:
        return "Error"

def getAnswers(row):
    try: 
        cellA = sheet.cell(row,3).value
        cellB = sheet.cell(row,4).value
        cellC = sheet.cell(row,5).value
        anwsers = {"a": cellA, "b": cellB, "c": cellC}
        return anwsers
    except:
        return "Error"