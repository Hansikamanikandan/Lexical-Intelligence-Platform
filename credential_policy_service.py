p = input("Enter password: ")

if not (8 <= len(p) <= 15):
    print("Password must be between 8 and 15 characters")

elif " " in p:
    print("Password cannot contain space")

elif not any(i.isdigit() for i in p):
    print("Password must contain digit")

elif not any(i.islower() for i in p):
    print("Password must contain lowercase letter")

elif not any(i.isupper() for i in p):
    print("Password must contain uppercase letter")

elif not any(i in "@#$%^&*" for i in p):
    print("Password must contain special character")

else:
    print("Password is valid")
