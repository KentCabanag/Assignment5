#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

from typing import is_typeddict


print("\n\033[33;3m Finding the Lowest Number\033[0m")
print()
def Lowest_number():
    Fnum = int(input("Enter the First Number: "))
    Snum = int(input("Enter the Second Number: "))
    Tnum = int(input("Enter the Third Number: "))
    print()

    if Fnum < Snum and Fnum < Tnum:
        print(f"The Lowest Number is {Fnum}.")
    
    elif Snum < Fnum and Snum < Tnum:
        print(f"The Lowest Number is {Snum}.")
    
    elif Tnum < Fnum and Tnum < Snum:
        print(f"The Lowest Number is {Tnum}.")

    elif Fnum < Snum or Fnum < Tnum:
        print(f"The Lowest Number is {Fnum}.")
    
    elif Snum < Fnum or Snum < Tnum:
        print(f"The Lowest Number is {Snum}.")
    
    else:
        Tnum < Fnum or Tnum < Snum
        print(f"The Lowest Number is {Tnum}.")

Lowest_number()





