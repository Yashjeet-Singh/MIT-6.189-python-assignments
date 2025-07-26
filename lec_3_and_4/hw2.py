# Name: Yashjeet Singh
# Section: Self
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

import math
import random
import cmath
# **********  Exercise 2.0 ********** 

def f1(x):
    print (x + 1)

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here
def rps(p1, p2):
    # Following is the different cases of rock paper scissors game incorporated into
    # if elif and else statements
    if (p1 == 'rock' and p2 == 'scissors'):
        print('Player 1 wins.')
    elif (p1 == 'rock' and p2 == 'paper'):
        print('Player 2 wins.')
    elif (p1 == 'rock' and p2 == 'rock'):
        print('Tie.')
    elif (p1 == 'scissors' and p2 == 'scissors'):
        print('Tie.')
    elif (p1 == 'scissors' and p2 == 'paper'):
        print('Player 1 wins.')
    elif (p1 == 'scissors' and p2 == 'rock'):
        print('Player 2 wins.')
    elif (p1 == 'paper' and p2 == 'scissors'):
        print('Player 2 wins.')
    elif (p1 == 'paper' and p2 == 'paper'):
        print('Tie.')
    elif (p1 == 'paper' and p2 == 'rock'):
        print('Player 1 wins.')
    else:
        print("This is not a valid object selection")

# Test Cases for Exercise 2.1
#rps('rock', 'paper')
#rps('paper', 'scissors')
#rps('paper', 'paper')
# ********** Exercise 2.2 ********** 

# Define is_divisible function here
''' this function takes two ints as m and n parameter checks the divisibility
 between them '''
def is_divisible(m, n):
    if n == 0:
        return False  # or raise an exception
    return m % n == 0

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print is_divisible(10, 5)  # This should return True
#print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return? -- ZeroDivisionError


# Define not_equal function here
def not_equal(m, n):
    if m == n:
        return False
    else:
        return True

# Test cases for not_equal
#print not_equal(3, 3)
#print not_equal(5, 3)
#print not_equal(1, 9)

# ********** Exercise 2.3 ********** 

## 1 - multadd function
def multadd(a, b, c):
    result = a*b+c
    return result

## 2 - Equations
angle = multadd(math.pi, 0.25, 0)
sine = multadd(2, math.sin(angle), 0)
cosine = multadd(math.cos(angle), 1, 0)
sums = multadd(1, sine, cosine)

t1 = math.ceil(multadd(276, 1.0/19, 0))
t2 = multadd(2, math.log(12, 7), 0)

# Test Cases
angle_test = multadd(0.5, sums, 0)
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test = t1 + t2
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)

## 3 - yikes function
def yikes(x):
    com_term = math.exp(-x)
    result = multadd(x, com_term, math.sqrt(multadd(1, 1, -com_term))) 
    return result


# Test Cases
x = 5
print("yikes(5) =", yikes(x))

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    number = random.randint(0, 100)
    if number%3 == 0:
        return True
    else:
        return False

# Test Cases
print(rand_divis_3())

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has

def roll_dice(sides, dices):
    for i in range(dices):
        print(random.randint(1, sides))
    print("That's all!")

# Test Cases
roll_dice(6, 3)
roll_dice(3, 3)
roll_dice(1, 3)

# ********** Exercise 2.5 **********

# code for roots function
def roots(a, b, c):
    d = b*b - 4*a*c  # discriminant
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("Root 1 is", r1)
        print("Root 2 is", r2)
        print("Roots are Real")
    elif d == 0:
        r = -b / (2*a)
        print("Root 1 is", r)
        print("Root 2 is", r)
        print("Roots are double")
    else:
        r1 = (-b + cmath.sqrt(d)) / (2*a)
        r2 = (-b - cmath.sqrt(d)) / (2*a)
        print("Root 1 is:", r1)
        print("Root 2 is:", r2)
        print("Roots are Complex")
    
    
# Test Cases
roots(1, 4, 4)
roots(1, -7, 10)
roots(1, 5, 7)
