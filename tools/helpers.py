from collections import Counter
from random import choice

def generate_random_num_w_excl_num(min_range, max_range,excluded_nums=[None]):
    return choice([num for num in range(min_range,max_range)
    if num not in excluded_nums])       

# prints a random value from the list 
list1 = [1, 2, 3, 4, 5, 6]  
print(choice(list1))    #this is actually random.choice but random is imported
print(*(num for num in range(0,20))) #num for num in range(0,20) is a python generator object where * unpacks it
print([num for num in range(0,20)])   #can unpack a generator function by encapsulating it in a list  
print([num for num in range(0,20) if num not in list1]) #can perform conditionals directly onto a generator function
print(choice([num for num in range(0,20) if num not in list1])) #finally perform a random choice on this list


def generate_random_num(min_range, max_range):
    return choice(list(range(min_range,max_range)))

def get_random_element_of_list(list1):
    return list1[generate_random_num(0,len(list1))]

