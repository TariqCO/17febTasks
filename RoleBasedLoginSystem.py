# 9. Role-Based Login System (H,D,S,A)
# Ask the user for username and role (admin/user).
# 
# Keep asking until valid credentials.
# If role is admin → show admin menu.
# If role is user → show user menu.
# while loop → login validation
# if-elif-else → role handling
# Nested while → menu system



admin1="tariq001"
admin2="rehbar98"
admin3="jabbar1985"

user1="alikhan_89"
user2="bakhtawar6090"

print("\n =========== Role-Based Login System =========== \n")

while True:
    role = int(input("Enter the role: (1. Admin 2. User) -->| "))
    username = input("Enter the username: ")

    if (role == 1):
        if (username == admin1) or (username == admin2) or (username == admin3):
            print("\n ===== Admin =====")
            print(f"\nWelcome {username}, \nTo the Admin dashboard")
            
            break
        else:
            print("\n--- Invalid Details ---")
            print(f"There is no Admin registered with this username {username}\n")
            continue
    elif(role == 2):
        if (username == user1) or (username == user2):   
            print("\n ===== User =====")
            print(f"\nWelcome {username}, \nTo our website.")
            break
        else:
            print("\n--- Invalid Details ---")
            print(f"There is no User registered with this username {username}\n")
            continue
    else:
        print("Invalid Input")
        
    
    
    
    
    