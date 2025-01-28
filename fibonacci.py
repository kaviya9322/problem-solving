def fibonacci_for(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b    # Update 'a' and 'b' for the next number in the sequence

fibonacci_for(10)
