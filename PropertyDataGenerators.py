__author__ = 'Tom'
import random
import time
import string


def get_current_timestamp():
    return time.strftime("%H:%M:%S%d/%m/%Y/")


def get_rand_int(length):
    return ''.join(random.choice(string.digits) for i in range(length))


def get_rand_positive_double(upperbound):
    return random.random() * upperbound


def get_rand_text(max_length, min_length):
    length = random.randrange(min_length, max_length)
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(length))


def get_rand_boolean():
    return random.choice([True, False])

print(get_rand_boolean())
