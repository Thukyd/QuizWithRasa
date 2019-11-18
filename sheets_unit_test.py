from pprint import pprint
import sheets

data = sheets.getQuestionRound(3)

pprint(data)

#pprint(data.answers)

pprint("************** Image *******************")

pprint(data["image"])

pprint("************** Answers *******************")

pprint(data["answers"])

pprint("************** Answers A *******************")

pprint(data["answers"]["a"][0])

pprint("************** Answers true or false? *******************")
pprint(data["answers"]["a"][1])
