list1 =[1,2,3,4]
list2 =[5,6,7,8]

list3 =[1,2,3]
list4 =[3,4]

def checkRepeating(list1,list2):
    combined = list1 + list2
    if(len(combined)==len(set(combined))):
            print("no repeating elements")
    else:
            print("repeating elements present")

checkRepeating(list1,list2)
checkRepeating(list4,list3)