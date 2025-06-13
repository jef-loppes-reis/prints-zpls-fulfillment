"""---"""
import customtkinter as ctk

from prints_zpls_fulfillment.app.ui.login_screen import LoginScreen
from prints_zpls_fulfillment.app.ui.input_data_screen import InputDataScreen

class Application(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Gestor de Etiquetas")
        self.geometry("500x400")

        # Inicializa a tela de login e passa a instância de Application (self) para ela
        self.login_screen = LoginScreen(self)
        self.login_screen.pack(fill="both", expand=True)

    def go_to_input_data_screen(self, user_info=None):
        """Redireciona para a tela de entrada de dados após login bem-sucedido"""
        self.login_screen.pack_forget()  # Esconde a tela de login
        self.input_data_screen = InputDataScreen(self, user_info=user_info)  # Passa as informações para a tela de entrada de dados
        self.input_data_screen.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
