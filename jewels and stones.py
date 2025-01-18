def numJewelsInStones(jewels: str, stones: str) -> int:
    ans = 0
    for i in stones:
        if i in jewels:
            ans += 1
    return ans

# Get input from the user
jewels = input("Enter the jewels (characters representing jewels): ")
stones = input("Enter the stones (characters representing stones): ")

# Calculate and display the result
result = numJewelsInStones(jewels, stones)
print("Number of jewels in stones:", result)
