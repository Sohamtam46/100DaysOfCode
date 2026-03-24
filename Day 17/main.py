

class User:
    # called everytime this class is called
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("001","SohamT")

# print(user_1.username)

user_2 = User("002","N!")
# user_2.user_id = "003"
# user_2.username = "N!"

# print(user_2.user_id)
print(user_2.username,user_2.followers)

user_1.follow(user_2)

print(user_2.username,user_2.followers)
# notes
# PascalCase -> class name
# camelCase -> not used
# snake_case -> everything else


