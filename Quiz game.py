

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"}
]

def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question["question"])
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")
    print(f"Your final score is {score}/{len(questions)}")
    print(f"Thank you for playing!, {user_name}")

user_name = input("Welcome to the Quiz game! What is your name? ")
print(f"Hello {user_name}, let's start the quiz!")
run_quiz(questions)

while True:
    final_ques = input(f"{user_name}, do you want to play again ? (yes/no)")

    if final_ques.lower() == "yes":
       run_quiz(questions)
    elif final_ques.lower() not in ["yes", "no"]:
        print(f"not a vaild answer.Thank you for playing! {user_name}")
        break   
    elif final_ques.lower() == "no":
        print(f"Thank you for playing! , {user_name}")
        break

   