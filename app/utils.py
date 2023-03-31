from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashing(password: str):
    return pwd_context.hash(password)

def verifying(plain_pass, hashed_pass):
    return pwd_context.verify(plain_pass, hashed_pass)