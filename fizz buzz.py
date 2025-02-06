# fizz buzz 
n = int(input("enter a number"))
ans =[]
for i in range(1,n+1):
    if i % 3==0 and i % 5==0:       #chech the number is divisible by 3 and 5
        ans.append("FIZZBUZZ")
    elif i % 3 ==0:
        ans.append("FIZZ")
    elif i % 5==0:
        ans.append("BUZZ")     
    else:
        ans.append(i)       ##if no condition is satisfied then the else part will run 
 print(ans)                     # the same number print in arr
     
