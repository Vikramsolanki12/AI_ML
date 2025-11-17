#print number of digit and digits in a number

def NumberOfDigits(n):
    count = 0
    while(n % 10 != 0):
        count +=1
        print("digit is:", n%10)
        n = n // 10

    print("number of digits is:", count)

n = int(input("enter a number:"))
NumberOfDigits(n)