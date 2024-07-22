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
    

if __name__ == "__main__":
    if main():
        print("Processo finalizado com sucesso")
    else:
        print("Erro ao executar o processo")