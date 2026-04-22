s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
