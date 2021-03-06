import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
import json

###### Configuration Sheets
# set scope for access
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# set up credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("./credentials/credentials-spreadsheets.json", scope)
client = gspread.authorize(creds)
# get sheets data
sheet = client.open("Learning NLU").sheet1  # Open the spreadhseet
#data = sheet.get_all_records()  # Get a list of all records

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

def getInfoGraphic(row):
	try: 
		infoGraphic = sheet.cell(row,6).value
		return infoGraphic
	except: 
		return "Error getInfoGraphic()"

def getInfoURL(row):
	try: 
		infoURL = sheet.cell(row,7).value
		return infoURL
	except: 
		return "Error getInfoURL()"

def getFunFact(row):
	try:
		funFact = sheet.cell(row,8).value
		return funFact
	except:
		return "Error getFunFact()"


def getQuestionRound(row):
	try: 
		#TODO: What if the row is empty? Handle it! ==> field should be null
		question = getQuestion(row)
		answers = getAnswers(row) 
		url = getInfoURL(row)
		image = getInfoGraphic(row)
		fact = getFunFact(row)

		singleRound = {
			"question": question,
			"answers" : answers,
			"url" : url,
			"image": image,
			"funFact" : fact
		}

		return singleRound
	except: 
		return "Error getQuestionRound()"

####### Example output
#   
#    {'answers': {'a': ['A2', True], 'b': ['C2', False], 'c': [' B2', False]},
#    'image': 'https://www.youtube.com/watch?v=ET1k9OrsfYQ&t=11s',
#    'question': 'What is a Whitespace Tokenizer?',
#    'url': 'http://groonga.org/docs/images/used-when-indexing.png'
#    }


# TODO: Get topics of questions and where they can be found 
	#   input = null
	#   output = strutured 
	#   output: [
	# {
	#        "Rasa Pipeline": [2,6]       
	#       }, ...
	# ]
	# Topic + content is from row x to row y 

# find all topic names
def getTopics():
	try:
		allTopicValues = sheet.col_values(1)
		# get unique topics
		topics = set(allTopicValues)
		# remove headline
		topics.remove("Topic") 
		return topics
	except: 
		return "Error getTopics()"

# find the rows for a specific topic
	# 1. find all cells with topic name as content
	# 2. filter out 
		## logic => [return rowNumber for all_rows in findAllRows if colum == 1]
		## see also https://stackoverflow.com/questions/30919430/how-to-filter-python-list-with-multiple-criteria
		# _row & _col are part of gspread library
def getTopicRows(topicName):
	try:
		findAllRows = sheet.findall(topicName)
		filteredTopics = [i._row for i in findAllRows if str(i._col) in ["1"]]
		return filteredTopics
	except:
		return "Error getTopicRows()"

def getAllRows():
	try:
		values_list = sheet.col_values(1)
		totalRows = len(values_list)
		return totalRows
	# TODO: should be like topicRows but return all rows which are filled with content
	except:
		return "Error getAllRows()"


# TODO: Get a random row
def getRandomRow():
	try:
		rangeFrom = 1 # do not include headings
		rangeTill = getAllRows()
		randomRow = random.randrange(rangeFrom, rangeTill)
		return randomRow
	except: 
		return "Error getRandomRow()"

# TODO: Get a random row for a specific topic
	# input = get which rows are relevant ["from row x", "till row y"]
	# output = row


# TODO - last step
	# write two function which combine these upper function
	# case 1: random question => output a structure with question, answers etc.
	# case 2: specific topic question => outuput a structure with question, answers etc. for this topic
