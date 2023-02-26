from hashlib import blake2b

# the 'database' of users
users = []

class User:
    def __init__(self, name: str, password: str, email: str):
        self.name = name
        self.password = blake2b(password.encode('UTF-8')).hexdigest()
        self.email = email
        self.plan = "basic"
        self.reset_code = ""

    def __repr__(self):
        return f"NAME: {self.name}, EMAIL: {self.email}, PASSWD: {self.password}"
    
    def reset_password(self, code: str, new_password: str):
        if code != self.reset_code:
            raise Exception("Invalid password reset code.")
        self.password = blake2b(new_password.encode('UTF-8')).hexdigest()

def create_user(name: str, email: str, password: str):
    user = User(name, password, email)
    users.append(user)
    return user

def find_user(email: str):
    for user in users:
        if user.email == email:
            return user
    raise Exception("User with email address {email} not found.")