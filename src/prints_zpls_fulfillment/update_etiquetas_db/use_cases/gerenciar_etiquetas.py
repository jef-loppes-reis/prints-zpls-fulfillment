# Caso de Uso: GerenciarEtiquetas
from typing import List
from datetime import datetime

from pandas import DataFrame

class GerenciarEtiquetas:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def carregar_etiquetas(self, path_etiqueta: str) -> str:
        return self.repositorio.carrega_etiquetas(path_etiqueta)

    def separar_etiquetas(self, etiquetas: str) -> List[str]:
        return self.repositorio.separa_etiquetas(etiquetas)

    def manipular_etiquetas(self, etiqueta: str) -> dict:
        return self.repositorio.manipulacao_etiquetas(etiqueta)

    def montar_df(self, lista_etiquetas: List[str]) -> DataFrame:
        rows_to_append = []
        for et in lista_etiquetas:
            row_etq = self.manipular_etiquetas(et)
            etq_unica = self.repositorio.estrutura_etiqueta(et)
            idx_etq = 0
            for _ in range(row_etq.get('qtd_etq', 0)):
                row_etq.update({
                    'cod_user': None,
                    'data_emissao': datetime.today(),
                    'data_impressao': None,
                    'zpl_code': etq_unica,
                    'zpl_code_data_validade': None,
                    'etq_impressa': False,
                    'idx_etq': idx_etq
                })
                rows_to_append.append(row_etq.copy())
                idx_etq += 1
        df = DataFrame(rows_to_append)
        df_merge = df.merge(self.repositorio.identificacao_ean()[['cod_ml', 'ean']], on='cod_ml', how='left')
        return df_merge

    def atualizar_bd(self, df_etiquetas: DataFrame):
        self.repositorio.update_db(df_etiquetas)

    def executar(self, path_etiqueta: str):
        etiqueta = self.carregar_etiquetas(path_etiqueta)
        lista_etiquetas = self.separar_etiquetas(etiqueta)
        df_merge = self.montar_df(lista_etiquetas)
        self.atualizar_bd(df_merge)
