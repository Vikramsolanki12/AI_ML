# Write a program that takes salary as input. Using conditional statements,
# calculate final tax rate based on the rules:
# If salary<30,000 → 5%
# •If salary is 30,000–70,000 → 15%
# •If salary>70,000 → 25%

salary = int(input("enter salary:"))

if(salary > 0 and salary <30000):
    print("final tax rate is: 5%")
elif(salary >30000 and salary <70000):
    print("final tax rate is: 15%")
elif(salary>70000):
    print("final tax rate is: 25%")
else:
    print("invalid salary")