# Simple Quiz Game

def show_welcome():
    print("===== QUIZ GAME =====")
    print("Answer the questions and test your knowledge!\n")

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    try:
        choice = int(input("Enter your answer (1-4): "))
        if options[choice - 1] == correct_answer:
            print("Correct! ✅\n")
            return 1
        else:
            print(f"Wrong! ❌ Correct answer is: {correct_answer}\n")
            return 0
    except:
        print("Invalid input! ❌\n")
        return 0

def run_quiz():
    score = 0

    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
            "answer": "Delhi"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["Python", "C", "HTML", "Java"],
            "answer": "HTML"
        },
        {
            "question": "Who is known as the father of computers?",
            "options": ["Einstein", "Newton", "Charles Babbage", "Tesla"],
            "answer": "Charles Babbage"
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Process Unit",
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Power Unit"
            ],
            "answer": "Central Processing Unit"
        },
        {
            "question": "Which data type is used for text in Python?",
            "options": ["int", "float", "str", "bool"],
            "answer": "str"
        }
    ]

    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])

    return score

def show_result(score, total):
    print("===== RESULT =====")
    print(f"Your Score: {score}/{total}")

    percentage = (score / total) * 100

    if percentage == 100:
        print("Excellent! 🔥")
    elif percentage >= 60:
        print("Good Job! 👍")
    else:
        print("Keep Practicing! 💪")

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ")
    return choice.lower() == "yes"

def main():
    show_welcome()

    while True:
        score = run_quiz()
        show_result(score, 5)

        if not play_again():
            print("Thanks for playing! 🎮")
            break

# Extra feature: add custom question
def add_question(questions):
    q = input("Enter your question: ")
    options = []
    for i in range(4):
        options.append(input(f"Enter option {i+1}: "))
    ans = input("Enter correct answer: ")
    questions.append({"question": q, "options": options, "answer": ans})

# Run program
if __name__ == "__main__":
    main()
# Note: The above code is a simple quiz game. You can add more questions or features as needed.
#   For example, you can allow users to add their own questions or keep track of high scores.
#   This code is meant for educational purposes and can be expanded with more complex features like categories, timers, or multiplayer mode.