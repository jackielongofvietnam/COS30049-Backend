def find_user_by_username(database, username):
    return database.Users.find_one({'username': username})
