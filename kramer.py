print("Kramer equation calculator")
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
        print("First root is: " + str(delta_1 / det_coef))
        print("Second root is: " + str(delta_2 / det_coef))
    #TODO 3x3 case
