from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("secure_storage/master_access.key", "wb") as f:
    f.write(key)
