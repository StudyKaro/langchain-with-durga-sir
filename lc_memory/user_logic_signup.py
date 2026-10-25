import json
import os

USERS_FILE = "users.json"

#get users list
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}
    
#save users
def save_user(users):
    with open(USERS_FILE,"w") as file:
        json.dump(users,file, indent=2)

#sign up function
def signup(users):
    print("\n==== Sign Up ======")
    name = input("Enter name: ").strip()
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ")
    
    if not name or not username or not password :
        print("\n All field are required.")
        return
    
    if not username.replace("_","").isalnum() :
        print("\n User name should contains only alphabets, number and underscore.")
        return
    if username in users:
        print("\n Username already exist, try other name.")
        return
    # add in users
    users[username] = {
            "name": name,
            "password": password
        }  
    save_user(users)
    print(f"Hello! {users[username]['name']}, your account has beed created successfully.")

# login 
def login(users):
    print("=== Login ===")
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()
    if not username or not password:
        print("Username and Password required.")
        return 
    if username not in users:
        print("Invalid username.")
        return None
    if users[username]["password"] == password:
        print(f"Hello! {users[username]['name']}, Welcome to persistent chat history.")
        return username
    
    print("Invalid username and password.")
    return


users = load_users()
# print("users detail : ", users)
current_user = None

print("=====Multi User Login System======\n")
while True:
    if current_user is None:
        print("\n=====Dashboard======")
        print("""
            \n 1. Sign Up
            \n 2. Login
            \n 3. Exit
            """)
        option = input("Choose the Option \n")
        if option == "1":
            signup(users)
        
        elif option == "2":
            login(users)
            
        elif option == "3":
            print("\n You have quit.")
            break
        else:
            print("Invalid optioin. Choose from dashboard.")

        