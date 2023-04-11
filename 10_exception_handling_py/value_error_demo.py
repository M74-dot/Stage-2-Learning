while True:
    try:
        num = int(input("Please enter a positive integer: "))
        if num <= 0:
            raise ValueError("The number must be positive")
        break
    except ValueError as e:
        print("Invalid input:", e)

print("The number you entered is:", num)
