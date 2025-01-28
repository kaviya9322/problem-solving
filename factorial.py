num = int(input("Enter a number: ")) 
factorial = 1                                    # Initialize factorial as 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i                               # Multiply factorial by the current value of i
    print(f"The factorial of {num} is {factorial}.")
