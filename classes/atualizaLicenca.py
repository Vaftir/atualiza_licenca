from classes.PlataformaAcesso import PlataformaAcesso
from classes.SalvaDados import SalvaDados
from modules.config.ConfigHandler import ConfigHandler
from modules.criptografia.encripta import Criptografia

import time
"""
Essa classe é responsável por atualizar a licença, ela depende das classes PlataformaAcesso e SalvaDados
alem de depender ds modulos ConfigHandler e Criptografia
Atributos:
    config: ConfigHandler
    criptografia: Criptografia
    banco: dict
    user: dict
    salva_dados: SalvaDados
    plataforma: PlataformaAcesso
Métodos:
    _load_config: ConfigHandler
    _decrypt_password: str
    _setup_banco: dict
    _setup_user: dict
    _setup_plataforma: PlataformaAcesso
    verifica_retorno: None
    atualiza_licenca: bool
    __del__: None
dependencias:
    ConfigHandler
    Criptografia
    PlataformaAcesso
    SalvaDados
    time

"""
class AtualizaLicenca:

#region Construtores
    def __init__(self):
        self.config = self._load_config("config/config.json")
        self.criptografia = Criptografia()
        self.banco = self._setup_banco() if self.config else None
        self.user = self._setup_user() if self.config else None
        self.salva_dados = SalvaDados(self.banco) if self.banco else None
        self.plataforma = self._setup_plataforma() if self.user else None

    


    def _load_config(self, config_path):
        # Carrega as configurações do arquivo de configuração
        try:
            return ConfigHandler(config_path)
        except Exception as e:
            print(f"Erro ao carregar configurações: {e}")
            return None

    def _decrypt_password(self, password):
        # Desencripta a senha se ela existir
        return self.criptografia.desencriptar(password) if password else None

    def _setup_banco(self):
        # Obtém os dados do banco de dados do arquivo de configuração
        banco = self.config.get_data("banco de dados")
        if not banco or "password" not in banco:
            print("Erro ao obter dados do banco de dados")
            return None
        banco["password"] = self._decrypt_password(banco["password"])
        return banco

    def _setup_user(self):
        # Obtém os dados do usuário do arquivo de configuração
        user = self.config.get_data("zantus_user")
        if not user or "password" not in user:
            print("Erro ao obter dados do usuário")
            return None
        user["password"] = self._decrypt_password(user["password"])
        return user

    def _setup_plataforma(self):
        # Obtém a URL da plataforma de acesso do arquivo de configuração
        site = self.config.get_data("url_manager")
        if not site or "url" not in site:
            print("Erro ao obter URL do site")
            return None
        return PlataformaAcesso(self.user["username"], self.user["password"], site["url"])
    
    def _pega_numaronumero_de_dias(self, dados):
        dias = self.config.get_data("numero_minimo_de_dias")
        if not dias:
            print("Erro ao obter o número mínimo de dias")
            return None
        return dias
#endregion

#region Métodos Privados
    def verifica_retorno(self, resultado, dados = None):

        '''
        Método que verifica o retorno da atualização da licença e salva os dados no banco

        '''
        # Dicionário que mapeia mensagens específicas a seus respectivos status
        mensagens = {
            "Para que as atualizações entrem em vigor, é necessário refazer o login": "SUCCESS",
            "Licença atualizada com restrições": "WARNING"
        }

        encontrou_mensagem = False  # Flag para verificar se alguma mensagem conhecida foi encontrada

        # Itera sobre cada par (mensagem, status) no dicionário
        for mensagem, status in mensagens.items():
            # Se a mensagem atual está presente no resultado
            if mensagem in resultado:
                self.salva_dados.salvar(texto=resultado, status=status,flag=True, dados= dados)  # Salva o resultado com o status correspondente
                encontrou_mensagem = True  # Marca que encontramos pelo menos uma mensagem
                break

        # Se nenhuma mensagem conhecida foi encontrada no resultado
        if not encontrou_mensagem:
            self.salva_dados.salvar(texto=resultado, status="ERROR", flag=True, dados= dados)  # Salva o resultado com o status "ERROR"

#endregion

#region Métodos Públicos
    def atualiza_licenca(self, dados = None):
        '''
        Método que realiza a atualização da licença
        Retorna True se a atualização foi bem-sucedida, False caso contrário
        '''
        if not self.plataforma:
            print("Erro ao acessar plataforma")
            return False
        try:
            # self.plataforma.faz_login()
            # self.plataforma.barra_de_pesquisa(texto="Administração de licenças", input_id="menu-search")
            # self.plataforma.clica_em_botao(xpath="/html/body/div[1]/aside/div/section/ul/li[5]/ul/li[4]")
            self.plataforma.clica_em_botao(button_id="BTN_LICENCA_UPDATE_MANAGER")
            resultado = self.plataforma.trata_popup(element_id="alert_message_internal")
            self.verifica_retorno(resultado, dados)
            self.plataforma.scroll()
            # self.plataforma.atualiza_licenca()
            self.plataforma.fecha_navegador()
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
#endregion


#region destructors
    def __del__(self):
        if self.banco:
            self.banco = None
        if self.config:
            self.config = None
        if self.criptografia:
            self.criptografia = None
        if self.user:
            self.user = None
        print("Objeto de atualização de licença destruído")
        
        
#endregion