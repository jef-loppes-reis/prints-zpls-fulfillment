from dotenv import load_dotenv
import os

load_dotenv()  # Carrega o arquivo .env

USERS = os.getenv("USERS")
# print(USERS)  # Apenas para verificar se está funcionando
