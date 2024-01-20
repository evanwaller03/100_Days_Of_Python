class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def questions_remain(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ").lower()
        self.check_answer(user_answer, self.question_list[self.question_number].answer.lower())
        self.question_number += 1
        
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
            print(f"The correct answer was: {correct_answer}")
        print(f"Current Score: {self.score}/{self.question_number+1}\n")