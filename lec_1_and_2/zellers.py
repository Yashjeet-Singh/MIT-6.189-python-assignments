# Yashjeet Singh
# May 21st, 2025
# zellers.py

'''
This Python program calculates the day of the week for a user's birthdate using Zeller�s Congruence.
It takes input for year, month, and day, adjusts the month and year as per the algorithm, and
computes intermediate values to find a number (0�6) corresponding to a weekday. It then prints the
day name based on the result.
'''

# Asks the user to enter the date on which they were born
print ("Enter your date of birth in number format")
year = int(input("Year: "))
month = int(input("Month (1-12): "))
day = int(input("Day (1-31): "))

# making month march as value 1 for the algorithim
month = month - 2

# for month 1 and 2 entered
if month == -1:
    month = 11
if month == 0:
    month = 12
    
# implementing rules as stated by algorithim
if (month == 11 or month == 12):
    year = year - 1
    
# Storing the last 2 digits in C, as they are the year of the century    
C = year%100

# storing the century number of the year in D
D = (year - C)//100

# Following is the algorithm stated in the homework
W = (13*month - 1) // 5 
X = C // 4 
Y = D // 4 
Z = W + X + Y + day + C - 2*D 
R = Z%7

if R == 0:
    print ("You were born on a beautiful Sunday!")
elif R == 1:
    print ("You were born on a beautiful Monday!")
elif R == 2:
    print ("You were born on a beautiful Tuesday!")
elif R == 3:
    print("You were born on a beautiful Wednesday!")
elif R == 4:
    print("You were born on a beautiful Thursday!")
elif R == 5:
    print("You were born on a beautiful Friday!")
elif R == 6:
    print("You were born on a beautiful Saturday!")
else:
    print("There is some issue in the algorithim, Find if you can")
