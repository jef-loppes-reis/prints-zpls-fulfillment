"""
    Entidade para a base de EAN SIAC
"""

class BaseEanSiac:

    @staticmethod
    def set_base_ean_siac(base_ean_siac: list[str]) -> str:
        if not base_ean_siac:
            raise ValueError('Base de EAN SIAC nao pode ser vazia')
        if not isinstance(base_ean_siac, list):
            raise ValueError('Base de EAN SIAC deve ser uma lista')
        if not all(isinstance(ean, str) for ean in base_ean_siac):
            raise ValueError('Base de EAN SIAC deve ser uma lista de strings')

        return ','.join(base_ean_siac)
