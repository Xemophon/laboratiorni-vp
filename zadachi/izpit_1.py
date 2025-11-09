lst_10 = input("Enter 10 numebrs: ").split()
lst_10_odd = []

#a podtochka
for i in range(len(lst_10)):
    if int(lst_10[i]) % 2 == 0:
        pass
    elif int(lst_10[i]) % 2 == 1:
        lst_10_odd.append(lst_10[i])
print(f"The odd numbers are: {lst_10_odd}")

#b podtochka
sum = 0
for j in range(len(lst_10)):
    sum += int(lst_10[j])
print(f"Average is: {sum/len(lst_10)}")

#v i g podtochka
lst_5 = []
lst_10.sort(reverse=True)
for k in range(len(lst_10)):
    if int(lst_10[k]) % 2 == 0:
        lst_5.append(lst_10[k])
        if len(lst_5) == 5:
            break
        else:
            pass
print(f"The biggest even numbers are: {lst_5}")

#d podtochka
lst_5_1 = []
for h in range(0, len(lst_5), 2):
    lst_5_1.append(lst_5[h])
for o in range(len(lst_5_1)):
    lst_5.remove(lst_5_1[o])
print(f"The left numbers are: {lst_5}")