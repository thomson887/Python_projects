# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:20:25 2022

@author: justi
"""
# x = 5
# y= 8

# z = x + y
# print(z) 

# #The input command by default is of String datatype. setting the variable type of x to integer. 
#If not specifically mentioned then it makes it into a string
# #x= input('Enter value of x: \n>>> ')

# #x = int(input('Enter value of x:\n>>> '))
# #print(type(x))

# Radius = float(input("Enter value of radius of the circle: "))
# pi = 3.14159
# area_of_circle = pi * Radius**2
# print('You entered the radius as', Radius, 'The area of the circle is' ,area_of_circle)

#Convert Fahrenheit to Celsius

far = float(input('Enter temperature in Fahrenheit: \n>>> '))
cel = (far - 32) * 5/9
print(far, 'Fahrenheit in celsius is', cel)

# Learning Conditional statements
some_condition = False

#The default position of the IF statement is True
if some_condition:
    print("The variable some_condition is True")
else:
    print("The variable some_condition is False")


# IF-ELIF-ELSE

temp = int(input("Enter temperature in Fahrenheit: \n>>> "))

if temp > 100:
    print("Too hot to go outside")
elif temp >= 85 and temp <= 100:
    print("Wear sunscreen when you go out")
elif temp >=70 and temp <= 84:
    print("Perfect weather to go out")
else:
    print("Too cold to go outside")
    
    
#Working with strings

my_string = 'Python'

len(my_string)
my_string[0:4]
my_string[:4]
upper = my_string.upper()
lower = my_string.lower()   
firstlettercapital = my_string.capitalize()

#Python is case sensitive therefore 'n' != 'N'

#Exercise 1

number  = int(input("PLease enter a number between 1 and 5 inclusive: \n>>> "))

if number == 1:
    print("The number is One")
elif number ==2:
    print("The number is Two")
elif number ==3:
    print("The number is Three")
elif number ==4:
    print("The number is Four")
elif number == 5:
    print("The number is Five")
else:
    print("The number entered is not between 1 and 5")
    
#Exercise 2

number_string  = input("PLease enter a string between 1 and 5 inclusive: \n>>> ")
number = number_string.lower()
if number == 'one':
    print("The number is 1")
elif number == 'two':
    print("The number is 2")
elif number == 'three':
    print("The number is 3")
elif number == 'four':
    print("The number is 4")
elif number == 'five':
    print("The number is 5")
else:
    print("The number entered is not between 1 and 5")
    

#eXERCISE 3

guess = 3
numberguess = input("Guess the number between 1 and 10: \n>>> ")

if numberguess.isdigit():
    numberguess = int(numberguess)
    if numberguess == 3:
        print("You have guessed the correct number")
    elif numberguess > guess and numberguess < 10:
        print("You have guessed too high, try again")
    elif numberguess < 3 and numberguess > 1:
        print("The number guessed is too low, try again")
    else:
        print("The number guessed is out of range")
else:
    print("The number should be an integer only")
    


#LOOPS
#FOR LOOP

for i in range(10):
    print(i)
    

#for loop exercises
#1

# =============================================================================
# ask the user for 2 numbers between 1 and 100. Then count from the lower number to the higher number print results on screen.
# =============================================================================


num_1 = int(input('please enter a number between 1 and 100:> '))
num_2 = int(input('please enter a number between 1 and 100:> '))



while num_1<0 or num_1>100 or num_2 < 0  or num_2 > 100:
    try:
        print("the number is not between 1 and 100, try again")
        num_1 = int(input('please enter a number between 1 and 100:> '))
        num_2 = int(input('please enter a number between 1 and 100:> '))
    except ValueError:
        print("invalid input. Please enter a valid integer.")

if num_1 < num_2:
    for i in range (num_1,num_2):
        print(i, end=' ')
        #putting end appends the data while printing it. default the next print will be in next line

else: 
    for i in range (num_2, num_1):
        print(i, end=' ')
        






def validate_input(value):
    # Check if the value is an integer
    if not isinstance(value, int):
        print("Error: Value must be an integer.")
        return False
    
    # Check if the value is between 1 and 100
    if not (1 <= value <= 100):
        print("Error: Value must be between 1 and 100.")
        return False
    
    return True

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if validate_input(value):
                return value
        except ValueError:
            print("Error: Please enter an integer.")
            
def func1(num_1, num_2):
    if num_1 < num_2:
        for i in range (num_1,num_2):
            print(i, end=' ')
            #putting end appends the data while printing it. default the next print will be in next line

    else: 
        for i in range (num_2, num_1):
            print(i, end=' ')


value1 = get_valid_input("Enter the first value: ")
value2 = get_valid_input("Enter the second value: ")

print("Both inputs are valid:", value1, value2)

func1(value1, value2)






# =============================================================================
# 2. ask the user to input a string and then print it out in reverse order
# =============================================================================
   
def validate_input2(value):
    if not isinstance(value, str):
        print("Error! Input must be a string")
        return False
    
    if not value.isalpha():
        print("Error! Input must be a string.")
        return False
    return True

def get_valid_input2(prompt):
    while True:
        try:
            value = str(input(prompt))
            if validate_input2(value):
                return value
        except ValueError:
            print("Error! Please enter string:")


def func2(string):
    reverse_string = ' '
    for char in string:
        reverse_string = char + reverse_string
    return reverse_string
        
    
    
string_1 = get_valid_input2('please enter a string:> ')


print(func2(string_1))

#can also be done using indexes
print(string_1[::-1])

# =============================================================================
# 3. Input a number between 1 and 12 and get the times table for that number
# =============================================================================


user_input = input("Enter a number between 1 and 12:> ")

while (not user_input.isdigit() or not (1 <= int(user_input) <= 12)):
    print("Error! Input must be an integer between 1 and 12 only")
    user_input = input("Enter a number between 1 and 12:> ")

user_input = int(user_input)    
print(f'This is the {user_input} times table')

for i in range (1,11):
    print(f'{i} x {user_input} = {i*user_input}')


# =============================================================================
# 4. Ammend the 3rd exercise to obtain all the times tables between 1 and 10
# =============================================================================

for i in range (1,11):
    print('====================================================')
    for j in range (1,11):
        print(f'{i} * {j} = {i*j}')
        
# =============================================================================
# 5. ask user to input a sequence of numbers and calculate the mean and print the result
# =============================================================================

user_input = input('Please enter a number or type exit to stop:> ')

numbers = []
while (user_input.lower() != 'exit'):
    while (not user_input.isdigit()):
        print("input should only be a number")
        user_input = input('try again:> ')
    
    numbers.append(int(user_input))
    user_input = input('input next number:> ')

total = 0
for number in numbers:
    total += number
    
print(f'mean is {total/len(numbers)}')
print(sum(numbers)/len(numbers))


# =============================================================================
# calculate the factorial of a number
# =============================================================================

user_input = input('Please enter a number:> ')

while (not user_input.isdigit()):
    print("Error! Please enter only integers")
    user_input = input("Try again:> ")
fact = 1
user_input = int(user_input)
for i in range(1, user_input + 1):
    fact = fact * i

print(fact)

# =============================================================================
# fibonacci sequence
# =============================================================================

n = 50

a = 0
b = 1

fib_nums = []

for i in range (1, n):
    fib_nums.append(a)
    a,b = b,a+b
print(fib_nums)

# =============================================================================
# code to determine all odd and even numbers between 1 and 100. put odds in a 
# list named odd and even in a list named even.
# =============================================================================

n = 100

evens =[]
odds = []

for i in range(n+1):
    if not i % 2:
        evens.append(i)
    else:
        odds.append(i)
        
print(f'The evens are {evens}')
print(f'The odds are {odds}')

# =============================================================================
# # Defining functions
# #1
# =============================================================================
def my_func():
    print("Hello")
    print("How was your day") 
    
    
my_func()

# =============================================================================
# #2
# =============================================================================
def name_func(fname):
    print(fname + " Refsnes")
    
    
name_func("Justin")


# =============================================================================
# #3
# =============================================================================
def name_func2(firstname, lastname):
    print("The name is " + firstname + " " + lastname)
    
name_func2("Justin", "Thomson")
    
# =============================================================================
# #4
# # the order/sequence of the arguments will not matter in this example
# =============================================================================

def name_func3(arg1, arg2, arg3):
    print("The youngest child is " + arg3)
    
name_func3(arg2= "Justin", arg3 = "Sofiya", arg1 = "Yasmin")

# =============================================================================
# #5
# #if the number of arguments is not known then we can use **before the parameter name in the function definition
# 
# =============================================================================
def name_func4(**kid):
    print("The kids name is "+ kid["fname"])
    
name_func4(fname = "Sofiya", lname="Thomson")


# =============================================================================
# #6
# #default argument value when argument is not fed
# =============================================================================

def name_func5(country = "India"):
    print("The country's name is "+ country)
    
name_func5("Norway")
name_func5("USA")
name_func5()


# =============================================================================
# #7
# #Passing a list as an argument
# =============================================================================

def name_food(food):
    for x in food:
        print(x)
    # print(food[2])
        
a = ["rice", "curd", "dal"]

name_food(a)


# =============================================================================
# #8
# # To let a function return a value use return statement.
# =============================================================================

def my_func2(x):
    return x * 5

print(my_func2(3))
print(my_func2(4))
  
  
myList = ["python"]
for i in myList:
    myList.append(i.upper())
print(myList)





































    
