from prints_zpls_fulfillment.interfaces.user_repository import UserRepository

class LoginUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, username: str, password: str) -> bool:
        """Método para autenticar o usuário usando o repositório de usuários."""
        user = self.user_repository.get_user_by_username(username)
        
        if user and user.password == password:
            return True
        return False
