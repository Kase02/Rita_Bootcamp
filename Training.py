import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class TaskManagementSystem:
    def __init__(self):
        self.users = {}  # Stores users with hashed passwords
        self.tasks = {}  # Stores tasks for each user

def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self):
        print("\n--- Register ---")
        username = input("What is your name: ")
        if username in self.users:
            print("Username already exists.")
            return

        password = input("Enter a password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters long!")
            return

        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        self.tasks[username] = []
        print("User registered successfully.")

    def login_user(self):
        print("\n--- Login ---")
        username = input("Enter your username: ")
        if username not in self.users:
            return "Username not found."

        password = input("Enter your password: ")
        hashed_password = self.hash_password(password)
        if self.users[username] != hashed_password:
            return "Incorrect password."
        else:
            print(f"\nWelcome back, {username}!")
            return "Login successful."

    def add_task(self, username, task):
        if username not in self.users:
            print("Username not found! Please register first.")
            return
        self.tasks[username].append(task)
        print("Task added successfully.")

    def view_tasks(self, username):
        if username not in self.tasks:
            return "User not found."
        return self.tasks[username]

    def change_password(self, username):
        print("\n--- Change Password ---")
        old_password = input("Enter your current password: ")
        if self.users[username] != self.hash_password(old_password):
            print("Incorrect current password! Password not changed.")
            return

        new_password = input("Enter a new password: ")
        if len(new_password) < 6:
            print("Password must be at least 6 characters long!")
            return

        self.users[username] = self.hash_password(new_password)
        print("Password updated successfully!")

    def user_dashboard(self, username):
        while True:
            print(f"\n--- Dashboard: {username} ---")
            print("1. View Profile")
            print("2. Change Password")
            print("3. Logout")
            choice = input("Enter your choice (1, 2, or 3): ")
            if choice == "1":
                self.view_profile(username)
            elif choice == "2":
                self.change_password(username)
            elif choice == "3":
                print(f"Goodbye, {username}!")
                break
            else:
                print("Invalid choice! Please try again.")

    def view_profile(self, username):
        print(f"\n--- Profile ---")
        print(f"Username: {username}")
        print("Welcome to your dashboard!")

# Run the main program loop
if __name__ == "__main__":
    tms = TaskManagementSystem()
    while True:
        print("\n--- User Dashboard Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == "1":
            tms.register_user()
        elif choice == "2":
            result = tms.login_user()
            if result == "Login successful.":
                tms.user_dashboard(input("Enter your username again: "))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")




