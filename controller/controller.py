# Classe responsável por controlar a aplicação

# Importa as classes necessárias
from classes.atualizaLicenca import AtualizaLicenca
from classes.monitoraLicenca import MonitoraLicenca
class Controller:

    def __init__(self):
        self.atualiza_licenca = AtualizaLicenca()  # Instância da classe AtualizaLicenca
        self.monitora_licenca = MonitoraLicenca()

    def run(self):
        try:
            self.monitora_licenca.monitora_licenca()
            # self.atualiza_licenca.atualiza_licenca()
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