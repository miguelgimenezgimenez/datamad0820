"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""
from operator import sub,add


print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')

a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

numbers = {
    "negative five":-5,
    "negative four":-4,
    "negative three":-3,
    "negative two":-2,
    "negative one":-1,
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "ten":10,
}
operations = {
    "plus": add,
    "minus": sub
}
try:
    result =operations[b](numbers[a], numbers[c])
    for key, value in numbers.items(): 
        if value == result:
            print(f"{a} {b} {c} equals {key} ")
except KeyError as e:
    print(e, 'i am not able to print this solution')
   

print("Thanks for using this calculator, goodbye :)")
