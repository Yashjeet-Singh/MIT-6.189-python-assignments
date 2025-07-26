# Name: Yashjeet Singh
# Date: June 8th, 2025
# nims.py

'''
This program simulates a two-player version of the game Nims (also called Stones).
Starting with a pile of stones, players take turns removing 1 to a maximum allowed
number of stones. Input is validated to ensure legal moves. The game continues until
the pile is empty, and the last player to make a move is declared the winner.
'''

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    ## Basic structure of program (feel free to alter as you please):

    while pile > 0:    # starting the loop as pile is not zero
        p1 = int(input("Player 1's turn: ")) # asking the player 1 for the first time
        # if turn by p1 is not valid, used while loop repeatedly to make sure game only continues after the valid turn
        while type(p1) != type(1) or p1 > max_stones or p1 > pile or p1 < 1:   
            print("Enter legal number")       # printing the warning message
            p1 = int(input("Player 1's turn: "))  # asking them to enter their turn again 
        pile = pile - p1                  # if entered correctly, executing their move, deducting stones from the pile
        print ("Stones left in pile:", pile) # printing the left number of stones in pile

        if pile != 0:            # if the pile is not emptied by player 1, only ask then player 2 to enter, otherwise p1 won
            p2 = int(input("Player 2's turn: "))  # asking the player 2

            # performing validity check through while loop on the turn played by p2
            while type(p2) != type(1) or p2 > max_stones or p2 > pile or p2 < 1:
                print ("Enter legal number")   # printing warning message
                p2 = int(input("Player 2's turn: "))  # asking them again
            pile = pile - p2       # if they entered correct, exiting them from the loop and executing their move
            print ("Stones left in pile:", pile) # printing the stones left, if zero, get out of the outer most loop
            
        

    print ("Game over, Last Player Won")      # after getting out of the loop, printing game over

play_nims(100, 5)
