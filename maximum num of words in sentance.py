def mostWordsFound(sentences):
    ans = 0
    for i in range(len(sentences)):
        s = sentences[i]
        temp = 1
        for j in range(len(s)):
            if s[j] == " ":
                temp += 1
        ans = max(ans, temp)
    return ans

# Get input from the user
user_input = input("Enter sentences separated by a semicolon (;): ").split(";")

# Calculate and display the result
result = mostWordsFound(user_input)
print("The maximum number of words in a single sentence is:", result)
