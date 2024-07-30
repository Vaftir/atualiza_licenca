# Autor: Yago Assis Mendes Faria
import time
from modules.connection.connection import Connection

class SalvaDados:
    """
    Classe responsável por salvar dados em um banco de dados.
    
    Esta classe gerencia a conexão com o banco de dados e fornece métodos para salvar diferentes tipos de registros.
    
    Atributos:
   
    connection : Connection
        Instância da conexão com o banco de dados.
    -------------
    dependências:
        Connection : módulo connection.connection
        time : módulo time
    methods:
        __init__ : None
        __exit__ : None
        _salvarFilial : bool
        _salvarMonitoramento : bool
        _salvarMonitoramentoSemAtualizacao : bool
        _salvarAtualizacao : bool
        salvar

    """
    
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

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.connection:
            self.connection.disconnect()

    def _salvarFilial(self, dados, id_monitoramento, id_atualizacao):
        """
        Salva um registro de filial no banco de dados.
        """
        print(f"Salvando filial '{dados}'...")
        try:
            query = (
                "INSERT INTO filiais (numero_filial, nome, descricao_manager, num_dias, id_monitoramento, id_atualizacao, data_criacao) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            )
            params = (
                dados['filial'], dados['nome'], dados['licenca'], dados['num_dias'],
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
                result = self.connection.execute_read_query("SELECT MAX(id_monitoramento) FROM monitoramento")
                return result[0][0] if result else False
            else:
                print(f"Erro ao salvar registro '{status}'.")
                return False
        except Exception as e:
            print(f"Erro ao salvar monitoramento: {e}")
            return False

    def _salvarMonitoramentoSemAtualizacao(self, status, descricao, numero_de_dias):
        """
        Salva um registro de monitoramento no banco de dados, sem associar uma atualização.
        """
        try:
            data = time.strftime('%Y-%m-%d %H:%M:%S')
            query = (
                "INSERT INTO monitoramento (data, descricao, status, numero_de_dias) "
                "VALUES (%s, %s, %s, %s)"
            )
            params = (data, descricao, status, numero_de_dias)
            if self.connection.execute_query(query, params):
                print(f"Registro '{status}' salvo com sucesso.")
                result = self.connection.execute_read_query("SELECT MAX(id_monitoramento) FROM monitoramento")
                return result[0][0] if result else False
            else:
                print(f"Erro ao salvar registro '{status}'.")
                return False
        except Exception as e:
            print(f"Erro ao salvar monitoramento sem atualização: {e}")
            return False

    def _salvarAtualizacao(self, status, texto, dados):
        """
        Salva um registro de atualização no banco de dados.
        """
        try:
            data = time.strftime('%Y-%m-%d %H:%M:%S')
            query = "INSERT INTO atualizacao (status, data, texto) VALUES (%s, %s, %s)"
            values = (status, data, texto)
            
            if self.connection.execute_query(query, values):
                print(f"Registro '{status}' salvo com sucesso.")
                
                result = self.connection.execute_read_query("SELECT MAX(id) FROM atualizacao")
                id_atualizacao = result[0][0] if result else False

                if id_atualizacao:
                    menor_dias = min([dado['num_dias'] for dado in dados])
                    id_monitoramento = self._salvarMonitoramento(status, texto, menor_dias, id_atualizacao) 
                    if dados:
                        for dado in dados:
                            self._salvarFilial(dados=dado, id_monitoramento=id_monitoramento, id_atualizacao=id_atualizacao)
                    
                    return True
                else:
                    print(f"Erro ao obter ID da atualização.")
                    return False
            else:
                print(f"Erro ao salvar registro '{status}'.")
                return False
        except Exception as e:
            print(f"Erro ao salvar atualização: {e}")
            return False

    def salvar(self, texto, status, flag, dados=None):
        """
        Salva o texto com base no status fornecido e em uma flag indicando o tipo de operação.
        """
        if flag == True:
            if status in ["SUCCESS", "ERROR", "WARNING"]:
                return self._salvarAtualizacao(status, texto, dados)
            else:
                print("Status inválido")
                return False
        else:
            if dados:
                menor_dias = min([dado['num_dias'] for dado in dados])
                id_monitoramento = self._salvarMonitoramentoSemAtualizacao(status=status, descricao=texto, numero_de_dias=menor_dias)
                if id_monitoramento:
                    for dado in dados:
                        self._salvarFilial(dados=dado, id_monitoramento=id_monitoramento, id_atualizacao=None)
                    return True
                else:
                    print("Erro ao salvar monitoramento sem atualização.")
                    return False
            else:
                print("Dados inválidos")
                return False

'''
### Exemplo 1: Conexão e Salvamento Simples de Atualização
```python
# Definindo os parâmetros do banco de dados
banco = {
    "host": "localhost",
    "database": "meu_banco",
    "user": "usuario",
    "password": "senha"
}

# Criando uma instância da classe SalvaDados
salva_dados = SalvaDados(banco)

# Dados de exemplo para filiais
dados_filiais = [
    {"filial": "001", "nome": "Filial A", "descricao": "Descrição A", "num_dias": 10},
    {"filial": "002", "nome": "Filial B", "descricao": "Descrição B", "num_dias": 5}
]

# Salvando uma atualização de sucesso com dados de filiais
salva_dados.salvar("Atualização concluída com sucesso.", "SUCCESS", True, dados_filiais)

# Encerrando a conexão (automaticamente chamada ao final do script ou manualmente)
del salva_dados
```

### Exemplo 2: Salvamento de Erro sem Dados de Filiais
```python
# Criando uma instância da classe SalvaDados
salva_dados = SalvaDados(banco)

# Salvando uma mensagem de erro sem dados de filiais
salva_dados.salvar("Erro durante o processo.", "ERROR", True)

# Encerrando a conexão
del salva_dados
```

### Exemplo 3: Salvamento de Monitoramento Sem Atualização
```python
# Criando uma instância da classe SalvaDados
salva_dados = SalvaDados(banco)

# Salvando um monitoramento sem associar uma atualização, com dados de filiais
dados_filiais = [
    {"filial": "003", "nome": "Filial C", "descricao": "Descrição C", "num_dias": 8}
]

# Note que flag é False, pois não há atualização associada
salva_dados.salvar("Monitoramento de rotina.", "WARNING", False, dados_filiais)

# Encerrando a conexão
del salva_dados
```

### Exemplo 4: Tratamento de Status Inválido
```python
# Criando uma instância da classe SalvaDados
salva_dados = SalvaDados(banco)

# Tentando salvar com um status inválido
resultado = salva_dados.salvar("Texto de exemplo.", "INVALID_STATUS", True)

# Verificando o resultado
if not resultado:
    print("Falha ao salvar devido a status inválido.")

# Encerrando a conexão
del salva_dados
```

### Exemplo 5: Salvamento com Dados Inválidos
```python
# Criando uma instância da classe SalvaDados
salva_dados = SalvaDados(banco)

# Tentando salvar sem fornecer dados de filiais quando necessário
resultado = salva_dados.salvar("Monitoramento sem dados.", "SUCCESS", False)

# Verificando o resultado
if not resultado:
    print("Falha ao salvar devido a dados inválidos.")

# Encerrando a conexão
del salva_dados
```

### Notas:
- Certifique-se de que a classe `Connection` e seu método `execute_query` estejam implementados corretamente no módulo `modules.connection.connection`.
- A classe `SalvaDados` foi projetada para ser usada em um ambiente onde a conexão com o banco de dados é necessária. Certifique-se de que os parâmetros de conexão estejam corretos.
- O método `__del__` garante que a conexão com o banco de dados seja fechada adequadamente quando a instância da classe `SalvaDados` for destruída ou explicitamente chamada com `del`.

Esses exemplos demonstram como criar instâncias da classe, salvar dados de diferentes tipos, tratar erros e encerrar a conexão de forma apropriada.
'''