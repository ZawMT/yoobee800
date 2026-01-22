There are four classes in the design:
    1: Game 
    2: Question
    3: User
    4: ScoreRecorder

Game class takes care of playing activity. start_game is a method to start playing game which populates and prepares the class' attribute selected_questions - using Question class - (10 questions in total). Game allows the player to pause the game (method is pause_game) and to quit without playing until the end (method is halt_game). Game provides a method, show_current_score, to show the current score of the player. While the gaming is going on, with each answer provided by the user, Game updates the score info by the method update_score_info which updates the info of score through the class ScoreRecorder.

Question class is a representation of a question in the game, so it has a question and an answer to the question. It shows the question (method is show_question) and shows the answer at the end of each question when the player has provided an answer (method is show_answer).

User class is a representation of a player who can start plyaing game (method is start_play) which triggers Game.start_game, can pause playing game (method is pause_play) which triggers Game.pause_game, and can resign without playing until the end (method is resign_play) which triggers Game.halt_game. User has an attribute called current_score which tells the score the player has so far gained. The user can view the detail information about his score - such as what are the questions, what are the answers given by the player, and which answer is right or wrong (method is view_score_detail) which triggers the ScoreRecorder.display_score_detail.

ScoreRecorder class takes care of tracking the score informationn in detail. All the questions, the provided answers, and the correctness of the answers given are kept. So score information can be requested to display any time using the method display_score_detail.