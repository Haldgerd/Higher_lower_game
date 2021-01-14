import os
from random import choice, sample

from game_data import data
from title_logo import title, vs


# DEFINE FUNCTIONS
def clear():
    os.system("clear")


def print_title_and_initial_options():
    print(title + "\n")
    print(f"A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")


def select_first_cases():
    cases = sample(data, 2)
    return cases


def select_new_case():
    new_option = choice(data)
    return new_option


def determine_followers(data1, data2):
    max_followers = max([data1["follower_count"], data2["follower_count"]])
    return max_followers  # how to determine option from this number


# VARIABLE DECLARATIONS
game = True

# MAIN LOGIC
while game:
    correct_answer = " "
    option_a, option_b = select_first_cases()

    while correct_answer:  # could change this block into recursive function
        answer_count = 0
        print_title_and_initial_options()

        answer = input("Who has more followers A or B: ").lower()
        result = determine_followers(option_a, option_b)
        if (option_a["follower_count"] == result) and (answer == "a"):  # if answer is correct continue playing setting
            # option A to correct answer, else you lose
            answer_count += 1
            option_b = select_new_case()  # select new case to compare
        elif (option_b["follower_count"] == result) and (answer == "b"):
            answer_count += 1
            option_a = option_b
            option_b = select_new_case()  # select new case to compare

    print(f"You guessed correctly: {answer_count} times.")
    play_again = input("\nWould you like to play again? Type 'y' to play again, type 'n' to quit. ")
    if play_again != 'y':
        game = False
    clear()

print("Thank you for playing 'HigherLower' game!")
