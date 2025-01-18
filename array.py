from typing import List

def finalValueAfterOperations(operations: List[str]) -> int:
    X = 0
    for i in operations:
        if i == "--X" or i == "X--":
            X -= 1
        else:
            X += 1
    return X

# Get input from the user
user_input = input("Enter operations separated by spaces (e.g., --X X++ X--): ").split()
result = finalValueAfterOperations(user_input)
print("Final value of X:", result)
