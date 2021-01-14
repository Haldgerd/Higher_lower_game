import os
from random import choice, sample

from game_data import data
from title_logo import title, vs


# DEFINE FUNCTIONS
def clear():
    os.system("clear")


def select_first_cases():
    cases = sample(data, 2)
    return cases


def select_new_case():
    new_option = choice(data)
    return new_option


def title_and_initial_options_displayed(data1, data2):
    print(title + "\n")
    print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}.")
    print(vs)
    print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}.")


