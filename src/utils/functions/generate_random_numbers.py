from numpy import random


def get_random_numbers(amount_of_data):
    result_random_list = random.randint(1, 100, (amount_of_data))
    return result_random_list
