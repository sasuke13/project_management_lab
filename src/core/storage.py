AUTH_USERS = {}


async def add_user_to_session(username: str):
    global AUTH_USERS
    AUTH_USERS[username] = True


async def check_auth_user(username: str):
    return username in AUTH_USERS
