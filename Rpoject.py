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

def method_of_Kramer():
    coef_matrix_elements = input("Input with spaces squarble number of digits which are equation coefficients: ").split()
    size = float(len(coef_matrix_elements)) ** 0.5
    if round(size) != size:
        print("Not calculable by Kramer Formulas")
    elif size > 3:
        print("Too complicated for this calculator")
    else:
        size = int(size)
        coef_matrix = []
        for i in range(size):
            coef_row = []
            for j in range(size):
                coef_row.append(float(coef_matrix_elements[i*size + j]))
            coef_matrix.append(coef_row)
        res_matrix = []
        res_matrix_elements = input(f"Input {size} number of right-side numbers: ").split()
        for i in range(size):
            res_row = []
            res_row.append(float(res_matrix_elements[i]))
            res_matrix.append(res_row)
        if size == 2:
            det_coef = coef_matrix[0][0] * coef_matrix[1][1] - coef_matrix[0][1] * coef_matrix[1][0]
            delta_1 = res_matrix[0][0] * coef_matrix[1][1] - res_matrix[1][0] * coef_matrix[1][0]
            delta_2 = coef_matrix[0][0] * res_matrix[1][0] - coef_matrix[1][0] * res_matrix[0][0]
            print("First root is: " + str(round(delta_1 / det_coef, 2)))
            print("Second root is: " + str(round(delta_2 / det_coef, 2)))
        elif size == 3:
            det_coef = (coef_matrix[0][0] * (coef_matrix[1][1] * coef_matrix[2][2] - coef_matrix[1][2] * coef_matrix[2][1]) -
                         coef_matrix[0][1] * (coef_matrix[1][0] * coef_matrix[2][2] - coef_matrix[1][2] * coef_matrix[2][0]) +
                         coef_matrix[0][2] * (coef_matrix[1][0] * coef_matrix[2][1] - coef_matrix[1][1] * coef_matrix[2][0]))
            delta_1 = (res_matrix[0][0] * (coef_matrix[1][1] * coef_matrix[2][2] - coef_matrix[1][2] * coef_matrix[2][1]) -
                       coef_matrix[0][1] * (res_matrix[1][0] * coef_matrix[2][2] - coef_matrix[1][2] * res_matrix[2][0]) +
                       coef_matrix[0][2] * (res_matrix[1][0] * coef_matrix[2][1] - coef_matrix[1][1] * res_matrix[2][0]))
            delta_2 = (coef_matrix[0][0] * (res_matrix[1][0] * coef_matrix[2][2] - coef_matrix[1][2] * res_matrix[2][0]) -
                       res_matrix[0][0] * (coef_matrix[1][0] * coef_matrix[2][2] - coef_matrix[1][2] * coef_matrix[2][0]) +
                       coef_matrix[0][2] * (coef_matrix[1][0] * res_matrix[2][0] - res_matrix[1][0] * coef_matrix[2][0]))
            delta_3 = (coef_matrix[0][0] * (coef_matrix[1][1] * res_matrix[2][0] - res_matrix[1][0] * coef_matrix[2][1]) -
                       coef_matrix[0][1] * (coef_matrix[1][0] * res_matrix[2][0] - res_matrix[1][0] * coef_matrix[2][0]) +
                       res_matrix[0][0] * (coef_matrix[1][0] * coef_matrix[2][1] - coef_matrix[1][1] * coef_matrix[2][0]))
            print("First root is: " + str(round(delta_1 / det_coef, 2)))
            print("Second root is: " + str(round(delta_2 / det_coef, 2)))
            print("Third root is: " + str(round(delta_3 / det_coef, 2)))
        else:
            print("Uncalcualable by the current method")

print("Starting the calc...")
print("1.Reverse a Matrix, 2.Determinant, 3.Kramer's Method, 0 to exit")

        
x = float(input("Enter a number (0, 1, 2 or 3): "))
if x == 1:
   reverse_matrix()
elif x == 2:
    determinant()
elif x == 3:
    method_of_Kramer()
elif x == 0:
    print("Exiting the program.")
elif x not in {0,1,2,3}:
    while x not in {0,1,2,3}:
        x = float(input("Invalid input. Enter a number (0, 1, 2 or 3): "))
    if x == 1:
        reverse_matrix()
    elif x == 2:
        determinant()
    elif x == 3:
        method_of_Kramer()
    elif x == 0:
        print("Exiting the program.")