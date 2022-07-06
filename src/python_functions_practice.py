from calendar import calendar
from curses.ascii import isdigit
from datetime import date


def return_10(): 
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1*number_2    

def divide(number_1, number_2):
    return number_1/number_2    

def length_of_string(length):
    return len(length) 

def join_string(number_1, number_2):
    return number_1 + number_2    

def add_string_as_number(number_1, number_2):
    return int(number_1) + int(number_2) 
    
def number_to_full_month_name( month):
    if month == 1:
        return "January"
 
    elif month == 3:
        return "March"

    elif month == 9:
        return "September"    

def number_to_short_month_name( month):
    if month == 1:
        return "Jan"        