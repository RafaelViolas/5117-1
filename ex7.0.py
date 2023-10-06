my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

print("Original List: ", my_list)
ctr = {}
for num in my_list:
    ctr[num] = 0
for num in my_list:
    ctr[num] += 1

print("Frequency of the elements in the List: ", ctr)
