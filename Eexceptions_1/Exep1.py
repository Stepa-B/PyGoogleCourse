def validate_user (username, minlen):
    assert type(username) == str, "user name must be a string"
    if not type(minlen)==int:
        raise ValueError("minlen must be int")
    if minlen < 1:
        raise ValueError ("minlen must be at least 1")
    if len(username) <minlen:
        return False
    if not username.isalnum():
        return False
    return True
print(validate_user ([], "10"))