from fastapi import APIRouter, Request, HTTPException, status

router = APIRouter()


@router.get('/user-details')
async def get_current_user(request: Request):
    user = request.state.user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorised")
    return f"Hello, {user.user_name}"
