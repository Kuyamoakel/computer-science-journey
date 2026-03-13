# FlashCards
PERSONAL PROJECT.
dami kong sakit ng ulo dito, dami korin pangarap para dito eh lagyan ng gui tapos gawin apk para sa mobile app HAHAHAH. sobrang na istress ako dito pero marami naman ako natutunan dito. especially dito rin
na introduce saaken ang oop yung classes kaya inaaral ko siya tapos nilagay konarin dito yon. tapos yung refresh bangis non. naging solid din pagintindi ko dito sa functions and ibang pang mga methods and module.

10/10 project for me mahirap saaken noon pero solids!

# Python Quiz Game

A command-line quiz application built using Python.
The program allows users to create, store, and answer quiz questions with a time limit. Quiz data is stored in a JSON file so questions persist even after the program closes.

---

## Features

* Add custom quiz questions and answers
* Play the quiz with randomized questions
* Five-second time limit for each answer
* Score tracking system
* View all stored quiz questions
* Remove existing quiz questions
* Automatic saving using JSON storage
* Clear console between questions for better readability

---

## Menu System

When the program runs, the following menu appears:

```
---------- WELCOME TO QUIZ GAME ----------

[1] QUIZ GAME
[2] ADD QUIZ QUESTIONS AND ANSWER
[3] VIEW LIST OF THE QUIZZES
[4] REMOVE QUIZZES
[5] REVEAL SCORE
[6] EXIT
```

---

## How the Quiz Works

1. Select **Quiz Game** from the menu.
2. Questions are shuffled randomly.
3. Each question must be answered within five seconds.
4. If the time expires, the question is marked incorrect and the correct answer is shown.
5. Press **Q** anytime to quit the quiz.

Example:

```
Question: What is the capital of France?
Answer: Paris
```

---

## Project Structure

```
quiz-game/
│
├── quiz.py
├── quiz.json
└── README.md
```

* `quiz.py` – Main application file
* `quiz.json` – Stores quiz questions and answers
* `README.md` – Project documentation

---

## Technologies Used

* Python
* JSON
* Threading (for timed input)
* Random module
* OS module

---

## How to Run the Project

Clone the repository:

```
git clone https://github.com/yourusername/quiz-game.git
```

Navigate to the project folder:

```
cd quiz-game
```

Run the program:

```
python quiz.py
```

---

## Learning Objectives

This project demonstrates:

* Working with JSON files for persistent data storage
* Creating menu-driven command-line applications
* Using threading to implement timed input
* Managing program state using functions and global variables
* Structuring small Python projects

---

## Future Improvements

* Add multiple choice questions
* Implement difficulty levels
* Add a leaderboard system
* Create a graphical user interface

---

## Author

This project is part of a Computer Science learning journey focused on building small projects to strengthen programming fundamentals.
