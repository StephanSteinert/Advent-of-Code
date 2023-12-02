###########################################################################
### Setup
# Set state of challenge
FINISHED = True

# Imports
import sys

# Data files
PATH      = sys.path[0]
FILENAMES = [PATH + "\\..\\example.txt", PATH + "\\..\\input.txt"]

# Define vars
finalResult = 0
###########################################################################



###########################################################################
### Special code for each challenge
# Challenge:
# For each game, find the minimum set of cubes that must have been present.
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
# Expected test result: 2286
testResult = 2286

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

    # Extract individual rounds
    rounds = _a[1].split("; ")

    # Iterate over each round and extract cubes
    for round in rounds:
        # Separate cubes in each round
        cubes = round.split(", ")

        # Iterate over cubes to extract color and amount
        # and largest amount per color
        for color in cubes:
            if color.find(" red") != -1:
                _red = int(color.replace(" red", ""))
                if _red > red: red = _red
            if color.find(" green") != -1:
                _green = int(color.replace(" green", ""))
                if _green > green: green = _green
            if color.find(" blue") != -1:
                _blue = int(color.replace(" blue", ""))
                if _blue > blue: blue = _blue
      
    # Publish game id if result is valid
    result = red * green * blue

    if not FINISHED:
        print("\n###")
        print("Input: " + line)
        print("Game id: " + id)
        print("Power: " + str(result))

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