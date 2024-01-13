from datetime import timedelta, datetime
from jose import JWTError, jwt
from .yaml_loader import ACCESS_SECRET_KEY, ALGORITHM


def create_jwt_access_token(data: dict, expires_in: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_in:
        expire = datetime.utcnow() + expires_in
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, ACCESS_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, ACCESS_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return False
