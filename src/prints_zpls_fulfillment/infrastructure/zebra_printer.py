import win32print
from rich import print as rprint
from print_log.print_log import PrintLog


class ZebraPrinter:
    __print_log: PrintLog = PrintLog()

    def __init__(self, printer_name=None):
        self.printer_name = printer_name or self._find_zebra_printer()

    def _find_zebra_printer(self):
        """Encontra a impressora Zebra conectada ao sistema"""
        lista_impressoras: list[tuple[int, str, str]] = win32print.EnumPrinters(
            win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
        )
        for __printer in lista_impressoras:
            if isinstance(__printer[2], str) and 'ZPL' in __printer[2]:
                rprint(__printer)
                self.__print_log.log(
                    title='Zebra Printer - Find Zebra Printer',
                    text=f'Impressora encontrada "{__printer[2]}"',
                    style='sucess'
                )
                return __printer[2]
        raise ValueError("Nenhuma impressora Zebra encontrada")

    def _start_print_job(self, printer):
        """Inicia o trabalho de impressão e retorna o identificador do trabalho"""
        try:
            return win32print.StartDocPrinter(printer, 1, ('Label', None, 'RAW'))
        except Exception as e:
            raise RuntimeError(f"Falha ao iniciar o trabalho de impressão: {e}") from e

    def _write_to_printer(self, printer, zpl_bytes):
        """Escreve os dados ZPL para a impressora"""
        try:
            win32print.WritePrinter(printer, zpl_bytes)
        except Exception as e:
            raise RuntimeError(f"Falha ao escrever na impressora: {e}") from e

    def _end_print_job(self, printer):
        """Finaliza o trabalho de impressão"""
        try:
            win32print.EndDocPrinter(printer)
        except Exception as e:
            raise RuntimeError(f"Falha ao finalizar o trabalho de impressão: {e}") from e

    def print_label(self, zpl_bytes: bytes) -> bool:
        """Imprime o rótulo ZPL usando a impressora encontrada"""
        if not self.printer_name:
            raise ValueError("Nenhuma impressora foi selecionada")

        _printer = win32print.OpenPrinter(self.printer_name)
        try:
            hJob = self._start_print_job(_printer)
            self._write_to_printer(_printer, zpl_bytes)
            self.__print_log.log(
                title='Zebra Printer - Print Label',
                text='Sucess - Etiqueta impressa!',
                style='sucess'
            )
            return True
        except Exception as e:
            self.__print_log.log(
                title='Zebra Printer - Print Label',
                text=f'Alert - Falha na impressao !\n\nCall Back: \n\n{e}',
                style='alert'
            )
            return False
        finally:
            self._end_print_job(_printer)
            win32print.ClosePrinter(_printer)
