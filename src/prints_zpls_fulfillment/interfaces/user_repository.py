from abc import ABC, abstractmethod

from prints_zpls_fulfillment.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        """Método para buscar um usuário pelo nome de usuário"""
