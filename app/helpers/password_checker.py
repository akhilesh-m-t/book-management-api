from passlib.context import CryptContext
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def verify_password(password_to_check: str, hashed_password_from_db: str):
    if not bcrypt_context.verify(password_to_check, hashed_password_from_db):
        return False
    return True
