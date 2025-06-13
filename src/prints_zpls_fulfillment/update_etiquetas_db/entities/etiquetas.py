import re

class Etiqueta:
    def __init__(self, file_etiquetas: str):
        self.file_etiquetas = file_etiquetas

    def carrega_etiquetas(self, path_etiqueta: str) -> str:
        if not path_etiqueta.endswith('.txt'):
            raise ValueError('Esperava um arquivo .txt')
        with open(path_etiqueta, 'r', encoding='utf-8') as fp:
            return fp.read()

    def separa_etiquetas(self, etiquetas: str) -> list[str]:
        etiquetas_divididas = etiquetas.split('^XZ')[:-1]
        etiquetas_divididas = [
            etiqueta.strip() + "^XZ" if etiqueta != '' and "^XZ" not in etiqueta else etiqueta 
            for etiqueta in etiquetas_divididas if etiqueta != ''
        ]
        return etiquetas_divididas

    def manipulacao_etiquetas(self, etiqueta: str) -> dict:
        if not etiqueta:
            raise ValueError('Nao existe etiqueta')

        produto = {
            'cod_ref': '',
            'cod_ml': '',
            'qtd_etq': 0,
        }

        etiqueta_slice = etiqueta.split('\n')

        for x in etiqueta_slice:
            if not produto['cod_ml']:
                codml_res = re.findall(r'\^FD(.*?)\^FS', x)
                if codml_res:
                    produto['cod_ml'] = codml_res[0]
            if not produto['cod_ref']:
                codref_res = re.findall(r'\^FDSKU: (.*?)\^FS', x)
                if codref_res:
                    produto['cod_ref'] = codref_res[0]
            if produto['qtd_etq'] < 1:
                qtd_et_res = re.findall(r'\^PQ(.*?)\,', x)
                if qtd_et_res:
                    produto['qtd_etq'] = int(qtd_et_res[0])
        return produto

    def estrutura_etiqueta(self, etiqueta: str) -> str:
        zpl_code = re.sub(r'(^\^PQ)(\d+)', '\\g<1>1', etiqueta, count=0, flags=re.MULTILINE)
        return zpl_code
