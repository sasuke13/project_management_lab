class PasswordIsInvalid(Exception):
    # message = 'Password is invalid'

    def __init__(self, message):
        super().__init__(message[0])
