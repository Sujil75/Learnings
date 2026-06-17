numbers = [1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8, 0]

new_list = []

for val in numbers:
    if val not in new_list:
        new_list.append(val)

print(new_list)