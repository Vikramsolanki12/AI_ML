def DivisibleBy3and5(a,b):
    for i in range(a,b+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

a,b = map(int,input("enter a range of Numbers:").split())
print("Number that are divisible by 3 and 5:")
print(DivisibleBy3and5(a,b))