import json
import random
import threading
import os

FILE_QUIZ = "quiz.json"

design = "****************************************"
quiz = []
score = 0
total = 0

def load_quiz():
    global quiz
    try:
        with open(FILE_QUIZ, "r") as f:
            quiz = json.load(f)
    except FileNotFoundError:
        print("FILE DOESN'T EXIST!")

def save_quiz():
    global quiz
    with open(FILE_QUIZ, "w") as f:
        json.dump(quiz, f, indent=4)    

# Non-blocking input with timeout using threading
def timeout_input(prompt, timeout):
    user_input = [None]
    def get_input():
        user_input[0] = input(prompt)
    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout)  # Wait for the thread or timeout
    if thread.is_alive():
        return None  # Timeout
    return user_input[0]  # Return user input if received before timeout

def clear_screen():
    """Function to clear the console screen"""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')

def quiz_game():
    global score, total
    print(design)
    print("~~~~~~~~~~~~~~~~~~~~~OKAY LET'S GO! HERE IS THE QUESTIONS!~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~NOTE THAT ANYTIME YOU WANT TO QUIT PRESS [Q]~~~~~~~~~~~~~~~~")
    print("~~AND ALSO IF YOU DIDN'T GET THE ANSWER IN 5 SECONDS IT WILL CONSIDER WRONG~~")

    if not quiz:
        print("THERE IS NO AVAILABLE QUESTIONS. PLEASE ADD")
        return
    
    random.shuffle(quiz)

    for card in quiz:
        clear_screen()  # Clear the screen before displaying the next question
        print(f"\nQuestion: {card['question']}")
        total += 1
        user_input = timeout_input("answer: ", 5)  # Wait for the user's input within 5 seconds

        if user_input is None:
            print(f"OPS! TIMES UP! THE ANSWER IS {card['answer']}")
        elif user_input.lower() == "q":
            print("OKAY~OKAY QUITING THE QUIZ NA!")
            break
        else:
            if user_input.lower() == card['answer'].lower():
                score += 1
                print("\n~~~OH NICE THAT'S CORRECT~~~")
            else:
                print("\n~~~BUDY THAT'S IS INCORRECT~~~")

def quiz_add():
    question = input("QUESTION: ")
    answer = input("ANSWER: ")

    quiz.append(
        {
            "question": question, "answer": answer
        }
    )
    save_quiz()
    print("IT'S ADDED THANKS!")

def quiz_view():
    global quiz
    print("\nYOUR QUIZZES!")
    if not quiz:
        print(("NO QUIZZES AVAILABLE, PLEASE ADD!"))
    else:
        for i, t in enumerate(quiz, 1):
            print(f"{i}. {t['question']} --> {t['answer']}")

def quiz_remove():
    global quiz
    user = int(input("Put here you want to remove: "))
    if 0 < user <= len(quiz):
        quiz.pop(user - 1)
        save_quiz()
        print("Q&A REMOVED!")
    else:
        print("~ INVALID INPUT BOSS! ~")

def scores():
    global score, total
    print(f"GREAT WORK! HERE IS YOUR TOTAL SCORE ({score}/{total})")

def reset():
    global score, total
    score = 0
    total = 0

load_quiz()

while True:
    print("\n---------- WELCOME TO QUIZ GAME ----------")
    print(design)
    print("[1] QUIZ GAME")
    print("[2] ADD QUIZ QUESTIONS AND ANSWER")
    print("[3] VIEW LIST OF THE QUIZZES")
    print("[4] REMOVE QUIZZES")
    print("[5] TO REVEAL SCORE")
    print("[6] EXIT")
    print

    print(design)
    choice = input("MENU: ")

    if choice == "1":
        quiz_game()
    elif choice == "2":
        quiz_add()
    elif choice == "3":
        quiz_view()
    elif choice == "4":
        quiz_remove()
    elif choice == "5":
        scores()
        print("\nDO YOU WANT TO RESET THE SCORE?\n[yes?]~~~[no?]")
        choice_reset = input("HERE: ")
        if choice_reset.lower() == "yes":
            reset()
            print("IT HAS BEEN RESET!")
        elif choice_reset.lower() == "no":
            print("No worries!")
        else:
            print("INVALID")
    elif choice == "6":
        print("\n~~OKAY SO MUCH BOSS! NEXT TIME ULIT REVIEW TAYO!~~")
        break

    else:
        print("OPS?! I THINK THAT'S IS INVALID!")
