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

similarity = []
id = 0
while id < len(list_1):
    similarity_score = 0
    print()
    print(list_1[id])
    similarity_score = int(list_1[id]) * int(list_2.count(list_1[id]))
    similarity.append(int(similarity_score))
    print(f"Current similarity: {str(sum(similarity))}")
    id += 1
