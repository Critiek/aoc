test = input("test? y/n\n>")

match test:
    case "y":
        path = "test_input.txt"
    case "n":
        path = "input.txt"

with open(path, "r") as file:
    data = file.read().strip()

KEY = "XMAS"

key_count = 0


def get_length_of_matrix(matrix):
    length = 0
    for row in matrix:
        for _ in row:
            length += 1
    return length


def check_matrix_boundry(x, y, x_offset, y_offset, matrix):
    if (
        y + y_offset < 0
        or x + x_offset < 0
        or y + y_offset >= len(matrix)
        or x + x_offset >= len(matrix[y + y_offset])
    ):
        return True
    else:
        return False


def iterate_matrix_direction(x, y, x_offset, y_offset, matrix, key_step, key):
    global key_count
    print(matrix[y + y_offset][x + x_offset], x_offset, y_offset)
    for step in range(len(key) - 2):
        # print(f"STEP: {step+2}")
        if check_matrix_boundry(
            x, y, x_offset * (step + 2), y_offset * (step + 2), matrix
        ):
            break
        elif (
            matrix[y + y_offset * (step + 2)][x + x_offset * (step + 2)]
            == key[key_step + step + 1]
        ):
            print(
                matrix[y + y_offset * (step + 2)][x + x_offset * (step + 2)],
                x_offset * 2,
                y_offset * 2,
            )
            if matrix[y + y_offset * (step + 2)][x + x_offset * (step + 2)] == key[-1]:
                key_count += 1
                print("Counted new key")
        else:
            break


def search_from_root(x, y, matrix, key):
    key_step = 0
    if matrix[y][x] == key[key_step]:
        key_step += 1
        x_offset = -1
        y_offset = -1
        # while matrix[y + y_offset][x + x_offset] != key[key_step]:
        while True:
            print(matrix[y][x], x, y, "   offset: ", x_offset, y_offset)
            # print("HERE")
            if check_matrix_boundry(x, y, x_offset, y_offset, matrix):
                # print("Out of bounds!")
                if y_offset == 1 and x_offset == 1:
                    break
                elif x_offset == 1:
                    x_offset = -1
                    y_offset += 1
                    continue
                x_offset += 1
                continue
            # print(x_offset, y_offset)
            if matrix[y + y_offset][x + x_offset] == key[key_step]:
                iterate_matrix_direction(
                    x, y, x_offset, y_offset, matrix, key_step, key
                )
            if y_offset == 1 and x_offset == 1:
                break
            elif x_offset == 1:
                x_offset = -1
                y_offset += 1
                continue
            x_offset += 1

        # print(matrix[y + y_offset][x + x_offset], x + x_offset, y + y_offset)


print(data)

data = data.split("\n")

for row in range(len(data)):
    # print("\n")
    data[row] = list(data[row])
    # print(data[row])
    # for char in data[row]:
    #     print(f" {char} ", end="")

for y in range(len(data)):
    for x in range(len(data[y])):
        # print(x, y, data[y][x])
        search_from_root(x, y, data, key=KEY)

print(key_count)

# for char in range(getLengthOfMatrix(data)):
#     print(data[char][char])

# print("\n", data[-1][-1])
