def find_user_by_username(database, user_name):
    return database.Users.find_one({'user_name': user_name})
