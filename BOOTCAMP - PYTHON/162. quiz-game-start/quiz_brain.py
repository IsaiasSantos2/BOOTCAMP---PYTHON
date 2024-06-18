class QuizBrain:
    def __init__(self, questionlist):
        self.num = 0
        self.list = questionlist  
        self.great = 0
        self.wrong = 0  
    def stillquestions(self):
        return self.num < len(self.list)

    def next_question(self):
        present_question = self.list[self.num]
        user_answer = input(f"Q.{self.num + 1}: {present_question.text} (True or False?): ")  
        self.check_answer(user_answer, present_question.answer)                            
        self.num += 1 

    def check_answer(self, user_answer, correct_answer):    
        if user_answer == correct_answer:
            self.great += 1
            return print("Great")    
        else:
            self.wrong += 1   
            return print("Wrong")
          
  