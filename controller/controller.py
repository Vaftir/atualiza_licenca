# Autor: Yago Assis Mendes Faria
from classes.monitoraLicenca import MonitoraLicenca

'''
Classe Controller responsável por controlar o fluxo do programa
Atributos:

    monitora_licenca: MonitoraLicenca
Métodos:
    run: bool
dependencias:
    MonitoraLicenca
'''
class Controller:

    def __init__(self):
        self.monitora_licenca = MonitoraLicenca()

    def run(self):
        try:
            self.monitora_licenca.monitora_licenca()
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
        



'''

from classes.atualizaLicenca import AtualizaLicenca

def main():

    try:
        # Cria uma instância da classe Licenca
        atualiza_licenca = AtualizaLicenca()
        # Chama o método atualiza_licenca
        atualiza_licenca.atualiza_licenca()      
        return True
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False
'''