import beginner,classmodule,data
class QuizBrain():
    def __init__(self,questions_list):
        self.question_number = 0
        self.questions_list = questions_list
    
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        print(f"Q.{self.question_number} : {current_question.text} True / False ? ")
        current_question.text