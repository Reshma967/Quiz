from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in range(0,12):
    text=question_data[i]["text"]
    answer=(question_data[i]["answer"])
    new_question=Question(text,answer)
    question_bank.append(new_question)
        
que=QuizBrain(question_bank)
que.next_question()
    
while(que.still_has_que):
    que.next_question()
    
print("quiz over")
print(f"your score is {que.score/que.question_number}")
