def sum_of_digits(n):
total = 0
n = abs(n)  # Handle negative numbers
while n > 0:
  total += n % 10  # Get the last digit
n //= 10  # Remove the last digit
return total

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
