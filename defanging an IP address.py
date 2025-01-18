def defangIPaddr(address: str) -> str:
    ans = ""
    for i in address:
        if i == ".":
            ans += "[.]"
        else:
            ans += i
    return ans

# Get input from the user
user_input = input("Enter an IP address: ")

# Convert the IP address to its defanged version
result = defangIPaddr(user_input)
print("Defanged IP address:", result)
