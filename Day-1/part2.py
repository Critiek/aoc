line_characters = []
line_characters_string = ''
lines = []
digits = []
unfinished_digits = []
numbers = {
   "one": 1,
   "two": 2,
   "three": 3,
   "four": 4,
   "five": 5,
   "six": 6,
   "seven": 7,
   "eight": 8,
   "nine": 9
}

with open('./input.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    try:
        digits.append(unfinished_digits[0] + unfinished_digits[-1])
    except:
        pass
    line_characters.clear()
    print(line)
    for char in line:
        line_characters.append(char)
        # print(line_characters)
        line_characters_string = ''.join(line_characters)
        for number in numbers:
            if number in line_characters_string:
                unfinished_digits.append(numbers[number])
                print(line_characters)
                line_characters = line_characters[-2:]
                print(line_characters)
                print(numbers[number])

    # line = [char for char in line if char.isnumeric()]
    # digits.append(line[0] + line[-1])

print(digits)
print(sum(int(i) for i in digits))
