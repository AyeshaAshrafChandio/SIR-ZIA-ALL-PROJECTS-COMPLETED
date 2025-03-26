import time
import random

# Define a question bank with categories
question_bank = {
    "1": [  # General Knowledge
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
            "answer": "C"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["A) China", "B) Japan", "C) South Korea", "D) Thailand"],
            "answer": "B"
        }
    ],
    "2": [  # Math
        {
            "question": "What is 5 + 7?",
            "options": ["A) 10", "B) 12", "C) 15", "D) 9"],
            "answer": "B"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
            "answer": "B"
        },
        {
            "question": "What is 12 × 5?",
            "options": ["A) 50", "B) 60", "C) 70", "D) 80"],
            "answer": "B"
        },
        {
            "question": "What is 100 ÷ 4?",
            "options": ["A) 20", "B) 25", "C) 30", "D) 35"],
            "answer": "B"
        },
        {
            "question": "What is 3² + 4²?",
            "options": ["A) 5", "B) 9", "C) 16", "D) 25"],
            "answer": "D"
        }
    ],
    "3": [  # Science
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
            "answer": "A"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
            "answer": "B"
        },
        {
            "question": "What is the smallest unit of life?",
            "options": ["A) Atom", "B) Molecule", "C) Cell", "D) Tissue"],
            "answer": "C"
        },
        {
            "question": "What is the boiling point of water in Celsius?",
            "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"],
            "answer": "B"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A) Venus", "B) Earth", "C) Mercury", "D) Mars"],
            "answer": "C"
        }
    ]
}

def ask_question(question_data, time_limit):
    """Ask a single question and return whether the answer is correct."""
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    start_time = time.time()
    user_answer = input("Your answer (A/B/C/D): ").upper()
    end_time = time.time()

    # Check if the user answered within the time limit
    if end_time - start_time > time_limit:
        print("⏰ Time's up! You took too long to answer.")
        return False

    # Check if the answer is correct
    if user_answer == question_data["answer"]:
        print("✅ Correct! 🎉")
        return True
    else:
        print(f"❌ Incorrect! The correct answer is {question_data['answer']}.")
        return False

def quiz_game():
    print("🧠 Welcome to the Quiz Game! 🧠")
    print("Categories:")
    print("1) General Knowledge")
    print("2) Math")
    print("3) Science")
    category = input("Choose a category (1/2/3): ").strip()

    # Check if the category exists
    if category not in question_bank:
        print("❌ Invalid category! Please choose from the available categories.")
        return

    # Get the list of questions for the selected category
    questions = question_bank[category]

    # Check if there are enough questions
    if len(questions) < 5:
        print(f"⚠️ Not enough questions in this category. Only {len(questions)} questions available.")
        return

    # Select 5 random questions from the chosen category
    selected_questions = random.sample(questions, 5)
    score = 0

    # Ask each question
    for i, question_data in enumerate(selected_questions, start=1):
        print(f"\nQuestion {i}:")
        if ask_question(question_data, time_limit=10):  # 10-second time limit
            score += 1

    # Display final score
    print(f"\nFinal Score: {score}/{len(selected_questions)} 🎯")

# Run the quiz game
quiz_game()