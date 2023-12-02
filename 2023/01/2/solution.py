# https://www.w3schools.com/python/python_regex.asp
import re

x   = 1
sum = 0
#file_name = "example.txt"
file_name = "../input.txt"

# Open the file
file = open(file_name, "r")

# Iterate over each line
for line in file:  
    # Replace number words with real numbers
    # one|two|three|four|five|six|seven|eight|nine
    
    # Find leftmost digit
    left = "0"
    y = re.search("[0-9]|one|two|three|four|five|six|seven|eight|nine", line)
    if y: left = y.group()
    left = re.sub("one",   "1", left)
    left = re.sub("two",   "2", left)
    left = re.sub("three", "3", left)
    left = re.sub("four",  "4", left)
    left = re.sub("five",  "5", left)
    left = re.sub("six",   "6", left)
    left = re.sub("seven", "7", left)
    left = re.sub("eight", "8", left)
    left = re.sub("nine",  "9", left)

    # Find rightmost digit
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    right = "0"
    y = re.search("[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", line[::-1])
    if y: right = y.group()
    right = re.sub("eno",   "1", right)
    right = re.sub("owt",   "2", right)
    right = re.sub("eerht", "3", right)
    right = re.sub("ruof",  "4", right)
    right = re.sub("evif",  "5", right)
    right = re.sub("xis",   "6", right)
    right = re.sub("neves", "7", right)
    right = re.sub("thgie", "8", right)
    right = re.sub("enin",  "9", right)

    # Combine digits
    digits = left + right

    # Cast digit to int and add to sum
    sum += int(digits)

    print(str(x) + ": " + line + " = " + digits)
    x += 1

print("============")
print("Sum: " + str(sum))

file.close()