# Example:


import random
import math
import os
import sys
eggs = (1, 3, 8, 3, 2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

# Insert here the module/library import statements


# 1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [k**2 for k in range(0, 20)]

print("\n 1. \n", square)

# 2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
power_of_two = [2**k for k in range(0, 20)]
print("\n 2. \n", power_of_two)

# 3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.
# Remember to use list comprehensions and to print your results

sqrt = [math.sqrt(k) for k in range(0, 100)]
print("\n 3. \n", sqrt)


# 4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list = list(range(-10, 1))
print('\n 4. \n', my_list)


# 5. Find the odd numbers from 1-100. Use odds as the name of the list.
# Remember to use list comprehensions and to print your results
odds = list(range(0, 100, 3))
print('\n 5. \n', odds)

# 6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
divisible_by_seven = [k for k in range(1, 1001) if k % 7 == 0]
print('\n 6. \n', divisible_by_seven)
# 7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
vowels = 'aeiou'
teststring = 'Find all of the words in a string that are monosyllabic'


def remove_chars_from_string(str, chars):
    return [v for v in str if v not in chars]


non_vowels = remove_chars_from_string(teststring, vowels)
print('\n 7. \n', non_vowels)

# 8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'.
# Use capital_letters as the name of the list.
# Remember to use list comprehensions and to print your results
fox = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = [k for k in fox if ord(k) >= 65 and ord(k) <= 90]
print('\n 8. \n', capital_letters)

# 9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
sentence = 'The quick brown fox jumped over the lazy dog.'
consonants = remove_chars_from_string(sentence, ' aeiou.')

print('\n 9.  \n', consonants)

# 10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

files = [f for f in os.listdir('../../') if not os.path.isfile(f)]


print('\n 10. \n', files)
# 11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list.
# You will probably need to import random module
# Remember to use list comprehensions and to print your results
items = range(0, 100)
random_lists = [random.choices(items, k=4) for i in range(0, 4)]
print('\n 11. \n', random_lists)


# 12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [x for sub in list_of_lists for x in sub]

print('\n 12. \n', flatten_list)
# 13. Convert the numbers of the following nested list to floats. Use floats as the name of the list.
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'],
                 ['30', '20', '30', '50', '10', '30', '20', '20', '20'], [
                     '100', '100'], ['100', '100', '100', '100', '100'],
                 ['100', '100', '100', '100']]


floats = [  [ float(i) for i in arr ] for arr in list_of_lists]

print('\n 13. \n', floats)

# 14. Handle the exception thrown by the code below by using try and except blocks.


for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError as e :
        print(e)


# 15. Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use.

x = 5
y = 0
try:
    z = x/y
    pass
except ZeroDivisionError as err:
    print(err)


# 16. Handle the exception thrown by the code below by using try and except blocks.
# Check in provided resources the type of error you may use.

abc=[10,20,20]
try:
    print(abc[3])
except IndexError as e:
    print(e)


# 17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user.
# Hint: take a look on python input function.
# Check in provided resources the type of error you may use.

try:
    user_input_A = int(input('Enter input A'))
    user_input_B = int(input('Enter input B'))

    user_input_A / user_input_B
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as err:
    print(err)



# 18. Handle the exception thrown by the code below by using try and except blocks.
# Check in provided resources the type of error you may use.

try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError as e:
    print(e)


# 19. Handle the exceptions that can be thrown by the code below using try and except blocks.
# Hint: the file could not exist and the data could not be convertable to int
try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())

except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
    


# 20. The following function can only run on a Linux system.
# The assert in this function will throw an exception if you call it on an operating system other than Linux.
# Handle this exception using try and except blocks.
# You will probably need to import sys

def linux_interaction():
    
    try:
        assert('linux' in sys.platform) # "Function can only run on Linux systems."
    except AssertionError as e:
        print(f"{sys.platform} is the platform")
    print('Doing something.')

linux_interaction()
# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

# 21.  Write a function that asks for an integer and prints the square of it.
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.
while True:
    try:
        user_input = int(input("insert an integer"))
    except ValueError :
        print("Incorrect input")
    else:
        break
    


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9).
# Use results as the name of the list
def isDivisible(num):
    for i in range(2,10):
        if num % i ==0:
          return True
    return False


divisible = [ k for k in range(1,1001) if isDivisible(k) ]

print('\n 22. \n', divisible)

# 23. Define a customised exception to handle not accepted values.
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python
class NotAcceptedError(Exception):
    pass


try:
    Total_Marks = int(input("Enter Total Marks Scored: "))
    Num_of_Sections = int(input("Enter Num of Sections: "))
    if (Num_of_Sections < 2):
        raise NotAcceptedError

except NotAcceptedError as e:
    print("CUSTOM ERROOORRR")
