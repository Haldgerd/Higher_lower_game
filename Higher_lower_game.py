from title_logo import title, vs
from time import sleep
from game_functions import clear, select_first_cases, select_new_case, title_and_initial_options_displayed
# import module, file consisting functions used in this program.


# VARIABLE DECLARATIONS
game = True

# MAIN LOGIC
while game:
    guess_count = 0
    correct_answer = True
    option_a, option_b = select_first_cases()  # returning two different data.

    while correct_answer:  # could change this block into recursive function
        title_and_initial_options_displayed(option_a, option_b)  # displaying title and printing information
        # about particular data
        answer = input("Who has more followers A or B: ").lower()
        while answer not in ["a", "b"]:
            answer = input("Invalid input. Please type 'A' or 'B': ").lower()

        if (option_a["follower_count"] < option_b["follower_count"]) and (answer == "b"):
            option_a = option_b
            option_b = select_new_case()
        elif (option_b["follower_count"] < option_a["follower_count"]) and (answer == "a"):
            option_b = select_new_case()
        else:
            break

        while option_b == option_a:  # checking if option b is equal to option a. Setting new option b until
            # it is no longer equal to option a.
            option_b = select_new_case()

        # this two lines of code always execute when guess is correct.
        guess_count += 1  # adding additional score if guess is correct
        print(f"You're right! Your current score is {guess_count}.")  # displaying current score
        clear()

    clear()
    print(f"Sorry, you're wrong. YOUR FINAL SCORE: {guess_count}.")
    play_again = input("\nWould you like to play again? Type 'y' to play again, type 'n' to quit. ").lower()
    if play_again != 'y':
        game = False

print("\nThank you for playing 'HigherLower' game!")
