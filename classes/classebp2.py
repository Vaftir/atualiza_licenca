# Importando o módulo necessário
import time
from modules.connection.connection import Connection

class SalvaDados:
    """
    Classe responsável por salvar dados em um banco de dados.
    
    Esta classe gerencia a conexão com o banco de dados e fornece métodos para salvar diferentes tipos de registros.
    
    Atributos:
    -----------
    connection : Connection
        Instância da conexão com o banco de dados.
    """
    
    # region Construtor
    def __init__(self, banco):
        """
        Inicializa a classe SalvaDados e tenta estabelecer uma conexão com o banco de dados.

        Parâmetros:
        -----------
        banco : dict
            Dicionário contendo as informações de conexão com o banco de dados (host, database, user, password).
        """
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
    def _salvarFilial(self, dados, id_monitoramento, id_atualizacao=None):
        """
        Salva um registro de filial no banco de dados.

        Parâmetros:
        -----------
        dados : dict
            Dicionário contendo os dados da filial (filial, nome, descricao, num_dias).
        id_monitoramento : int
            ID do monitoramento associado à filial.
        id_atualizacao : int, opcional
            ID da atualização associada à filial (padrão é None).

        Retorna:
        --------
        bool
            True se o registro for salvo com sucesso, False caso contrário.
        """
        try:
            query = (
                "INSERT INTO filiais (numero_filial, nome, descricao_manager, num_dias, id_monitoramento, id_atualizacao, data_criacao) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            )
            params = (
                dados['filial'], dados['nome'], dados['descricao'], dados['num_dias'],
                id_monitoramento, id_atualizacao, time.strftime('%Y-%m-%d %H:%M:%S')
            )
            if self.connection.execute_query(query, params):
                print(f"Registro '{dados['nome']}' salvo com sucesso.")
                return True
            else:
                print(f"Erro ao salvar registro '{dados['nome']}'.")
                return False
        except Exception as e:
            print(f"Erro ao salvar filial: {e}")
            return False

    def _salvarMonitoramento(self, status, descricao, numero_de_dias, id_atualizacao):
        """
        Salva um registro de monitoramento no banco de dados.

        Parâmetros:
        -----------
        status : str
            Status do monitoramento.
        descricao : str
            Descrição do monitoramento.
        numero_de_dias : int
            Número de dias do monitoramento.
        id_atualizacao : int
            ID da atualização associada ao monitoramento.

        Retorna:
        --------
        int ou bool
            ID do monitoramento salvo se bem-sucedido, False caso contrário.
        """
        try:
            data = time.strftime('%Y-%m-%d %H:%M:%S')
            query = (
                "INSERT INTO monitoramento (data, descricao, status, numero_de_dias, id_atualizacao, data_atualizacao) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )
            params = (data, descricao, status, numero_de_dias, id_atualizacao, data)
            if self.connection.execute_query(query, params):
                print(f"Registro '{status}' salvo com sucesso.")
                self.connection.cursor.execute("SELECT MAX(id) FROM monitoramento")
                return self.connection.cursor.fetchone()[0]
            else:
                print(f"Erro ao salvar registro '{status}'.")
                return False
        except Exception as e:
            print(f"Erro ao salvar monitoramento: {e}")
            return False

    def _salvarMonitoramentoSemAtualizacao(self, status, descricao, numero_de_dias):
        """
        Salva um registro de monitoramento no banco de dados, sem associar uma atualização.

        Parâmetros:
        -----------
        status : str
            Status do monitoramento.
        descricao : str
            Descrição do monitoramento.
        numero_de_dias : int
            Número de dias do monitoramento.

        Retorna:
        --------
        int ou bool
            ID do monitoramento salvo se bem-sucedido, False caso contrário.
        """
        # pega o menor numero de dias de dados
       
        try:
            data = time.strftime('%Y-%m-%d %H:%M:%S')
            query = (
                "INSERT INTO monitoramento (data, descricao, status, numero_de_dias) "
                "VALUES (%s, %s, %s, %s)"
            )
            params = (data, descricao, status, numero_de_dias)
            if self.connection.execute_query(query, params):
                print(f"Registro '{status}' salvo com sucesso.")
                self.connection.cursor.execute("SELECT MAX(id_monitoramento) FROM monitoramento")
                return self.connection.cursor.fetchone()[0]
            else:
                print(f"Erro ao salvar registro '{status}'.")
                return False
        except Exception as e:
            print(f"Erro ao salvar monitoramento sem atualização: {e}")
            return False

    def _salvarAtualizacao(self, status, texto, dados=None):
        """
        Salva um registro de atualização no banco de dados.

        Parâmetros:
        -----------
        status : str
            Status da atualização.
        texto : str
            Texto da atualização.
        dados : list, opcional
            Lista de dicionários contendo dados de filiais a serem associados à atualização (padrão é None).

        Retorna:
        --------
        bool
            True se o registro for salvo com sucesso, False caso contrário.
        """
        try:
            data = time.strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data e hora atual
            query = "INSERT INTO atualizacao (status, data, texto) VALUES (%s, %s, %s)"
            values = (status, data, texto)
            
            # Executa a consulta de inserção
            if self.connection.execute_query(query, values):
                print(f"Registro '{status}' salvo com sucesso.")
                
                # Obtém o id da atualização inserida
                self.connection.cursor.execute("SELECT MAX(id) FROM atualizacao")
                id_atualizacao = self.connection.cursor.fetchone()[0]

                menor_dias = min([dado['menor_dias'] for dado in dados])
                id_monitoramento = self._salvarMonitoramento(status, texto, menor_dias, id_atualizacao) 
                # Salva os dados de filiais se fornecidos
                if dados:
                    for dado in dados:
                        # Salva os dados de cada filial
                        self._salvarFilial(dado, id_monitoramento, id_atualizacao)
                
                return True
            else:
                print(f"Erro ao salvar registro '{status}'.")
                return False
        except Exception as e:
            print(f"Erro ao salvar atualização: {e}")
            return False

    # endregion

    # region Métodos Públicos
    def salvar(self, texto, status, flag, dados=None):
        """
        Salva o texto com base no status fornecido e em uma flag indicando o tipo de operação.

        Parâmetros:
        -----------
        texto : str
            Texto a ser salvo.
        status : str
            Status da operação (SUCCESS, ERROR, WARNING).
        flag : bool
            Flag indicando se deve associar a uma atualização (True) ou não (False).
        dados : list, opcional
            Lista de dicionários contendo dados de filiais a serem associados (padrão é None).

        Retorna:
        --------
        bool ou int
            True se a operação for bem-sucedida, False caso contrário. Retorna o ID do monitoramento se flag for False.
        """
        if flag:
            if status in ["SUCCESS", "ERROR", "WARNING"]:
                return self._salvarAtualizacao(status, texto, dados)
            else:
                print("Status inválido")
                return False
        else:
            if dados:
                menor_dias = min([dado['menor_dias'] for dado in dados])
                return self._salvarMonitoramentoSemAtualizacao(status=status, descricao=texto, numero_de_dias=menor_dias,)
            else:
                print("Dados inválidos")
                return False
    # endregion

    # region Destrutor
    def __del__(self):
        """
        Fecha a conexão com o banco de dados se ela existir.
        """
        if self.connection:
            self.connection.disconnect()
            print("Conexão encerrada")
    # endregion