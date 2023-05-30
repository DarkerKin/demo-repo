# this code is to find the minimum value in the list

list_1 = [1, 2, 3, 4, 13, -2342]
minimum = list_1[0]
for i in list_1:
    if minimum > i:
        minimum = i
print("minimum in the list is", minimum)

# this code is to program selection sort in python

list_2 = [23, 4, -2, 0, 54, 405, -21]
for i in range(len(list_2)):
    minimum = i
    value = list_2[i]
    for s in range(i+1, len(list_2)):
        if list_2[s] < list_2[minimum]:
            minimum = s
    list_2[i] = list_2[minimum]
    list_2[minimum] = value
print(list_2)

# This code is bubble sort

list_3 = [343, -21, 4, 0, 459, -123]
for i in range(len(list_3)):
    for s in range(len(list_3)-1):
        value = list_3[s]
        if list_3[s] > list_3[s+1]:
            list_3[s] = list_3[s+1]
            list_3[s + 1] = value
print(list_3)
# trail x

