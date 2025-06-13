import customtkinter as ctk
from prints_zpls_fulfillment.use_cases.login_use_case import LoginUseCase
from prints_zpls_fulfillment.infrastructure.env_user_repository import EnvUserRepository  # Usando o repositório que lê do .env

class LoginScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master  # Aqui master é a instância de Application

        # Inicializa o repositório de usuários que carrega dados do .env
        user_repository = EnvUserRepository()  # Agora usando o repositório que lê do .env
        self.login_use_case = LoginUseCase(user_repository)

        # Campos de login
        self.label_login = ctk.CTkLabel(self, text="Login:")
        self.label_login.pack(pady=(50, 5))
        self.entry_login = ctk.CTkEntry(self, width=300)
        self.entry_login.pack()
        self.entry_login.bind("<Return>", self.autenticar_usuario_event)

        # Campo de senha
        self.label_senha = ctk.CTkLabel(self, text="Senha:")
        self.label_senha.pack(pady=(20, 5))
        self.entry_senha = ctk.CTkEntry(self, width=300, show="*")
        self.entry_senha.pack()
        self.entry_senha.bind("<Return>", self.autenticar_usuario_event)

        # Botão de login
        self.button_login = ctk.CTkButton(self, text="Login", command=self.autenticar_usuario)
        self.button_login.pack(pady=(20, 10))

        # Resultado do login
        self.frame_resultado = ctk.CTkFrame(self)
        self.frame_resultado.pack(pady=(10, 20), fill="x", padx=20)
        self.label_resultado = ctk.CTkLabel(self.frame_resultado, text="")
        self.label_resultado.pack(pady=10)

    def autenticar_usuario_event(self, event=None):
        """Método wrapper para lidar com a ligação de eventos para autenticação"""
        self.autenticar_usuario()

    def autenticar_usuario(self):
        login = self.entry_login.get()
        senha = self.entry_senha.get()

        # Usando o caso de uso de login para autenticar
        if self.login_use_case.authenticate(login, senha):
            self.label_resultado.configure(text="Login bem-sucedido!")
            self.carregar_interface()  # Carrega a interface após login bem-sucedido
            
            # Passando as informações do usuário para a tela de entrada de dados
            user_info = {'username': login}
            self.master.go_to_input_data_screen(user_info=user_info)  # Chama a navegação para a tela de dados
        else:
            self.label_resultado.configure(text="Login ou senha incorretos. Tente novamente.")

    def carregar_interface(self):
        """Método para carregar a próxima interface após o login"""
        self.label_login.destroy()
        self.entry_login.destroy()
        self.label_senha.destroy()
        self.entry_senha.destroy()
        self.button_login.destroy()
        self.frame_resultado.destroy()
