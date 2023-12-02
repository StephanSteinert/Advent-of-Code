###########################################################################
### Setup
# Set state of challenge
FINISHED = True

# Imports
import sys

# Data files
PATH      = sys.path[0]
FILENAMES = [PATH + "\\example.txt", PATH + "\\..\\input.txt"]

# Define vars
finalResult = 0
###########################################################################



###########################################################################
### Special code for each challenge
# Challenge:
# Return game id if game has less or equal than 12 red cubes and
# less or equal than 13 green cubes and less or equal than 14 blue cubes
# in each pass
# Expected test result: 8
testResult = 8

def thisIsWhereTheMagicHappens(line):
    # define vars
    result = 0
    red    = 0
    green  = 0
    blue   = 0

    # sanitize input
    line = line.replace("\n", "")

    # Separate the input in game id and games
    _a = line.split(": ")

    # Extract and sanitize game id
    id = _a[0]
    id = id.replace("Game ", "")

    # Extract individual games
    rounds = _a[1].split("; ")
    maxRounds = len(rounds)

    # Iterate over each pass and extract cubes
    valid = True
    for round in rounds:
        # Separate cubes in each game
        cubes = round.split(", ")

        # Iterate over cubes to extract color and amount
        # and add them to the sum
        for color in cubes:
            if color.find(" red") != -1:
                red = int(color.replace(" red", ""))
            if color.find(" green") != -1:
                green = int(color.replace(" green", ""))
            if color.find(" blue") != -1:
                blue = int(color.replace(" blue", ""))

        # Set round as invalid if to many cubes
        if red > 12 or green > 13 or blue > 14: valid = False
      
    # Publish game id if result is valid
    if valid == True: result = int(id)

    if not FINISHED:
        print("\n###")
        print("Input: " + line)
        print("Game id: " + id)
        print("Valid") if result > 0 else print("Not Valid")

    return result
###########################################################################



###########################################################################
### Common code to parse data
# Open data file for read
file = open(FILENAMES[FINISHED], "r")

# Parse the data
for line in file:
    finalResult += int(thisIsWhereTheMagicHappens(line))

# Print result. 
# If example run is enabled, print test result.
if not FINISHED:
    testResultState = "\033[41m --- FAILED --- \033[0m"
    if finalResult == testResult: 
        testResultState = "\033[42m --- PASSED --- \033[0m"

    print("\nResult: " + str(finalResult) + " " + testResultState)
else:
    print("\nResult: " + str(finalResult))

# Close data file
file.close()
###########################################################################