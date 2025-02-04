# greatest among three numbers
a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input ("enter the third number"))
if a>b and a>c:
    print ("a is greater")    # chech all posibilities if a is greater
elif b>c and b>a:
    print("b is greater")     # chech all posibilities if b is greater
else:
    print("c is greater")     # the two conditions are not satisfied then the c is greater
