import re

test = input("test? y/n\n>")

match test:
    case "y":
        path = "test_input.txt"
    case "n":
        path = "input.txt"

with open(path, "r") as file:
    data = file.read().strip()

filtered_data = re.finditer(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", data)

total = 0

continuing = False

for pair in filtered_data:
    pair = pair.group()
    print(pair)
    if pair == "do()":
        continuing = False
        continue
    elif pair == "don't()":
        continuing = True
        continue
    if continuing:
        continue
    pair = pair[4:-1]
    pair = pair.split(",")
    print(pair)
    total += int(pair[0]) * int(pair[1])

print(total)

# looking for mul(#,#)