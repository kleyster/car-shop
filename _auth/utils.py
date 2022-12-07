import random


def generate_random_int(length=5):
    min_range = 10**(length-1)
    max_range = int("".join('9' for i in range(length)))
    return random.randint(min_range, max_range)
