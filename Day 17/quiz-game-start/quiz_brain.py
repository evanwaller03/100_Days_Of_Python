class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list

    def questions_remain(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ").lower()
        self.question_number += 1
        return user_answer
    
    def check_answer(self, user_answer):
        if user_answer == self.question_list[self.question_number].answer.lower():
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False