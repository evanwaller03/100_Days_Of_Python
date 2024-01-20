# PascalCase, camelCase, snake_case
# A CONSTRUCTOR is a part of the blueprint initialization
# Create the constructor with the def __init__ function


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def change_followers(self, user, ):
        self.following += 1
        user.followers =+ 1


users = []

evan = User(1, "Waller")
lindsay = User(2, "Instructor Peters")

print(evan.following)
print(lindsay.followers)

evan.change_followers(lindsay)

print(evan.following)
print(lindsay.followers)