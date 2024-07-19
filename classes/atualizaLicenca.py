from classes.PlataformaAcesso import PlataformaAcesso
from classes.SalvaDados import SalvaDados
from modules.config.ConfigHandler import ConfigHandler
from modules.criptografia.encripta import Criptografia

class AtualizaLicenca:

    #region Construtores
    def __init__(self, licenca):
        self.licenca = licenca
        self.config = self._load_config("config/configHomolog.json")
        self.criptografia = Criptografia()
        self.banco = self._setup_banco() if self.config else None
        self.user = self._setup_user() if self.config else None
        self.plataforma = self._setup_plataforma() if self.user else None

    def _load_config(self, config_path):
        try:
            return ConfigHandler(config_path)
        except Exception as e:
            print(f"Erro ao carregar configurações: {e}")
            return None

    def _decrypt_password(self, password):
        return self.criptografia.desencriptar(password) if password else None

    def _setup_banco(self):
        banco = self.config.get_data("banco de dados")
        if not banco or "password" not in banco:
            print("Erro ao obter dados do banco de dados")
            return None
        banco["password"] = self._decrypt_password(banco["password"])
        return banco

    def _setup_user(self):
        user = self.config.get_data("zantus_user")
        if not user or "password" not in user:
            print("Erro ao obter dados do usuário")
            return None
        user["password"] = self._decrypt_password(user["password"])
        return user

    def _setup_plataforma(self):
        site = self.config.get_data("url_manager")
        if not site or "url" not in site:
            print("Erro ao obter URL do site")
            return None
        return PlataformaAcesso(self.user["username"], self.user["password"], site["url"])
    #endregion

    #region Métodos Públicos
    def atualiza_licenca(self):
        if not self.plataforma:
            print("Erro ao acessar plataforma")
            return False
        try:
            self.plataforma.faz_login()
            self.plataforma.atualiza_licenca()
            self.plataforma.fecha_navegador()
            return True
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
    #endregion