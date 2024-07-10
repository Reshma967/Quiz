class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.score=0
        self.q_list=question_list

    def still_has_que(self):
        return (self.question_number<len(self.q_list))

    def next_question(self):
        currentq = self.q_list[self.question_number]
        self.question_number += 1
        choice=input(f"Q{self.question_number}: {currentq.text}. (True/False)")
        self.check_answer(choice,currentq.answer)

    def check_answer(self,user_answer,correct_answer):
        if(user_answer == correct_answer ):
            self.score+=1
            print("you are right")
        else:
            print("you are wrong")
        print(f"the correct answer is {correct_answer}")
        print(f"your score is:{self.score}/{self.question_number}")

