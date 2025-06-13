# Interface do repositório de etiquetas
from abc import ABC, abstractmethod
from pandas import DataFrame

class IRepositorioEtiquetas(ABC):

    @abstractmethod
    def carrega_etiquetas(self, path_etiqueta: str) -> str:
        ...

    @abstractmethod
    def separa_etiquetas(self, etiquetas: str) -> list:
        ...

    @abstractmethod
    def manipulacao_etiquetas(self, etiqueta: str) -> dict:
        ...

    @abstractmethod
    def estrutura_etiqueta(self, etiqueta: str) -> str:
        ...

    @abstractmethod
    def identificacao_ean(self) -> DataFrame:
        ...

    @abstractmethod
    def update_db(self, df_etiquetas: DataFrame):
        ...
