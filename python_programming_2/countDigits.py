#count the number of digits in a number

def countDigits(n):
    count=0
    while( n % 10 !=0):
        count+=1
        n//=10
    return count

n = int(input("enter a number:"))
print(countDigits(n))