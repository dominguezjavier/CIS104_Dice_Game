import random


# get random number rolled from the dice step 1
def rollRandomNumber ():
    return random.randint (1, 7) #random.randit gives you an integer.

print (" This is the number you rolled" + (rollRandomNumber) + ".Would you like to roll again? ")



keepRolling = True

while(keepRolling):

    playersChoice = input("If you would like to roll again press y to continue or n to stop. ")

    try:
        intplayersChoice = int(playersChoice)
        
        playersChoice = intplayersChoice

    if  playersChoice == y:
        continue
    else playersChoice == n:
         break 2
         keepRolling = False

print (" Thank you for playing. Keep it rolling. ")

