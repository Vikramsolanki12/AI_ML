tuple1 = (3,4,6,12,90,67,45,34,76,23,14,37)
evenList = []
oddList = []
for item in tuple1:
    if item % 2 == 0:
        evenList.append(item)
    else:
        oddList.append(item)

print(tuple(evenList))
print(tuple(oddList))
