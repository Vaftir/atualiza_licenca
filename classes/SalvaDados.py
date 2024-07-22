# Importando o módulo necessário
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
            print("Conexão com o banco de dados estabelecida com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")  # Exibe erro se a conexão falhar

    # endregion

    # region Métodos Privados para Salvar Dados
    def _salvar(self, status, texto):
        """Método genérico para salvar dados no banco de dados."""
        data = time.strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data e hora atual
        query = f"INSERT INTO atualizacao (status, data, texto) VALUES ('{status}', '{data}', '{texto}')"
        # Executa a consulta e verifica se o registro foi salvo com sucesso
        if self.connection.execute_query(query):
            print(f"Registro '{status}' salvo com sucesso.")
            return True
        else:
            print(f"Erro ao salvar registro '{status}'.")
            return False

    def _salva_sucesso(self, texto):
        """Salva uma mensagem de sucesso."""
        return self._salvar('SUCCESS', texto)
    
    def _salva_erro(self, texto):
        """Salva uma mensagem de erro."""
        if not texto:
            texto = "Erro não especificado"
        return self._salvar('ERROR', texto)
    
    def _salva_aviso(self, texto):
        """Salva uma mensagem de aviso."""
        return self._salvar('WARNING', texto)

    # endregion

    # region Métodos Públicos
    def salvar(self, texto, status):
        """Salva o texto com base no status fornecido."""
        if status == "SUCCESS":
            return self._salva_sucesso(texto)
        elif status == "ERROR":
            return self._salva_erro(texto)
        elif status == "WARNING":
            return self._salva_aviso(texto)
        else:
            print("Status inválido")
            return False

    # endregion

    # region Destrutor
    def __del__(self):
        """Fecha a conexão com o banco de dados se ela existir."""
        if self.connection:
            self.connection.disconnect()
            print("Conexão encerrada")

    # endregion
