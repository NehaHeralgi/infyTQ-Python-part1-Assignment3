'''
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.
'''
#lex_auth_01269441913243238467

def create_largest_number(number_list):
    
    max=0 
    number_list.sort()
    number_list.reverse()
    
    for i in number_list:
        max=max*100+i 
    return max

number_list=[19,27,99]
largest_number=create_largest_number(number_list)
print(largest_number)