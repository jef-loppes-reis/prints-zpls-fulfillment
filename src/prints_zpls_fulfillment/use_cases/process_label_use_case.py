from datetime import datetime

from pandas import DataFrame

from prints_zpls_fulfillment.interfaces.product_repository import ProductRepository
from prints_zpls_fulfillment.infrastructure.zebra_printer import ZebraPrinter

class ProcessLabelUseCase:

    def __init__(self, zebra_printer: ZebraPrinter, product_repository: ProductRepository):
        self.zebra_printer = zebra_printer
        self.product_repository = product_repository

    def execute(self, ean: str, data_validade: str, coduser: str) -> dict:
        """Processa a impressão das etiquetas com base nos dados do produto"""

        # Passo 1: Consultar o produto pelo EAN
        # product_data: DataFrame = self.product_repository.find_product_by_barcode(ean)
        # print(product_data)

        # if product_data.empty:
        #     print("Produto não encontrado.")
        #     return

        # Passo 3: Imprimir o código ZPL
        product_data: DataFrame = self.product_repository.find_product_by_barcode(ean)
        print(product_data)
        if product_data.empty:
            return {}
        product_data_dict = product_data.to_dict('records')[0]
        zpl_code: str = product_data_dict.get('zpl_code', '')
        # self.print_label(zpl_code)
        # Passo 4: Atualizar o status da impressão no banco de dados
        self.update_product_status(
            id_db=product_data_dict.get('idx_etq', 0),
            coduser=coduser,
            data_validade=data_validade,
            codml=product_data_dict.get('cod_ml', '')
        )
        return product_data_dict


    def print_label(self, zpl_code: str) -> None:
        """Imprime a etiqueta usando a impressora Zebra"""
        self.zebra_printer.print_label(bytes(zpl_code, encoding='utf-8'))

    def update_product_status(self, id_db: int, coduser: str, data_validade: str, codml: str) -> None:
        """Atualiza o status do produto no banco de dados após a impressão"""
        __zpl_code_data_validade: str = 'null' if not data_validade else data_validade
        update_query = f"""
            UPDATE "ECOMM".etiqueta_full
            SET
                etq_impressa = TRUE,
                cod_user = '{coduser}',
                data_impressao = '{datetime.now()}',
                zpl_code_data_validade = {__zpl_code_data_validade}
            WHERE
                idx_etq = {id_db}
                AND cod_ml = '{codml}';
        """
        self.product_repository.update_product(update_query)
