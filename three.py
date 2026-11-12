one_list = []
for x in range(0,101):
    one_list.append(x ** 2)
two_list = [x**2 for x in range(0,101)]
print(one_list == two_list)
