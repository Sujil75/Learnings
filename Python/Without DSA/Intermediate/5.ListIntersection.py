list1 = [1, 2, 3, 4, 5]
list2 = [2, 5, 7, 1, 8]

new_list = []

for val in list1:
    if val in list2:
        new_list.append(val)

print(sorted(new_list))