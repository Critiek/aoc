test = input("test? y/n\n>")

match test:
    case "y":
        path = "test_input.txt"
    case "n":
        path = "input.txt"

with open(path, "r") as file:
    data = file.read().strip()

data = data.split("\n")

safe_entries = []


def check_entry(entry, ascending, recursion):
    if not recursion:
        last_num = 0
    viable = True
    for iter, num in enumerate(entry):
        print(iter, num)
        if iter > 0 and ascending and last_num > int(num):
            if recursion:
                viable = False
                print("break at 1")
                break
            del entry[iter]
            print(entry)
            viable = check_entry(entry, ascending, recursion=True)
            return viable
        if iter > 0 and not ascending and last_num < int(num):
            if recursion:
                viable = False
                print("break at 2")
                break
            del entry[iter]
            print(entry)
            viable = check_entry(entry, ascending, recursion=True)
            return viable
        if iter > 0 and (abs(int(num) - last_num) > 3 or abs(int(num) - last_num) < 1):
            if recursion:
                viable = False
                print("break at 3")
                break
            del entry[iter]
            print(entry)
            viable = check_entry(entry, ascending, recursion=True)
            return viable
        last_num = int(num)
    print("outside")
    return viable


for entry in data:
    print("\n\n===========\nNew set!\n===========")
    entry = entry.split(" ")
    if int(entry[1]) > int(entry[0]):
        ascending = True
    else:
        ascending = False
    print(f"Ascending = {ascending}")
    viable = check_entry(entry, ascending, recursion=False)
    if viable:
        safe_entries.append(entry)
    print(f"viable = {viable}")
# print(safe_entries)
print(f"\nTOTAL VIABLE ENTRIES = {len(safe_entries)}")


# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
