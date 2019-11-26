## Happy - Open Mode
* greet
    - utter_greet
* game_start
    - utter_game_mode
* game_mode{"e_game_mode": "open"}
    - utter_game_round   <!-- predicted: action_listen -->
    - action_game_question
* game_answer{"e_answer_option": "a"}
    - utter_game_answer
    - utter_game_result


## Happy - Topic Mode
* greet
    - utter_greet
* game_start
    - utter_game_mode
* game_mode{"e_game_mode": "topic"}
    - utter_game_topic   <!-- predicted: action_listen -->
* game_topic{"e_game_topic": "NLU"}
    - utter_game_topic_chosen
    - utter_game_round
    - action_game_question
* game_answer{"e_answer_option": "a"}
    - utter_game_answer
    - utter_game_result


