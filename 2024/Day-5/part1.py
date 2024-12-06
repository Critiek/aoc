path = "test_input.txt"
# path = "input.txt"
with open(path, "r") as file:
    data = file.read().strip()

data = data.split("\n")

for line in range(len(data)):
    if data[line] == "":
        splitting_line = line

page_ordering_rules = data[:splitting_line]
updates = data[splitting_line:]
updates.pop(0)

for rule in range(len(page_ordering_rules)):
    page_ordering_rules[rule] = page_ordering_rules[rule].split("|")

print(page_ordering_rules)

for update in updates:
    update = update.split(",")
    print(update)
    for page in range(len(update)):
        print(page)
        try:
            print((update[page], update[page + 1]))
        except Exception:
            pass
        try:
            if (update[page], update[page + 1]) in page_ordering_rules:
                print(update[page], update[page + 1])
        except Exception as e:
            print(f"{e}, End of update")
