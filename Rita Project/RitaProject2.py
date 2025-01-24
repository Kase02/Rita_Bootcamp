import hashlib

#User data storage
class User:
    def __init__(self, username, password):
        self.users = username
        self.tasks = password


class TaskManagementSystem:
    def __init__(self):
        self.user = {}


    def hash_password(self):
        print("\n--- Register ---")
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
    else:
        return hashlib.sha256(password.encode()).hexdigest()

# Function to register a user
    def register_user(self):
        print("\n--- Register ---")
        username = input("What is your name: ")
        if username in self.user:
            print("Username already exists.")
            return

        self.users[username] = hash_password(self)
        self.tasks[username] = []
        return "User registered successfully."

# Function to log in a user
    def login_user(self):
        print("\n--- Login ---")
        username = input("Enter your username: ")
        if username not in self.users:
            return"Username not found."
        print("\n--- Login ---")
        password = input("Enter your password: ")
        if self.users[username] != hash_password():
            return"Incorrect password."
        else:
            print(f"\nWelcome back, {username}!")
            return"Login successful."


    def add_task(self, username, task):
        if username not in self.users:
            print("Username not found! Please register first.")
            return
        self.tasks[username].append(task)
        return"Task added successfully."


    def view_tasks(self, username):
        if username not in self.tasks:
            return"User not found."



# Dashboard after successful login
def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Logout")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == "1":
            view_profile(username)
        elif choice == "2":
            change_password(username)
        elif choice == "3":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")

# View Profile
def view_profile(username):
    print(f"\n--- Profile ---")
    print(f"Username: {username}")
    print("Welcome to your dashboard!")

# Change Password
def change_password(self, username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    if self.users[username] != hash_password():
        print("Incorrect current password! Password not changed.")
        return
    else:
        new_password = input("Enter a new password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
    else:
        return hashlib.sha256(new_password.encode()).hexdigest()

    self.users[username] = hash_password()
    print("Password updated successfully!")

# Run the main program loop
while True:
    print("\n--- User Dashboard Management System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        register_user(self)
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")