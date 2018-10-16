
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
def main()
   for i in range(5):
       number = input("Number: ")
       numbers.append(number)
    print("The First number is", numbers[0])
   print("The Last number is :", numbers[-1])
   print("The Smallest Number is", min(numbers))
   print("The largest number is", max(numbers))
   print("The Average number is", sum(numbers) / len(numbers))


#Woefully inadequate security checker...
    username = input("Enter username: ")
   if username in usernames:
       print("Access Granted")
   else:
       print("Access Denied")


main()