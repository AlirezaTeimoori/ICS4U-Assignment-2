'''
---------------------------------------
-- Created by:     Alireza Teimoori  --
-- Created on:     Feb 9 2019        --
-- Created for:    Unit 1-08         --
-- Course Code:    ICS4U             --
-- Teacher Name:   Chris Atkinson    --
---------------------------------------
-- This program generates random     --
-- numbers and add them to array and --
-- find the maximum and minimum in it--
---------------------------------------
In this code, the user can even CHOOSE the length of the list!
'''
import random

def Winner(user, comp):
    answer = comp - user

    if answer == 0: # If both have the same number
        output = "Tie!"
    elif answer < 0: # Computer has ha lower number
        if answer == -2: # User has a paper!
            output = "User Wins!"
        else:
            output = "User Loses!"
    else: # If computer has a higher number
        if answer == 2: # Computer has a paper!
            output = "User Loses!"
        else:
            output = "User Wins!"
    
    return output

dictionary = {
    1 : "Rock",
    2 : "Scissors",
    3 : "Paper"
}

# Asking for and storing data
usernumber = eval(input("Hello and welcome to the RPS Game! \nRock = 1, Scissors = 2, Paper = 3 \nGo! \n"))
compnumber = random.randint(1,3)

# Output:
print ( "User chose: " + dictionary[usernumber] + "\nThe Computer chose: " + dictionary[compnumber] )
if 1 <= usernumber <= 3: # Make sure user is sane!
    print ( "That's right! " + Winner(usernumber, compnumber) )
else:
    print ( "YOU MUST ONLY CHOOSE A NUMBER BETWEEN 1 ~ 3 ! TRY AGAIN!" )