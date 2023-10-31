from cryptography.fernet import Fernet


def encrypted(password: str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    password_b = bytes(password, 'ascii')
    encrypted_password = f.encrypt(password_b)
    return encrypted_password.decode('ascii')


def decrypt(password: str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    password_b = bytes(password, 'ascii')
    password_decrypt_b = f.decrypt(password_b)
    return password_decrypt_b.decode('ascii')
