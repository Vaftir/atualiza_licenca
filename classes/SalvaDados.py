# Importando o módulo Connection
import time
from modules.connection.connection import Connection

class SalvaDados:
    # region Construtor
    def __init__(self, banco):
        self.connection = None  # Inicializa a variável de conexão como nula
        try:
            # Cria uma instância da classe Connection e tenta conectar ao banco de dados
            self.connection = Connection(banco["host"], banco["database"], banco["user"], banco["password"])
            self.connection.connect()
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")  # Exibe erro se a conexão falhar

    # endregion

    # region Métodos Privados para Salvar Dados
    def _salva_sucesso(self, texto):
        # Inserir no banco de dados o status de sucesso, a data e o texto fornecido
        data = time.strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data e hora atual
        query = f"INSERT INTO atualizacao (status, data, texto) VALUES ('SUCCESS', '{data}', '{texto}')"
        # Executa a consulta e verifica se o registro foi salvo com sucesso
        if self.connection.execute_query(query):
            print("Registro salvo com sucesso")
            return True
        else:
            print("Erro ao salvar registro")
            return False
    
    def _salva_erro(self, texto):
        if not texto:
            texto = "Erro não especificado"
        # Inserir no banco de dados o status de erro, a data e o texto fornecido
        data = time.strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data e hora atual
        query = f"INSERT INTO atualizacao (status, data, texto) VALUES ('ERROR', '{data}', '{texto}')"
        # Executa a consulta e verifica se o registro foi salvo com sucesso
        if self.connection.execute_query(query):
            print("Registro salvo com sucesso")
            return True
        else:
            print("Erro ao salvar registro")
            return False
    
    def _salva_aviso(self, texto):
        # Inserir no banco de dados o status de aviso, a data e o texto fornecido
        data = time.strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data e hora atual
        query = f"INSERT INTO atualizacao (status, data, texto) VALUES ('WARNING', '{data}', '{texto}')"
        # Executa a consulta e verifica se o registro foi salvo com sucesso
        if self.connection.execute_query(query):
            print("Registro salvo com sucesso")
            return True
        else:
            print("Erro ao salvar registro")
            return False
    # endregion

    # region Métodos Públicos
    def salvar(self, texto, status):
        # Salva o texto com base no status fornecido
        if status == "SUCCESS":
            return self._salva_sucesso(texto)
        elif status == "ERROR":
            return self._salva_erro(texto)
        elif status == "WARNING":
            return self._salva_aviso(texto)
        else:
            print("Status inválido")  # Exibe mensagem de erro se o status for inválido

    # endregion

    # region Destrutor
    def __del__(self):
        # Fecha a conexão com o banco de dados se ela existir
        if self.connection:
            self.connection.disconnect()
            print("Conexão encerrada")  # Mensagem de sucesso ao fechar a conexão
    # endregion
