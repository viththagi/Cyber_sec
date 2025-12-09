def check_password_strength(password):
    common_weak = ["123456", "password", "admin", "qwerty"]

    # Too short?
    if len(password) < 8:
        return False

    # Common password?
    if password.lower() in common_weak:
        return False

    return True
