x = 0

def reverse_matrix():
    matrix_elements = (input("Enter numbers with spaces: ").split())
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
        if size == 2:
            delta_det = int(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
            if delta_det == 0:
                print("The matrix is not invertible.")
                return
            elif delta_det != 0:
                inv = [[matrix[1][1] / delta_det, -matrix[0][1] / delta_det],
                        [-matrix[1][0] / delta_det, matrix[0][0] / delta_det]]
            print("The inverse of the 2x2 matrix is:")
            for row in inv:
                print(row)
        elif size == 3:
            delta_det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                         matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                         matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
            if delta_det == 0:
                print("The matrix is not invertible.")
                return
            elif delta_det != 0:
                inv = [[(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) / delta_det,
                        (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) / delta_det,
                        (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) / delta_det],
                       [(matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) / delta_det,
                        (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) / delta_det,
                        (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) / delta_det],
                       [(matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) / delta_det,
                        (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) / delta_det,
                        (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) / delta_det]]
                print("The inverse of the 3x3 matrix is:")
                for row in inv:
                    print(row)
        else:
            print("Not calculable now")

def determinant():
    matrix_elements = (input("Enter numbers with spaces: ").split())
    size = float(len(matrix_elements) ** 0.5)
    if round(size) != size:
        print("Not a square matrix")
    else:
        size = int(size)
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(float(matrix_elements[i * size + j]))
            matrix.append(row)
        if size == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            if det == 0:
                print("The determinant of the 2x2 matrix is: 0")
            else:
                print(f"The determinant of the 2x2 matrix is: {det}")
        elif size == 3:
            det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                    matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                    matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
            if det == 0:
                print("The determinant of the 3x3 matrix is: 0")
            else:
                print(f"The determinant of the 3x3 matrix is: {det}")
        else:
            print("Not calculable now")
            return None

print("Starting the calc...")
print("1.Reverse a Matrix, 2.Determinant, 0 to exit")

        
x = float(input("Enter a number (0, 1, or 2): "))
if x == 1:
   reverse_matrix()
elif x == 2:
    determinant()
elif x == 0:
    print("Exiting the program.")
elif x not in {0,1,2}:
    while x not in {0,1,2}:
        x = float(input("Invalid input. Enter a number (0, 1, or 2): "))
    if x == 1:
        size = int(input("Enter the size of the matrix (2 or 3): "))
        reverse_matrix()
    elif x == 2:
        size = int(input("Enter the size of the matrix (2 or 3): "))
        determinant()
    elif x == 0:
        print("Exiting the program.")