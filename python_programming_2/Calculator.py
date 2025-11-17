def Calculator(a,b,operator):
    if(operator == "+"):
        return a + b
    elif(operator == "-"):
        return a - b
    elif(operator == "*"):
        return a * b
    elif(operator == "/"):
        return a / b
    else:
        print("Operator not recognized")

a,b = map(int,input("enter a,b:").split())
operator = input("enter operator:")

print(Calculator(a,b,operator))