# Yashjeet Singh
# May 21st, 2025
# rps.py

'''
In this code, i am writing the simplest (Not Efficient) possble code to write rock paper
scissors game.
'''

# Asks player 1 to choose between rock, paper and scissors
p1 = input("Player 1? Enter rock, paper or scissors: ").lower()
# Asks player 2 to choose between rock, paper and scissors
p2 = input("Player 2? Enter rock, paper or scissors: ").lower()

# Following is the different cases of rock paper scissors game incorporated into
# if elif and else statements
if (p1 == 'rock' and p2 == 'scissors'):
    print ('Player 1 wins.')
elif (p1 == 'rock' and p2 == 'paper'):
    print ('Player 2 wins.')
elif (p1 == 'rock' and p2 == 'rock'):
    print ('Tie.')
elif (p1 == 'scissors' and p2 == 'scissors'):
    print ('Tie.')
elif (p1 == 'scissors' and p2 == 'paper'):
    print ('Player 1 wins.')
elif (p1 == 'scissors' and p2 == 'rock'):
    print ('Player 2 wins.')
elif (p1 == 'paper' and p2 == 'scissors'):
    print ('Player 2 wins.')
elif (p1 == 'paper' and p2 == 'paper'):
    print ('Tie.')
elif (p1 == 'paper' and p2 == 'rock'):
    print ('Player 1 wins.')
else:
    print ("This is not a valid object selection")
