test = input("test? y/n\n>")

match test:
    case "y":
        path = "test_input.txt"
    case "n":
        path = "input.txt"

with open(path, "r") as file:
    data = file.read().strip()

data = data.split("\n")

for line in range(len(data)):
    if data[line] == "":
        splitting_line = line

page_ordering_rules = data[:splitting_line]
updates = data[splitting_line:]
updates.pop(0)

print(page_ordering_rules)
print()
print(updates)
