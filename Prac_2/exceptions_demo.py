"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Can't divide by 0, choose valid number")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Question 1
""" ValueError will occur if the denominator is a number smaller than 1 (ie 0.9)"""
# Question 2
""" This will occur if you try to enter 0 as the value of the denominator"""
# Questions 3
""" Added an error checking while loop to prevent entering 0 which cuases the error"""
