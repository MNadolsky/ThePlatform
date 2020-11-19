from collections import Counter
from random import choice

def generate_random_num(min_range, max_range,excluded_nums=[None]):
    return choice([num for num in range(min_range-1,max_range-1)
    if num not in excluded_nums])       

