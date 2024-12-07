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

for idx, rule in enumerate(page_ordering_rules):
    page_ordering_rules[idx] = page_ordering_rules[idx].split("|")
    # page_ordering_rules[rule] = (page_ordering_rules[rule][0], page_ordering_rules[rule][1])
    print(page_ordering_rules[idx])

viable_lists = []

for update in updates:
    viable = True
    update = update.split(",")
    print(update)
    for idx, num in enumerate(update):
        if not viable:
            break
        print(idx, num)
        temp_array = []
        temp_array = update.copy()
        temp_array.pop(idx)
        for other_num in temp_array:
            if not viable:
                break
            print(other_num)
            if [other_num, num] in page_ordering_rules and update.index(
                other_num
            ) > update.index(num):
                print("Rule broken!")
                viable = False
            elif [num, other_num] in page_ordering_rules and update.index(
                other_num
            ) < update.index(num):
                print("Rule broken!")
                viable = False

    if viable:
        viable_lists.append(update)
    else:
        continue

print(viable_lists)

final_value = 0

for list in viable_lists:
    print(int((len(list) - 1) / 2))
    final_value += int(list[int((len(list) - 1) / 2)])
    
print(final_value)
