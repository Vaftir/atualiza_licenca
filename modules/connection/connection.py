# Importando os módulos necessários
import os
import mysql.connector
from mysql.connector import Error

# Definindo a classe de conexão
class Connection:
    def __init__(self, host, database, user, password):
        self.connection = None  # Inicializando a variável de conexão como nula
        self.cursor = None  # Inicializando o cursor como nulo

        self.host = host
        self.database = database
        self.user = user
        self.password = password


    # Método para estabelecer a conexão com o banco de dados
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database")  # Mensagem de sucesso
            return True
        except Error as e:
            print(f"The error '{e}' occurred")  # Mensagem de erro em caso de falha na conexão
            return False

    # Método para executar uma consulta (INSERT, UPDATE, DELETE)
    def execute_query(self, query):
        try:
            self.cursor.execute(query)  # Executa a consulta
            self.connection.commit()  # Confirma as alterações no banco de dados
            print("Query executed successfully")  # Mensagem de sucesso
            return True
        except Error as e:
            print(f"The error '{e}' occurred")  # Mensagem de erro em caso de falha na execução da consulta
            return False

    # Método para executar uma consulta de leitura (SELECT)
    def execute_read_query(self, query):
        result = None
        try:
            self.cursor.execute(query)  # Executa a consulta de leitura
            result = self.cursor.fetchall()  # Obtém todos os resultados da consulta
            return result  # Retorna os resultados
        except Error as e:
            print(f"The error '{e}' occurred")  # Mensagem de erro em caso de falha na execução da consulta
            return result

    # Método para desconectar do banco de dados
    def disconnect(self):
        if self.connection is not None and self.connection.is_connected():
            self.cursor.close()  # Fecha o cursor
            self.connection.close()  # Fecha a conexão
            print("Connection closed")  # Mensagem de sucesso ao fechar a conexão
            return True
        else:
            print("No connection to close")
            return False


'''
# Exemplo de uso da classe de conexão
# Importando a classe de conexão
from connection import Connection

# Criando uma instância da classe de conexão
connection = Connection("localhost",
'''