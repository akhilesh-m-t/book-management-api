from fastapi import Request, HTTPException
from jose import JWTError, jwt
from helpers.yaml_loader import ACCESS_SECRET_KEY, ALGORITHM


async def check_user_authorization(request: Request, call_next):

    token = request.cookies.get("token")

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        user = jwt.decode(token=token, key=ACCESS_SECRET_KEY,
                          algorithms=[ALGORITHM])
        request.state.user = user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    print(user)

    response = await call_next(request)
    return response
