# Password Strength Checker
# 
# Ask the user to enter a password until it is strong.  (A,S,A,K,R)
# 
# Minimum 8 characters
# At least one digit
# At least one special character
# while loop → repeat until strong
# Nested if → check each condition
# elif → medium
# else → weak


while True:
    password = input("Enter your password: ")
    specialChar = ["#","!","@","$","%","^","&","*"]

    for i in range(len(specialChar)):
        for j in range(len(password)):
            if (specialChar[i] == password[j]):
                char = True
                break

    
    if len(password) < 8:
        print("Password must be atleast 8 characters long.")
    else:
        if char == True:
            print("Strong password")
            break
        else:
            print("Weak password")
            continue
            
            
            
            
            
            
            
            
            
            
            