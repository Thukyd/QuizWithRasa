# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
######## Watch also
# https://www.youtube.com/watch?v=W7jdIeyIPcU&t=544s

# This is a simple example for a custom action which utters "Hello World!"

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

class ActionTestBackend(Action):
     def name(self) -> Text:
          return "action_test_backend"
     
     ### get a sheets cell
     
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List [Dict[Text, Any]]:
          
          ## get a value of my sheet
          dispatcher.utter_message(sheets.getValue())
          
          return []
