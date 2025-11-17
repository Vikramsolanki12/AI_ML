def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a,b,c = map(int,input("enter three numbers:").split())
print(largest(a,b,c))