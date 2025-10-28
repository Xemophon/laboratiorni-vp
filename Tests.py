print("Test how matrixes and PY co-work")
matrix_elements = (input("Enter numbers 4 with spaces: ").split())
size = float(len(matrix_elements) ** 0.5)
if round(size) != size:
    print("Error")
else:
    size = int(size)
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(float(matrix_elements[i * size + j]))
        matrix.append(row)
for row in matrix:
    print(row)