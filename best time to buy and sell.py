def maxProfit(prices):
    minval = prices[0]
    ans = 0
    for i in range(1, len(prices)):
        ans = max(ans, (prices[i] - minval))
        minval = min(minval, prices[i])
    return ans

# Get input from the user
user_input = input("Enter the stock prices separated by spaces: ").split()
prices = [int(price) for price in user_input]

# Calculate and display the maximum profit
result = maxProfit(prices)
print("Maximum profit:", result)
