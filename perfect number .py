def is_perfect_number(num):
  if num <= 1:
    return False
    total = 1  # 1 is always a divisor
    for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        total += i
        if i != num // i:  # Avoid adding the square root twice
          total += num // i
return total == num

num = int(input("Enter a number: "))
print(is_perfect_number(num))
