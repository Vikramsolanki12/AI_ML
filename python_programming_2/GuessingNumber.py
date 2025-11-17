x = 37

while True:
    guess = int(input("enter number:"))

    if(guess == x):
        print("correct!")
        break

    if(guess < x):
        print("Too low")
    else:
        print("Too high")