import time
#list of questions and answers
questions = [
    {
        "question": "What is the capital of India",
        "answer": "New Delhi"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter"
    },
    {
        "question": "Who is the Prime Minister of the India",
        "answer": "Narendra Modi"
    },
    {
        "question": "What is our national tree",
        "answer": "Banyan"
    },
    {
        "question": "Who is father of Maths",
        "answer": "Archimedes"
    }
]
# Function to display a question and check the answer
def ask_question(question, answer):
    print(question)
    user_answer = input("Your answer: ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

# Function to run the quiz game
def run_quiz():
    score = 0
    total_questions = 100

    
    for question in questions:
        print("\n---")
        if ask_question(question["question"], question["answer"]):
            score += 10
        time.sleep(1)

    print("---\n")
    print("Quiz completed!")
    print("Your score: {}/{}".format(score, total_questions))

    
run_quiz()