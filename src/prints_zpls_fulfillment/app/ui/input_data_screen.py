import customtkinter as ctk

from prints_zpls_fulfillment.use_cases.process_label_use_case import ProcessLabelUseCase
from prints_zpls_fulfillment.infrastructure.zebra_printer import ZebraPrinter
from prints_zpls_fulfillment.infrastructure.postgres_repository import PostgresRepository

class InputDataScreen(ctk.CTkFrame):
    def __init__(self, master, user_info: dict):
        super().__init__(master)
        self.master = master

        # Recebe as informações do usuário (se necessário)
        self.user_info: dict = user_info

        # Inicializando os repositórios e o caso de uso de etiquetas
        zebra_printer = ZebraPrinter()
        postgres_repository = PostgresRepository()
        self.process_label_use_case = ProcessLabelUseCase(zebra_printer, postgres_repository)

        # Campos de entrada
        self.label_validade = ctk.CTkLabel(self, text="Data de Validade (DD/MM/AAAA):")
        self.label_validade.pack(pady=(20, 5))
        self.entry_validade = ctk.CTkEntry(self, width=300)
        self.entry_validade.pack()

        self.label_multiplicador = ctk.CTkLabel(self, text="Multiplicador X (quantidade de etiquetas):")
        self.label_multiplicador.pack(pady=(20, 5))
        self.entry_multiplicador = ctk.CTkEntry(self, width=70)
        self.entry_multiplicador.pack()

        self.label_barras = ctk.CTkLabel(self, text="Código de Barras (EAN):")
        self.label_barras.pack(pady=(20, 5))
        self.entry_barras = ctk.CTkEntry(self, width=300)
        self.entry_barras.pack()
        self.entry_barras.bind("<Return>", self.processar_codigo_barras)

        # Frame para exibir o resultado
        self.frame_resultado = ctk.CTkFrame(self)
        self.frame_resultado.pack(pady=(30, 10), fill="x", padx=20)
        self.label_resultado = ctk.CTkLabel(self.frame_resultado, text="Aguardando leitura do código de barras...")
        self.label_resultado.pack(pady=10)

    def processar_codigo_barras(self, event=None):
        # Lê os dados inseridos pelo usuário
        data_validade = self.entry_validade.get()  # Data de validade
        codigo_barras = self.entry_barras.get()  # Código de barras (EAN)
        multiplicador = self.entry_multiplicador.get()

        # Verificar se o multiplicador é válido (número inteiro positivo)
        if multiplicador and not multiplicador.strip().isnumeric():
            self.label_resultado.configure(text='O MULTIPLICADOR precisa ser numérico.')
            return
        if multiplicador and int(multiplicador.strip()) > 100:
            self.label_resultado.configure(text='Número máximo do MULTIPLICADOR é 100.')
            return
        if not multiplicador:
            multiplicador_int = 1  # Se o multiplicador não for fornecido, usa 1 por padrão
        else:
            multiplicador_int = int(multiplicador)

        if codigo_barras.strip():  # Verifica se o código de barras não está vazio
            texto_resultado = f'Validade: {data_validade}\nCódigo de Barras: {codigo_barras}'

            self.label_resultado.configure(text=texto_resultado)

            # Chama o caso de uso para processar as etiquetas
            self.processar_etiquetas(
                codigo_barras,
                data_validade,
                multiplicador_int,
                self.user_info.get('username', '')
            )

    def processar_etiquetas(self, codigo_barras: str, data_validade: str, multiplicador_int: int, coduser: str):
        # Usando o caso de uso de ProcessLabelUseCase para gerar e imprimir as etiquetas
        try:
            # Chama o caso de uso para processar a impressão das etiquetas
            for _ in range(multiplicador_int):
                res: dict = self.process_label_use_case.execute(
                    codigo_barras,
                    data_validade,
                    coduser
                )
                self.label_resultado.configure(
                    text=f'COD_REF: {res.get('sku', '')}\nCOD_ML: {res.get('cod_ml', '')}\nPRODUTO: {res.get('title')}''')
                # self.label_resultado.configure(text="Etiquetas geradas e enviadas para a impressora!")
        except Exception as e:
            self.label_resultado.configure(text=f"Erro ao gerar as etiquetas: {e}")
