################################################################################
#
# Computer Project 02
#
################################################################################


# DO NOT MODIFY THE FOLLOWING 2 LINES OR YOU RISK TO NOT PASS THE TESTS
import random
random.seed(10)

# USE THE FOLLOWING IN YOUR PRINT AND INPUT STATEMENTS
banner = """*** Welcome to the Game of Nim! ***
*Spoiler Alert: I am probably going to win...* 
"""

rules="""Nim is a deceptively simple two-player game where stones mysteriously disappear,
one, two, or three at a time!
The game kicks off with two piles of stones, cleverly named Pile 1 and Pile 2 
(because creativity matters!). Players take turns. 
On your turn, pick a pile and decide how many stones to make vanish: 1, 2, or 3.
The goal? Be the one to remove the very last stone and victory!
But hey, do not feel bad when you lose...I have had lots of practice!
"""
print(banner)
print(rules)

user_input = int(input(":~Would you like to play? (0=no, 1=yes) ~:"))

if user_input == 1:
    print(":~How many stones per pile would you like to play? ~:")
    stones_1 = int(input("Start --> Pile 1:"))
    stones_2 = int(input("   Pile 2:"))
    print("\nStarting a new game...")

    while stones_1 !=0 and stones_2 != 0:
        #User Turn
        user_pile = int(input(":~Choose a pile (1 or 2) ~:"))
        if user_pile != 1 and user_pile != 2:
            while user_pile != 1 and user_pile != 2:
                user_pile = int(input("Pile must be 1 or 2 and non-empty. Please try again."))
        elif(user_pile == 1):
            user_removeinput = int(input(":~Choose stones to remove from pile ~:"))
            if user_removeinput == 1 or user_removeinput == 2 or user_removeinput == 3 and user_removeinput <= stones_1:
                stones_1 = stones_1 - user_removeinput
            else:
                while user_removeinput != 1 and user_removeinput != 2 and user_removeinput != 3 and user_removeinput > stones_1:
                    user_removeinput = int(input(":~Please choose 1, 2 or 3 stones~:"))
        if user_pile == 2:
            user_removeinput = int(input(":~Choose stones to remove from pile ~:"))
            if user_removeinput == 1 or user_removeinput == 2 or user_removeinput == 3 and user_removeinput <= stones_2:
                stones_2 = stones_2 -  user_removeinput
            else:
                while user_input != 1 and user_input != 2 and  user_input != 3 and user_removeinput > stones_2:
                    user_removeinput = int(input(":~Please choose 1, 2 or 3 stones~:"))
                stones_2 = stones_2 - user_removeinput
        if stones_1 == 0 and stones_2 ==0:
            print("You actually won! Did you cheat?")
        print("Score -> human:")
        print("Pile 1:", stones_1)
        print("Pile 2:", stones_2)

    #Computer Turn
        if stones_1 !=0 and stones_2 !=0:
            computer_pile = random.randint(1,2)
            if(computer_pile == 1):
                computer_removeinput = random.randint(1,3)
                stones_1 = stones_1 -  computer_removeinput
            else:
               computer_removeinput = random.randint(1, 3)
               stones_2 = stones_2 - computer_removeinput

            print("Pile 1:", stones_1)
            print("Pile 2:", stones_2)

if stones_1 == 0 and stones_2 == 0:
    print("\nThanks for playing! See you again soon!")





#"\nThanks for playing! See you again soon!"
#"Score -> human:"
#"; computer:"
#"Remove"
#"stones from pile"




