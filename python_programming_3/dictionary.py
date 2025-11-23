students = {
    "name": ["vikram","ashish","anaya"],
    "marks":[89,56,90]
}
print("Select an option (A,B,C or D:")
print("A:Add a student")
print("B:Update marks")
print("C:search for a student")
print("D:display all students and marks")
userInput = input()

if userInput == "A":
    name = input("Enter student name:")
    students["name"].append(name)
    students["marks"].append(None)
    print("student added!")
elif userInput == "B":
    name = input("enter student name:")
    if name in students["name"]:
        index = students["name"].index(name)
        marks= input("enter marks:")
        students["marks"][index]=marks
        print("marks added!")
    else:
        print("student not found")
elif userInput == "C":
    name = input("enter student name:")
    if name in students["name"]:
        index = students["name"].index(name)
        print("Marks:",students["marks"][index])
    else:
        print("student not found")
elif userInput == "D":
    print("\nStudent List:")
    for i in range(len(students["name"])):
        print(students["name"][i],"-",students["marks"][i])
else:
    print("Invalid input")