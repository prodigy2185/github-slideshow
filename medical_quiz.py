# A simple text-based medical quiz for a 3-year-old

def run_quiz():
    # Store Questions and Answers
    questions = [
        {
            "question": "What color is a boo-boo (an owie/a cut)?",
            "answer": "red"
        },
        {
            "question": "What do you wear on your head to stay safe on a bike?",
            "answer": "helmet"
        },
        {
            "question": "Where does food go after you chew it?",
            "answer": "tummy",
            "alternatives": ["belly"]
        },
        {
            "question": "What does a doctor use to listen to your heart?",
            "answer": "stethoscope"
        },
        {
            "question": "If you feel hot, what might mommy or daddy use to check your temperature?",
            "answer": "thermometer"
        }
    ]

    # Welcome Message
    print("Hello! Let's play a fun quiz!")
    print("---")

    # Loop Through Questions
    for q_data in questions:
        question = q_data["question"]
        correct_answer = q_data["answer"]
        alternative_answers = q_data.get("alternatives", [])

        # Display the question
        print(question)
        
        # Prompt the user for an answer
        user_answer = input("Your answer: ")

        # Retrieve the user's answer and convert to lowercase
        user_answer_lower = user_answer.lower()
        correct_answer_lower = correct_answer.lower()
        alternative_answers_lower = [alt.lower() for alt in alternative_answers]

        # Feedback
        if user_answer_lower == correct_answer_lower or user_answer_lower in alternative_answers_lower:
            print("That's right! Great job!")
        else:
            print(f"That was a good try! The answer is {correct_answer}.")
        print("---")

    # Ending Message
    print("You finished the quiz! You did so well!")

if __name__ == "__main__":
    run_quiz()
