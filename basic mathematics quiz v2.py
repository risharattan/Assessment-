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

# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = ("Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to be between low and high
    else:
        error = ("Please enter an integer that"
                 f"is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # checks for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
            print(error)

# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

# Programs starts here (with a heading)
print(" ➕➖✖️➗ Welcome to Basic Mathematics Quiz!! ➕➖✖️➗ ")
print()

# Displays instructions if user wants to see them.
want_instructions = yes_no("Do you want to read the instructions?")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Question generator
point = 0
num_questions = 20

for question_number in range(1, num_questions + 1):
    print(f"\nQuestion {question_number}:")
    num1, num2, operation = generate_questions()
    user_answer = ask_questions(num1, num2, operation)
    # Show quiz results
    if check_answer(num1, num2, operation, user_answer):
        print("Correct!")
        point += 1
    else:
        print("Incorrect! The correct answer was", end=" ")
        if operation == '/':
            print(f"{num1} / {num2} = {round(num1 / num2, 2)}")
        else:
            print(eval(f"{num1} {operation} {num2}"))

    # Game loop ends here

# Displays game history if user wants to see it
show_history = yes_no("Do you want to see the game history?")
if show_history == "yes":
    print("\n⏳⏳⏳ Game History⏳⏳⏳")

    for item in game_history:
        print(item)

    print()

# calculate the lowest, highest and average
# scores and display them.

user_stats = point

print("⚙️⚙️⚙️ Game Statistics ⚙️⚙️⚙️ ")
print(f"User     - Lowest Score: {user_stats}\t "
      f"Highest Score: {user_stats}\t "
      f"Average scores: {user_stats:.2f}")

print()
print("\nQuiz over!")
print("😀😀Thank you for playing.😀😀")


