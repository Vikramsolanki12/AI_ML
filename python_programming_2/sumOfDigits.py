def sumOfDigits(n):
    sum = 0
    while( n % 10 != 0):
        sum = sum + (n%10)
        n = n // 10
    return sum

n = int(input("enter a number:"))
print(sumOfDigits(n))