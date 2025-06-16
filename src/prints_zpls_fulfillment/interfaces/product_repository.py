from abc import ABC, abstractmethod
from pandas import DataFrame

class ProductRepository(ABC):
    @abstractmethod
    def find_product_by_barcode(self, barcode: str) -> DataFrame:
        """Método para buscar o produto pelo código de barras"""

    @abstractmethod
    def update_product(self, update_query: str) -> None:
        """Método para atualizar o banco de dados"""
