class user:
    def __init__(self, username):
        self.username = username
    def login(self):
        print(f"{self.username} logged in")

class Admin(user):
    def delete_user(self):
     print("Admin deleted the user")
a = Admin("lbc")
print(a.username)
a.delete_user()


