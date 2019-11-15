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

# mark true/false & shuffle
def shuffleAnswers(colX, colY, colZ):
    shuffleArray = [[colX, True], [colY, False] , [colZ, False]]
    random.shuffle(shuffleArray)
    data = {
        "a" : shuffleArray[0],
        "b" : shuffleArray[1],
        "c" : shuffleArray[2],
    }
    return data

# get quiz answer & shuffle answers
def getAnswers(row):
    try: 
        colX = sheet.cell(row,3).value
        colY = sheet.cell(row,4).value
        colZ = sheet.cell(row,5).value
        answers = shuffleAnswers(colX, colY, colZ)
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

def getInfoGraphic(row):
    try: 
        infoGraphic = sheet.cell(row,7).value
        return infoGraphic
    except: 
        return "Error getInfoGraphic()"

def getQuestionRound(row):
	try: 
		#TODO: What if the row is empty? Handle it! ==> field should be null
		question = getQuestion(row)
		answers = getAnswers(row) 
		url = getInfoURL(row)		
		image = getInfoGraphic(row)
		
		singleRound = {
			"question": question,
			"answers" : answers,
			"url" : url,
			"image": image
		}	
		return data 
		


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
