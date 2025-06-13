"""---"""
from ecomm import Postgres
from pandas import DataFrame

from prints_zpls_fulfillment.update_etiquetas_db.db.queries import queries
from prints_zpls_fulfillment.update_etiquetas_db.entities.etiquetas import Etiqueta
from prints_zpls_fulfillment.update_etiquetas_db.repositories.i_repositorio_etiquetas import IRepositorioEtiquetas

class HandlerPostgres(IRepositorioEtiquetas):

    def __init__(self):
        self.db: Postgres = None

    def __enter__(self):
        self.db = Postgres()
        return self.db

    def __exit__(self, exc_type, exc, tb):
        if self.db:
            self.db.close()

    def carrega_etiquetas(self, path_etiqueta: str) -> str:
        etiqueta_obj = Etiqueta(path_etiqueta)
        return etiqueta_obj.carrega_etiquetas(path_etiqueta)

    def separa_etiquetas(self, etiquetas: str) -> list:
        etiqueta_obj = Etiqueta('')
        return etiqueta_obj.separa_etiquetas(etiquetas)

    def manipulacao_etiquetas(self, etiqueta: str) -> dict:
        etiqueta_obj = Etiqueta('')
        return etiqueta_obj.manipulacao_etiquetas(etiqueta)

    def estrutura_etiqueta(self, etiqueta: str) -> str:
        etiqueta_obj = Etiqueta('')
        return etiqueta_obj.estrutura_etiqueta(etiqueta)

    def identificacao_ean(self) -> DataFrame:
        try:
            with Postgres() as db:
                return db.query(queries.get('ml_info', ''))
        except Exception:
            return DataFrame()

    def update_db(self, df_etiquetas: DataFrame):
        with Postgres() as db:
            db.insert(df=df_etiquetas, table='etiqueta_full')
