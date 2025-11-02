data_matrix = []
data_elements = input("Enter lenght of section and its max velocity (ex. 2 20): ").split()
size = float(len(data_elements) / 2)
if size * 2 % 2 != 0:
    print("Invalid")
else:
    size = int(size)
    for i in range(size):
        row = []
        for j in range(2):
            row.append(int(data_elements[i*2 + j]))
        data_matrix.append(row)
    delta_t = 0
    delta_s = 0
    for k in range(size):
        time = 0
        time = data_matrix[k][0] / data_matrix[k][1]
        delta_t += time
        delta_s += data_matrix[k][0]
    avg_v = round(delta_s / delta_t)
    print("Average velocity should be " + str(avg_v) + " km/h")