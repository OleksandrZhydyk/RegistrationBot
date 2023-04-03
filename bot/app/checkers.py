import string


def check_username(username: str) -> bool:
    special_symbols = '!?+-*%$#@~`"/:;()[]{}|<>.,\''
    forbidden_symbols = special_symbols
    for symbol in username:
        if symbol in forbidden_symbols:
            return False
    return True


def check_password(password: str, username: str) -> bool:
    password_length = len(password)
    if password_length < 8:
        return False
    special_symbols = '!?+-*%$#@~`"/:;()[]{}|<>.,\''
    for i in range(3, password_length-1):
        if username[i-3:i+1] in password:
            return False
    for symbol in password:
        if symbol in special_symbols:
            return True
    return False
