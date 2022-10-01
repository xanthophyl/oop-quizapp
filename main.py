
from data import question_data
import random
from replit import clear

end_of_game = False
while not end_of_game:
    class Quiz():
        @classmethod
        def score_scorer():
            score = 0
            score += 1
             
        def __init__(self,text,answers) :
            self.text = text
            self.answers = answers
            self.score = 0
            print("datalar çekildi.")
            

        def getQuestions():
            
            question = random.choice(question_data)
            print(question["text"])
            answer = question["answer"]
            print(answer)
            guess = input("t / f :").capitalize()
            if guess in answer:
                print("u win")
                score_scorer()
                print(f"your score: '{score}'")
            else:
                print("u lose")
                end_of_game =True
        
    Quiz.getQuestions()
