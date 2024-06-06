import random


def generate_questions():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])
    return num1, num2, operation


def ask_questions(num1, num2, operation):
    if operation == '+':
        question = f"What is {num1} + {num2}? "
    elif operation == '-':
        question = f"What is {num1} - {num2}? "
    elif operation == '*':
        question = f"What is {num1} * {num2}? "
    else:
        question = f"What is {num1} / {num2}? (Round your answer to two decimal places) "
    answer = input(question)
    return answer


def check_answer(num1, num2, operation, user_answer):
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    else:
        correct_answer = round(num1 / num2, 2)
    return float(user_answer) == correct_answer

# checks user enter yes (y) or no (n)


def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if user don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you did not choose a valid response")


def instructions():
    print('''

**** Instructions ****

This is a quiz which performs basic mathematical operations 
such as addition, subtraction, multiplication, and division.

There will be 20 given questions.

Your goal is to answer as much questions.  

Good Luck!! 

    ''')


# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_answered = 0
end_quiz = "no"
feedback = ""

quiz_history = []
all_point = []

# Programs starts here (with a heading)
print(" ➕➖✖️➗ Welcome to Basic Mathematics Quiz!! ➕➖✖️➗ ")
print()

# Displays instructions if user wants to see them.
want_instructions = yes_no("Do you want to read the instructions?")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Question generator
user_point = 0
num_questions = 20

for question_number in range(1, num_questions + 1):
    print(f"\nQuestion {question_number}:")
    num1, num2, operation = generate_questions()
    user_answer = ask_questions(num1, num2, operation)
    # Show quiz results
    if check_answer(num1, num2, operation, user_answer):
        print("👍 You got it correct! 👍")
        user_point += 1
    else:
        print("You got it wrong! The correct answer was", end=" ")
        if operation == '/':
            print(f"{num1} / {num2} = {round(num1 / num2, 2)}")
        else:
            print(eval(f"{num1} {operation} {num2}"))

    # Game loop ends here


# Displays quiz history for user

print()
print("\nQuiz over!")
print(f"You got {user_point}/{num_questions} correct.")
print("😀😀Thank you for answering.😀😀")
