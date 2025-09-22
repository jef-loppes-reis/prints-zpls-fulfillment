import re
from typing import Dict, Any

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

    def manipulacao_etiquetas(self, etiqueta: str) -> Dict[str, Any]:
        if not etiqueta:
            raise ValueError('Nao existe etiqueta')

        produto = {
            'cod_ref': '',
            'cod_ml': '',
            'qtd_etq': 0,
        }

        etiqueta_slice = etiqueta.split('\n')

        # helper: converte _HH -> chr(HH) se houver ^FH
        def decode_hex_escapes(s: str, esc_char: str = '_') -> str:
            pattern = re.escape(esc_char) + r'([0-9A-Fa-f]{2})'
            return re.sub(pattern, lambda m: chr(int(m.group(1), 16)), s)

        for x in etiqueta_slice:
            # detecta se tem ^FH antes de ^FD
            fh_match = re.search(r'\^FH(.)', x)
            # Se há ^FH mas sem caractere especificado (^FH seguido por ^), usa '_' como padrão
            # Se há ^FH com caractere especificado (^FH_ por exemplo), usa esse caractere
            if fh_match:
                esc_char = fh_match.group(1) if fh_match.group(1) != '^' else '_'
            else:
                esc_char = '_'
                fh_match = None

            if not produto['cod_ml']:
                codml_res = re.findall(r'\^FD(.*?)\^FS', x)
                if codml_res:
                    produto['cod_ml'] = decode_hex_escapes(codml_res[0], esc_char) if fh_match else codml_res[0]

            if not produto['cod_ref']:
                codref_res = re.findall(r'\^FDSKU: (.*?)\^FS', x)
                if codref_res:
                    produto['cod_ref'] = decode_hex_escapes(codref_res[0], esc_char) if fh_match else codref_res[0]

            if produto['qtd_etq'] < 1:
                qtd_et_res = re.findall(r'\^PQ(.*?)\,', x)
                if qtd_et_res:
                    produto['qtd_etq'] = int(qtd_et_res[0])

        return produto

    def estrutura_etiqueta(self, etiqueta: str) -> str:
        zpl_code = re.sub(r'(^\^PQ)(\d+)', '\\g<1>1', etiqueta, count=0, flags=re.MULTILINE)
        return zpl_code
