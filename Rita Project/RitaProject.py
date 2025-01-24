import hashlib

#User data storage
class User:
    def __init__(self, username, password):
        self.users = username
        self.tasks = password

class TaskManagementSystem:
    def __init__(self):
        self.user = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(self, username, password):
    if username in self.users:
        return "Username already exists."
    self.users[username] = hash_password(password)
    self.tasks[username] = []
    return "User registered successfully."

def login_user(self, username, password):
    if username not in self.users:
        return"Username not found."
    if self.users[username] != hash_password(password):
        return"Incorrect password."
    return"Login successful."

def add_task(self, username, task):
    if username not in self.users:
        return "User not found."
    self.tasks[username].append(task)
    return"Task added successfully."

def view_tasks(self, username):
    if username not in self.tasks:
        return"User not found."
    return self.tasks[username]

if __name__ == "__main__":
    system = TaskManagementSystem()
    