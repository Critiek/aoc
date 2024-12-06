test = input("test? y/n\n>")

match test:
    case "y":
        path = "test_input.txt"
    case "n":
        path = "input.txt"

with open(path, "r") as file:
    data = file.read().strip()


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


TL_offset = {"x": -1, "y": -1}
TR_offset = {"x": +1, "y": -1}
BL_offset = {"x": -1, "y": +1}
BR_offset = {"x": +1, "y": +1}

M_and_S = ["M", "S"]

x_mas_counter = 0


def search_from_root(x, y, matrix):
    global x_mas_counter
    tr_bl = False
    tl_br = False
    if matrix[y][x] == "A":
        if not check_matrix_boundry(
            x, y, TL_offset["x"], TL_offset["y"], matrix
        ) and not check_matrix_boundry(x, y, BR_offset["x"], BR_offset["y"], matrix):
            tl = matrix[y + TL_offset["y"]][x + TL_offset["x"]]
            br = matrix[y + BR_offset["y"]][x + BR_offset["x"]]
            if tl in M_and_S and (br in M_and_S and br != tl):
                print("TL_BR true")
                tl_br = True
            else:
                pass

        if not check_matrix_boundry(
            x, y, TR_offset["x"], TR_offset["y"], matrix
        ) and not check_matrix_boundry(x, y, BL_offset["x"], BL_offset["y"], matrix):
            tr = matrix[y + TR_offset["y"]][x + TR_offset["x"]]
            bl = matrix[y + BL_offset["y"]][x + BL_offset["x"]]
            if tr in M_and_S and (bl in M_and_S and bl != tr):
                print("TR_BL true")
                tr_bl = True
            else:
                pass

        if tr_bl and tl_br:
            x_mas_counter += 1


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
        search_from_root(x, y, data)

print(x_mas_counter)

# for char in range(getLengthOfMatrix(data)):
#     print(data[char][char])

# print("\n", data[-1][-1])
