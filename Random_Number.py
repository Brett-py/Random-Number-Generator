import random

points = 0 #this defines the points that the player will earn
rounds = 0 #this defines the number of rounds after the while loop restarts 



# This is the main program
while True:
    numPick = random.randint(1, 10) #this creates the actual number generator
    print()
    print('please pick a number between 1 and 10')
    playerGuess = (int(input()))
    if playerGuess == numPick:
        points += 1
        print('Congratulations, you guessed correctly with ' + (str(int(numPick)))) 

    else:
        print('Sorry, I was thinking of ' + (str(int(numPick))))


    if (int(points)) == 1:
        print('You currently have ' + (str(int(points))) + ' point!')
    if (int(points))!= 1:
        print('You currently have ' + (str(int(points))) + ' points!')
    rounds += 1

    if rounds >= 5:

        print()
        print('Would you like to stop playing now?') #quick player promt that asks if they would like to stop playing after five rounds have passed
        playerResponse = input()
        if playerResponse == 'Yes' or 'yes':
            break
        else:
           
            
            
     




        
    
    







