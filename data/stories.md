## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Happy Flow

* greet
    - utter_iamabot
* game_start
    - utter_game_start
    - action_game_question
* game_answer{"answer_option":"a"}
    - utter_game_answer
    - action_game_question
* game_answer{"answer_option":"b"}
    - utter_game_answer
    - action_game_question
* game_answer{"answer_option":"a"}
    - utter_game_answer
    - utter_game_result

## Flow with Empty Response

* greet
    - utter_iamabot
* game_start
    - utter_game_start
    - action_game_question
* game_answer
    - utter_answer_fallback
* game_answer{"answer_option":"c"}
    - utter_game_answer
    - action_game_question
* game_answer{"answer_option":"b"}
    - utter_game_answer
    - action_game_question
* game_answer{"answer_option":"a"}
    - utter_game_answer
