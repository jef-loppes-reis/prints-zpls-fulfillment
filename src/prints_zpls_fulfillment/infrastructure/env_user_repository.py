import os
from dotenv import load_dotenv

from prints_zpls_fulfillment.domain.user import User
from prints_zpls_fulfillment.interfaces.user_repository import UserRepository

# Carrega as variáveis do arquivo .env
load_dotenv()

class EnvUserRepository(UserRepository):

    def __init__(self):
        self.users = {}
        self.load_users_from_env()

    def load_users_from_env(self):
        """Carrega os usuários do arquivo .env"""
        users_env = os.getenv("USERS")
        if users_env:
            users_list = users_env.split(',')
            for user in users_list:
                username, password = user.split(':')
                self.users[username] = User(username, password)

    def get_user_by_username(self, username: str) -> User:
        """Retorna o usuário pelo nome de usuário"""
        return self.users.get(username, '0000')
