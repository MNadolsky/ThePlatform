from collections import Counter
from random import choice

class Tools():

    def format_element_list_to_text_list(self,element_list):
        text_list = []
        for element in element_list:
            text_list.append(element.text)
        
        return text_list
    
    def compare_two_lists_sequence_ind(self,list1,list2):
        return Counter(list1) == Counter(list2)

    def generate_random_num(self,min_range, max_range,excluded_nums=[None]):
        return choice([num for num in range(min_range-1,max_range-1)
        if num not in excluded_nums])       

