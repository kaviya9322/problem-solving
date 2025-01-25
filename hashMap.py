li = [1,2,6,5,7,0,7,8,4,2,2,2,2,4,4,4,4]
n= len(li)
dici = {}
for i in range(n):
    val = li[i]
    if val not in dici:
        dici[val] = 1
    else:
        temp = dici[val]
        dici[val] = temp +1
print(dici)
