#The majority element is the element that appears more than ⌊n / 2⌋ times
num = [2,2,1,1,1,2,2]
dici={}
for key in num:     # using a hashmap to decline a key values
    if key in dici:
        dici[key]= dici[key]+1  
    else:
        dici[key] = 1
ans = -1
temp = len(num)//2      # storing the n//2 in temp
for key in dici:        # looping the key values 
    val = dici[key]
    if val > temp:       # checking the condition 
        ans = key 
print(ans)               # out put 2
    
