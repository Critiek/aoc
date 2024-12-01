with open("input.txt", "r") as file:
    data = file.read().strip()

data = data.split("\n")

list_1 = []
list_2 = []

for pair in data:
    pair = pair.split("   ")
    list_1.append(pair[0])
    list_2.append(pair[1])

list_1.sort()
list_2.sort()

ranges = []
id = 0
while id < len(list_1):
    # while id < 5:
    temp_list = []
    print()
    print(list_1[id] + " 1")
    print(list_2[id] + " 2")
    temp_list.append(list_1[id])
    temp_list.append(list_2[id])
    temp_list.sort()
    current_range = len(range(int(temp_list[0]), int(temp_list[1])))
    print("range: " + str(current_range))
    ranges.append(current_range)
    print("Current sum: " + str(sum(ranges)))
    id += 1
