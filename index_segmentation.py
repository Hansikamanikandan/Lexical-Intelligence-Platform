s = input("Enter the string: ")

print("Characters in odd position:")
for i in range(len(s)):
    if i % 2 == 1:
        print(s[i])

print("Characters in even position:")
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i])
