# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
######## Watch also
# https://www.youtube.com/watch?v=W7jdIeyIPcU&t=544s

# This is a simple example for a custom action which utters "Hello World!"


######################
### How to run the bot in a test: https://www.youtube.com/watch?v=W7jdIeyIPcU
### "rasa run actions & rasa shell"



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# import google sheets module
import sheets

class ActionHelloWorld(Action):
     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker, 
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Hello World!")

         return []

class ActionGameQuestion(Action):
     def name(self) -> Text:
          return "action_game_question"
     
     ### get a sheets cell
     
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List [Dict[Text, Any]]:
          
          ## get a value of my sheet
          #TODO: Adapt to new structure of sheets
          data = sheets.getQuestionRound(4)

          a = data["answers"]["a"][0]
          b = data["answers"]["b"][0]
          c = data["answers"]["c"][0]

          response = "Ok, what is the meaning of life?\n Is it a) " + a + ", b)" + b + " or c) " + c + "?"
          
     
          dispatcher.utter_message(response)
          return []
