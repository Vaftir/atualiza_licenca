from modules.config.ConfigHandler import ConfigHandler
from modules.criptografia.encripta import Criptografia
from modules.connection.connection import Connection
from classes.PlataformaAcesso import PlataformaAcesso

import time
def main():

    try:
        # Cria uma instância da classe Licenca
        config = ConfigHandler("config/configHomolog.json")
        criptografia = Criptografia()
        
        site = config.get_data("url_manager")

        user = config.get_data("zantus_user")
        banco = config.get_data("banco de dados")
        
        banco["password"] = criptografia.desencriptar(banco["password"])
        user["password"] = criptografia.desencriptar(user["password"])

        plataforma = PlataformaAcesso(user["username"], user["password"], site["url"])
        plataforma.faz_login()

        
        # espera 25 segundos usando uma função time
        time.sleep(25)


        # conexao = Connection(banco["host"], banco["database"], banco["user"], banco["password"])
        # conexao.connect()




      
        
        # user2 = user["password"]
        # banco2 = banco["password"]

        # banco["password"] = encripta.desencriptar(banco2)
        # user["password"] = encripta.desencriptar(user2)

        
        # print(user)
        # print(banco)
        
        



 

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False
    

if __name__ == "__main__":
    main()