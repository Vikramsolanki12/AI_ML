list1 = [2,6,9,12,2,5,6,8,9,23,14,12]

duplicates = set()
for item in list1:
   seen = set()

   for item in list1:
       if item in seen:
           duplicates.add(item)
       else:
           seen.add(item)

print(duplicates)