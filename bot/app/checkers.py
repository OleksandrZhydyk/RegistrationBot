import string


def check_username(username: str) -> bool:
    special_symbols = '!?+-*%$#@~`"/:;()[]{}|<>.,\''
    forbidden_symbols = special_symbols + string.digits
    for symbol in username:
        if symbol in forbidden_symbols:
            return False
    return True


def check_password(password: str) -> bool:
    if len(password) < 8:
        return False
    special_symbols = '!?+-*%$#@~`"/:;()[]{}|<>.,\''
    for symbol in password:
        if symbol in special_symbols:
            return True
    return False
