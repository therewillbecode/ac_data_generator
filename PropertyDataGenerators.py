__author__ = 'Tom'
__author__ = 'Tom'
import random
import time
import string


def get_current_timestamp():
    result = time.strftime("%H:%M:%S%d/%m/%Y/")
    return "\'" + str(result) + "\'"


def get_rand_int(length):
    result = ''.join(random.choice(string.digits) for i in range(length))
    return "\'" + str(result) + "\'"


def get_rand_positive_double(upperbound):
    result = random.random() * upperbound
    return "\'" + str(result) + "\'"


def get_rand_text(max_length, min_length):
    length = random.randrange(min_length, max_length)
    result = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(length))
    return "\'" + str(result) + "\'"


def get_rand_boolean():
    result = random.choice([True, False])
    return "\'" + str(result) + "\'"


print(get_rand_int(2))
