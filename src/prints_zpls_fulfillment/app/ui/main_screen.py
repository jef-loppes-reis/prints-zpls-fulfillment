import customtkinter as ctk

class MainScreen(ctk.CTkFrame):
    def __init__(self, master, user_info=None):
        super().__init__(master)
        self.master = master

        # Exibe as informações do usuário se forem passadas
        if user_info:
            self.user_label = ctk.CTkLabel(self, text=f"Usuário: {user_info['username']}")
            self.user_label.pack(pady=(20, 5))

        # Outros widgets e informações que você quer exibir
        self.label = ctk.CTkLabel(self, text="Bem-vindo à tela principal!")
        self.label.pack(pady=(20, 5))
