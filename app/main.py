from middleware.auth_handler import check_user_authorization
from fastapi import Depends, FastAPI
from database import engine
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
import models
from routers import auth, books
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.middleware(middleware_type="http")(check_user_authorization)
app.include_router(router=auth.router)
app.include_router(router=books.router, dependencies=[
                   Depends(check_user_authorization)])
