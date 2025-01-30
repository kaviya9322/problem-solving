# A pair (i, j) is called good if nums[i] == nums[j] and i < j
nums = [1,2,3,1,1,3]
n= len(nums)
ans = 0 
for i in range (n):       #using a double for loop to print the pairs
  for j in range(i+1,n):
    if nums[i] == nums[j] and i < j:
      ans = ans + 1
      print(ans)        # o(n**2) time complexity
