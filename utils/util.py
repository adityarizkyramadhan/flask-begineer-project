import uuid
import bcrypt

def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))

        return True
    except ValueError:
        return False


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def compare_password(password, hashed) :
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


