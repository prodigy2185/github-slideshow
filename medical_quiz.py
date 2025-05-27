# This code defines a simple text-based medical quiz game for a 3-year old.
# It asks questions about health and hygiene, provides feedback, and keeps track of the score.
# The game encourages healthy habits and is designed to be engaging for young children.
# The game can be played multiple times, allowing children to learn and reinforce their knowledge about health.
# The quiz includes questions about tummy aches, hand washing, drinking water, eating fruits and vegetables, sleep, outdoor play, tooth brushing, and basic health knowledge.
# The game is interactive and uses simple language suitable for a 3-year old.
# The quiz also includes fun questions about the colors of kaka, pee, and blood, making it educational and entertaining.

def run_quiz():
    # Store the questions and answers
    print("Welcome to the Medical Quiz!")
    print("Answer the questions with 'yes' or 'no' (or the correct word).") # Modified instructions slightly
    score = 0
    # Question 1
    answer = input("Do you have a tummy ache? ").strip().lower()
    if answer == 'yes':
        print("Oh no! Let's be careful with our food.")
        # score += 1 # User feedback implies 'yes' to tummy ache is not a 'correct' answer for points
    else: # Assuming 'no' means the tummy is happy and is the desired state
        print("Great! Your tummy is happy.")
        score +=1 # Award point if tummy is NOT aching

    # Question 2
    answer = input("Did you wash your hands before eating? ").strip().lower()
    if answer == 'yes':
        print("Good job! Clean hands keep us healthy.")
        score += 1
    else:
        print("Remember, washing hands is very important!")

    # Question 3
    answer = input("Did you drink enough water today? ").strip().lower()
    if answer == 'yes':
        print("Awesome! Water is good for you.")
        score += 1
    else:
        print("Make sure to drink water every day!")

    # Question 4
    answer = input("Did you eat fruits and vegetables today? ").strip().lower()
    if answer == 'yes':
        print("Yay! Fruits and veggies are super healthy.")
        score += 1
    else:
        print("Try to eat some fruits and veggies every day!")

    # Question 5
    answer = input("Did you get enough sleep last night? ").strip().lower()
    if answer == 'yes':
        print("Great! Sleep helps you grow strong.")
        score += 1
    else:
        print("Sleep is very important for your health!")

    # Question 6
    answer = input("Did you play outside today? ").strip().lower()
    if answer == 'yes':
        print("Yay! Playing outside is fun and healthy.")
        score += 1
    else:
        print("Try to play outside every day for fresh air!")

    # Question 7
    answer = input("Did you brush your teeth today? ").strip().lower()
    if answer == 'yes':
        print("Good job! Brushing teeth keeps them strong.")
        score += 1
    else:
        print("Remember to brush your teeth twice a day!")

    # Question 8
    answer = input("What color is kaka? ").strip().lower() # Added space
    if answer == 'brown':
        print("That's right! Kaka is brown.")
        score += 1
    else:
        print("Hmm, kaka is usually brown. Let's remember that!")

    # Question 9
    answer = input("What color is pee? ").strip().lower() # Added space
    if answer == 'yellow':
        print("Correct! Pee is yellow.")
        score += 1
    else:
        print("Pee is usually yellow. Let's remember that!")

    # Question 10
    answer = input("What color is blood? ").strip().lower() # Added space
    if answer == 'red':
        print("That's right! Blood is red.")
        score += 1
    else:
        print("Blood is usually red. Let's remember that!")

    # Question 11
    answer = input("Where does food go after you eat it? ").strip().lower() # Added space
    if answer == 'stomach':
        print("Correct! Food goes to your stomach.")
        score += 1
    else:
        print("Food goes to your stomach. Let's remember that!")

    # Question 12
    answer = input("What do you wear on your head before riding a bike to be safe? ").strip().lower() # Added space  
    if answer == 'helmet':
        print("Great! A helmet keeps your head safe.")
        score += 1
    else:
        print("You should wear a helmet to keep your head safe when riding a bike!")

    # Final score
    print(f"Your score is {score}/12. Thanks for playing!")
    if score == 12: # Changed to == 12 for "superstar"
        print("Wow! You're a health superstar!")
    elif score >= 8: # score is 8, 9, 10, 11
        print("Great job!")
    elif score >= 6: # score is 6, 7
        print("Good effort! Keep learning about health!")
    else: # score is 0-5
        print("That's okay! Let's try again and learn more about being healthy!")

    # Loop through the quiz again
    play_again = input("Do you want to play again? (yes/no) ").strip().lower()
    if play_again == 'yes':
        run_quiz()
    else:
        print("Thanks for playing! Bye!")
        print("Remember, being healthy is fun and important!") # Moved this to be part of the final exit

if __name__ == "__main__":
    run_quiz()
