import random 

randomNum = ""
userInput = ""
tries=0

def randomNumber():
    '''This function will determine a random integer based on the range specified by the user.'''
    global rangeMin
    global rangeMax
    global randomNum
    rangeMin = input("Enter the minimum range. (Default is 0. Leave blank for 0)\n>>> ")
    rangeMax = input("Enter the maximum range. (Default is 100. Leave blank for 100)\n>>> ")

    try:
        #checks if the inputted min range is blank. If yes, then make it 0

        #assigns the min range
        if len(rangeMin.lstrip(" ")) == 0:
            rangeMin = 0
        elif len(rangeMin.lstrip(" ")) != 0:
            rangeMin = int(rangeMin)
        else:
            exit("Messup in rangemin")

        #assigns the max range
        if len(rangeMax.lstrip(" ")) == 0:
            rangeMax = 100
        elif len(rangeMax.lstrip(" ")) != 0:
            rangeMax = int(rangeMax)
        else:
            exit("Messup in rangemax")

        #will raise error if minRange>maxRange
        if rangeMin>rangeMax:
            print("Make sure the minimum value is less than the maximum value!")
            raise MemoryError("GET MORE RAM!")

    #raising error if user enters a string instead of an integer
    except:
        raise ValueError("Maybe stop being creative eh?")
    

    #generate a random integer with the help of random module
    randomNum = random.randint(rangeMin, rangeMax)
    return randomNum



def getAndCheckUserInput():
    '''This function will get the user's input and check if it is equal to the genrated number'''
    #get the user's guess
    userInput = int(input(f"Enter your guess. The number is somewhere between {rangeMin} and {rangeMax}\n>>> "))

    #if guess is incorrect
    if userInput != randomNum:
        global tries
        #Only God knows what I wrote below
        print("Oops! looks like your guess was incorrect. Try again! Maybe a smaller number?") if userInput > randomNum else print("Oops! looks like your guess was incorrect. Try again! Maybe a larger number?")  if userInput < randomNum else ""
        confirm = str(input("Continue? (y/n)\n>>> ")) #confirm if the user wants to continue the game
        tries += 1 #increment tries

        #make an infinite while loop to bombarde the user with unlimites guesses, with their consent ofcourse. Break out of it if they input so.
        while True if confirm == "y" else exit("Bye then."):
            userInput = int(input("Enter another guess\n>>> ")) #get the user's guess
            if userInput == randomNum: #when the guess is correct
                tries += 1 #increment tries
                print(f"CORRECT! You took {tries} try") if tries <= 1 else print(f"CORRECT! You took {tries} tries") #print a congratulation message along with the number of tries it took. Also, print try if onlt one try was taken.
                break #break the infinite loop
            elif userInput != randomNum and userInput > randomNum: #when the guess is incorrect and the guess is greater than the random number
                tries += 1 #increment tries
                print("Maybe try guessing a smaller number?") #print help message
                confirm = str(input("Continue? (y/n)\n>>> ")) #get user's consent to continue
                if confirm.lower() == "n": #break out of the loop if the user wishes to do so
                    print("Bye then.")
                    break
            elif userInput != randomNum and userInput < randomNum: #when the guess is incorrect and the guess is smaller than the random number
                tries += 1 #increment tries
                print("Maybe try guessing a larger number?") #print a help message
                confirm = str(input("Continue? (y/n)\n>>> ")) #get the user's consent to continue
                if confirm.lower() == "n": #break out of the loop if the user wishes to do so
                    print("Bye then.")
                    break
    #case when the guess is correct
    elif userInput == randomNum:
        tries += 1 #increment tries
        print(f"CORRECT! You took {tries} try") if tries <= 1 else print(f"CORRECT! You took {tries} tries") #print a congratulation message along with the number of tries it took. Also, print try if onlt one try was taken.
    

#this is an emulation of a do...while loop. The game will start by itself but if the uses chooses "n", it will break the infinite loop
while True:
    randomNumber()
    getAndCheckUserInput()
    tries = 0 #reset the tries to make the game ready for the upcoming round
    userChoice = input("Another round? (y/n)\n>>> ")
    if userChoice != "y":
        print("Had fun playing with you.")
        break



# TO DO LIST:
#     Make the code "readable"
#     Make the "helping logic" better