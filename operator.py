num1=int(input("enter the first number"))
num2=int(input("enter the second number"))


print("choose operator")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choose = int(input(" select number (1-4):"))
if choose == 1:
    print("ans:",num1+num2)
elif choose ==2:
    print("ans:",num1-num2)
elif choose == 3 :
    print("ans:",num1*num2)
elif choose==4:
    if num2 != 0:
        print("ans:",num1/num2)
    else:
        print("error! 0 is not divisible")
else:
    print("choose 1-4")
