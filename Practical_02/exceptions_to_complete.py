"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        number1 = int(input("Enter First Number: "))
        #if number1 <= 0:
         #   print("Invalid Try again")
          #  number1 = int(input("Enter First Number: "))
        number2 = int(input("Enter Second Number: "))
       # if number2 <= 0:
            #print("Invalid Try again")
            #number2 = int(input("Enter Second Number: "))
        multiply = number1 * number2
        pass
    except:  number1, number2 <= 0:
        print("Please enter a valid integer.")
print("Valid result is:", result)