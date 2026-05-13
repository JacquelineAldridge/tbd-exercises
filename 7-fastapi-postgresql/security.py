from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()

def crear_hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verificar_password(password: str, hashed_password:str) -> bool:
    return pwd_context.verify(password, hashed_password)
