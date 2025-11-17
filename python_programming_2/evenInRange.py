# Write a function that takes two integers
# a and b and print sall even numbers
# between them (inclusive)

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def evenNumbers(a,b):
    for i in range(a,b+1):
        if(even(i)):
            print(i)


a,b= map(int,input("enter two numbers:").split())
print(evenNumbers(a,b))