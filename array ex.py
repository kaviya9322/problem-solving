This program calculates the final value of a variable X based on a list of operations provided by the user. The operations can be --X, X--, ++X, or X++, where:

--X or X-- decreases X by 1.
++X or X++ increases X by 1.
1.Start with X = 0, which is the initial value of the variable.
2.The user provides a list of operations as input.
3.The program loops through each operation in the list:
4.If the operation is --X or X--, it decreases the value of X by 1 using X -= 1.
5.Otherwise, for ++X or X++, it increases the value of X by 1 using X += 1.
6.After processing all operations, the program returns the final value of X.
