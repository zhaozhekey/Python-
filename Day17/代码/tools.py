import hashlib


def encrypt_password(password,x = "asdfgh"):
    h = hashlib.sha256()
    h.update(password.encode('utf-8'))
    h.update(x.encode("utf-8"))
    return h.hexdigest()

