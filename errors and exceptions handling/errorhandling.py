'''
Exercise 1: Handling ZeroDivisionError
Instructions:
Write a program that takes two numbers as input from the user and divides the first number by the second number.
Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.
'''
def divide_numbers():
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        result = first_number / second_number
        print(f"the result is : {result}")
        
    except ZeroDivisionError:
        print(f"YOU CANNOT DIVIDE BY ZERO")
    
divide_numbers()

