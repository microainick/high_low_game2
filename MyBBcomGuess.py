#import
import random
#make ran be a random integer between 1 and 128)
ran = random.randint(1, 128)
int(ran)
#it probably was an integer but that was to ensure it.
#Print eplanation
#spacing for readability
#i like the formatting this way with spaces

print("  ")
print("If the computer has 7 chances to calculate the Secret Number then our range can excede 100")
print("   ")
print("To go above and beyond we will allow the Secret Number to be bewteen 1 and 128")
print("   ")
print("Certainly this can still be done in 7 turns")
print("   ")
print("   ")

#print secret number to the screen, to show the user the computers goal
#use .format
print("The Secret number randomly generated is {}".format(ran))

#create a function to generate computer guesses
#ran is the secret number
#previous com guess is cg1
#change is half the interval remaining
#cg2 is the next guess
#if ran is greater than cg1, then cg2 is cg1 plus change
#if ran is less than cg1, then cg2 is cg1 minus change
#then print higher or lower respectively
#return next guess as cg2

def Eval(cg1, change):
    if ran > cg1:
        cg2 = cg1 + change
        print("The Secret number is Higher")
    if ran < cg1:
        cg2 = cg1 - change
        print("The Secret number is Lower")
    return cg2

#make variable for solution found (solfnd)
#set solfnd to false and use to conitue
#change solfnd to true if computer completes task

solfnd = False

#first guess will always be 64
#make that an integer
#print the round #
#display the next guess

cg1 = 64
int(cg1)
print("Round 1")
print("Computer selects {}".format(cg1))

#if computer gets the secret number then print computer wins
#if computer wins, change solfnd to true

if ran == cg1:
    print("Computer wins")
    solfnd = True

#as long as solution is not found continue
#generate next com guess with 32 as the plus or minus
#display the round number
#show com guess with .format
#end game if computer is right

if solfnd == False:
    cg2 = Eval(cg1, 32)
    input("press enter to continue")
    print("Round 2")
    print("Computer selects {}".format(cg2))
    if ran == cg2:
        print("Computer wins")
        solfnd = True

#as long as solution is not found continue
#generate next com guess with 16 as the plus or minus
#display the round number
#show com guess with .format
#end game if computer is right

if solfnd == False: 
    cg3 = Eval(cg2, 16)
    input("press enter to continue")
    print("Round 3")
    print("Computer selects {}".format(cg3))
    if ran == cg3:
        print("Computer wins")
        solfnd = True

#as long as solution is not found continue
#generate next com guess with 8 as the plus or minus
#display the round number
#show com guess with .format
#end game if computer is right
        
if solfnd == False:
    cg4 = Eval(cg3, 8)
    input("press enter to continue")
    print("Round 4")
    print("Computer selects {}".format(cg4))
    if ran == cg4:
        print("Computer wins")
        solfnd = True

#as long as solution is not found continue
#generate next com guess with 4 as the plus or minus
#display the round number
#show com guess with .format
#end game if computer is right

if solfnd == False:
    cg5 = Eval(cg4, 4)
    input("press enter to continue")
    print("Round 5")
    print("Computer selects {}".format(cg5))
    if ran == cg5:
        print("Computer wins")
        solfnd = True

#as long as solution is not found continue
#generate next com guess with 2 as the plus or minus
#display the round number
#show com guess with .format
#end game if computer is right

if solfnd == False:
    cg6 = Eval(cg5, 2)
    input("press enter to continue")
    print("Round 6")
    print("Computer selects {}".format(cg6))
    if ran == cg6:
        print("Computer wins")
        solfnd = True

#as long as solution is not found continue
#generate next com guess with 1 as the plus or minus
#display the round number and that it is the last
#show com guess with .format and that it must be right
#end game because the computer will be right!

if solfnd == False:
    cg7 = Eval(cg6, 1)
    input("press enter to continue")
    print("Final Round;  Round 7!")
    print("The Computer says your number must be {}".format(cg7))
    keepitgoing = False

    
