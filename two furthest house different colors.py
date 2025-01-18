def maximumDifference(nums):
    n = len(nums)
    ans = -1
    low = nums[0]
    for j in range(1, n):
        if low < nums[j]:
            temp = nums[j] - low
            ans = max(ans, temp)
        low = min(low, nums[j])
    return ans

# Get input from the user
user_input = input("Enter the list of numbers separated by spaces: ").split()
nums = [int(num) for num in user_input]

# Calculate and display the maximum difference
result = maximumDifference(nums)
print("Maximum difference:", result)
