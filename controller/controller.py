# Classe responsável por controlar a aplicação

# Importa as classes necessárias
from classes.atualizaLicenca import AtualizaLicenca

class Controller:

    def __init__(self):
        self.atualiza_licenca = AtualizaLicenca()  # Instância da classe AtualizaLicenca
    
    def run(self):
        try:
            self.atualiza_licenca.atualiza_licenca()  # Chama o método atualiza_licenca
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