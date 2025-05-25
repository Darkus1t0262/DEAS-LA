from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

app = FastAPI(title="Auth Service")

# Configuración de JWT
SECRET_KEY = "your-very-secret-key"    # Cámbialo por algo seguro
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Seguridad
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Usuario simulado
fake_user = {
    "username": "admin",
    # contraseña “secret” cifrada
    "hashed_password": pwd_context.hash("secret")
}

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user
    if form_data.username != user["username"] or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user["username"], "exp": expire}
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "auth"}

@app.get("/secure-data")
async def secure_data(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": payload.get("sub"), "data": "This is secured content"}
