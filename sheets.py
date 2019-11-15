import gspread
import random
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

# shuffle answers
def shufflAnswers(colX, colY, colZ):
    # Todo add, true / false, then shuffle
    # output: Json structure {a }
    #shuffleArray = [a, b ,c]
    #random.shuffle(shuffleArray)
    return 
    # return list of answers 

# get quiz answer & shuffle answers
def getAnswers(row):
    try: 
        colX = sheet.cell(row,3).value
        colY = sheet.cell(row,4).value
        colZ = sheet.cell(row,5).value
        answers = shufflAnswers(colX, colY, colZ)
        return answers
    except:
        return "Error getAnswers()"

# get question
def getQuestion(row):
    try: 
        question = sheet.cell(row,2).value
        return question
    except: 
        return "Error getQuestion()"

def getInfoURL(row):
    try: 
        infoURL = sheet.cell(row,6).value
        return infoURL
    except: 
        return "Error getInfoURL()"

def getInfoGraphc(row):
    try: 
        infoGraphic = sheet.cell(row,7).value
        return infoGraphic
    except: 
        return "Error getInfoGraphc()"

# TODO: Get topics of questions and where they can be found 
    #   input = null
    #   output = strutured 
    #   output: [
    # {
    #        "Rasa Pipeline": [2,6]       
    #       }, ...
    # ]
    # Topic + content is from row x to row y 

# TODO: Get a random row
    # input = null
    # outpur = row

# TODO: Get a random row for a specific topic
    # input = get which rows are relevant ["from row x", "till row y"]
    # output = row


# TODO - last step
    # write two function which combine these upper function
    # case 1: random question => output a structure with question, answers etc.
    # case 2: specific topic question => outuput a structure with question, answers etc. for this topic