s = input("Enter the sentence: ")
words = s.split()

for word in words:
    if len(word) > 5:
        print(word)
