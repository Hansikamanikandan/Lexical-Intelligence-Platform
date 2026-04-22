n = input("Enter the string: ")
result = ""
i = 0

while i < len(n):
    ch = n[i]
    num = int(n[i + 1])
    result += ch * num
    i += 2

print(result)
