from fastapi import APIRouter, HTTPException, status, Response
from schemas import Create_User, Login_User
from models import Users
from datetime import timedelta
from passlib.context import CryptContext
from database import db_dependency
from helpers.password_checker import verify_password
from helpers.jwt_helper import create_jwt_access_token
from helpers.yaml_loader import ACCESS_SECRET_KEY_EXPIRES


router = APIRouter(
    prefix='/auth',
    tags=['auth'])
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(db: db_dependency, user: Create_User):
    existing_user = db.query(Users).filter(
        Users.user_email == user.user_email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='User already exists.!')
    bcrypt_hashed_password = bcrypt_context.hash(user.password)
    new_user = Users(
        user_name=user.user_name,
        user_email=user.user_email,
        full_name=user.full_name,
        hashed_password=bcrypt_hashed_password,
        is_active=user.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": "User added Successfully!",
        "user_details": new_user
    }


@router.post('/login', status_code=status.HTTP_200_OK)
async def login(db: db_dependency, user: Login_User, response: Response):
    existing_user = db.query(Users).filter(
        Users.user_email == user.user_email).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User don't exist.")
    password_check = verify_password(
        password_to_check=user.password, hashed_password_from_db=existing_user.hashed_password)
    if not password_check:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Wrong Password Email combination")
    jwt_payload = {
        "user_id": existing_user.id,
        "user_name": existing_user.user_name,
        "user_email": existing_user.user_email,
    }
    access_token_expires = timedelta(minutes=ACCESS_SECRET_KEY_EXPIRES)
    access_token = create_jwt_access_token(
        jwt_payload, access_token_expires)
    response.set_cookie(key="token", value=access_token,
                        max_age=10000, httponly=True)
    return {
        "message": "Login successfull!"
    }
