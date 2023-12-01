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
    # Check if line contains digits at all else skip
    if line == re.findall(r"\D", line): continue
  
    # Find leftmost digit
    left = "0"
    y = re.search("[0-9]", line)
    if y: left = y.group()

    # Find rightmost digit
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    right = "0"
    y = re.search("[0-9]", line[::-1])
    if y: right = y.group()

    # Combine digits
    digits = left + right

    # Cast digit to int and add to sum
    sum += int(digits)

    print(str(x) + " " + line)
    x += 1

print("============")
print("Sum: " + str(sum))

file.close()