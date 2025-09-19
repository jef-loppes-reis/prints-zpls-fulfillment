"""---"""
from ecomm import Postgres
from pandas import DataFrame

from prints_zpls_fulfillment.interfaces.product_repository import ProductRepository

class PostgresRepository(ProductRepository):

    def __init__(self):
        self.db: Postgres = None

    # Método para abrir a conexão com o banco de dados.
    def __enter__(self):
        self.db = Postgres()
        return self.db

    # Método para fechar a conexão com o banco de dados.
    def __exit__(self, exc_type, exc, tb):
        if self.db:
            self.db.close()

    # Método para consultar o banco de dados e retornar um produto
    def find_product_by_barcode(self, barcode: str) -> DataFrame:
        try:
            with self:
                query = f"""
                    SELECT
                        etiqueta_full.*,
                        ml_info.title,
                        ml_info.sku
                    FROM
                        "ECOMM".etiqueta_full
                    LEFT JOIN
                        "ECOMM".ml_info ON etiqueta_full.cod_ml = ml_info.inventory_id
                    WHERE
                        etiqueta_full.ean ~* '{barcode}'
                        AND NOT etq_impressa
                    ORDER BY (etiqueta_full.etq_impressa, etiqueta_full.data_emissao)
                """
                return self.db.query(query).head(1)
        except Exception as e:
            print(f"Erro durante a consulta do produto: {e}")
        return DataFrame()  # Retorna um DataFrame vazio em caso de erro

    # Método para atualizar os dados do banco de dados
    def update_product(self, update_query: str) -> None:
        try:
            with self:
                self.db.query(update_query)
        except Exception as e:
            print(f"Erro durante a atualização do produto: {e}")
