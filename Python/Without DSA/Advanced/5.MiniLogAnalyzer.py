# check: user1, user2, user1, user3, user2, user1

log_details = input("Enter log details: ").split(", ")

user_dict = {}

for user in log_details:
    user_dict[user] = user_dict.get(user, 0) + 1

print(user_dict)