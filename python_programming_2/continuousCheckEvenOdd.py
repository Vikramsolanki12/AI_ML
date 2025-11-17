while True:
    user_input = input("Enter a number (or type Quit to exit): ")

    if user_input.lower() == "quit":
        print("Program ended.")
        break

    num = float(user_input)
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
