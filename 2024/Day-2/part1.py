with open("input.txt", "r") as file:
    data = file.read().strip()

data = data.split("\n")

safe_entries = []

for entry in data:
    print("\n\n===========\nNew set!\n===========")
    viable = True
    entry = entry.split(" ")
    if int(entry[1]) > int(entry[0]):
        ascending = True
    else:
        ascending = False
    print(f"Ascending = {ascending}")
    last_num = 0
    for iter, num in enumerate(entry):
        print(iter, num)
        if iter > 0 and ascending and last_num > int(num):
            viable = False
            print("break at 1")
            break
        if iter > 0 and not ascending and last_num < int(num):
            viable = False
            print("break at 2")
            break
        if iter > 0 and (abs(int(num) - last_num) > 3 or abs(int(num) - last_num) < 1):
            viable = False
            print("break at 3")
            break
        last_num = int(num)
    if viable:
        safe_entries.append(entry)
    print(f"viable = {viable}")
# print(safe_entries)
print(f"\nTOTAL VIABLE ENTRIES = {len(safe_entries)}")


# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
