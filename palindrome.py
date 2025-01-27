s = input()
ans = " "
for i in range(len(s)-1,-1,-1): #reversing a input using -1,-1,-1
  ans = ans + s[i]  
if ans == s:  #checking ans equa to s
  print("yes its a palindrome")
else:
  print("No its not a palindrome")   
  