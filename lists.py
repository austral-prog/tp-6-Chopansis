# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    Remove = [5,4,0]
    nueva = list_to_remove_elements[:]
    for i in (Remove):
        if i <len(nueva):
            del nueva[i]
    return nueva

def add_elements(list_to_add_elements):
    nueva = list_to_add_elements
    nueva.append("Yellow")
    nueva.insert(0, "Pink")
    return nueva 

def is_empty(list_to_check):
    nueva = list_to_check
    if len(nueva) == 0: 
        return True
    else: 
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else: 
            return False
    else: 
        return False
def list_of_lists(list_of_lists_to_modify):
    nueva = list_of_lists_to_modify
    nueva[0] = nueva[0][:2]
    nueva[1] = nueva [1][1:4]
    nueva[2] = nueva [2][-2:]
    return nueva