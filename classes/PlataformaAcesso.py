# Essa classe deve ter os seguintes métodos:
# init
# del
# faz login:  recebe login e senha e coloca no navegador
# fecha navegador
# barra de pesquisa: recebe um xpath da barra de pesquisa e um texto e coloca no xpath o texto
# clica em botão:  recebe um xpath e clica no botão "Esse método deve ser responsável por clicar em um botão de uma página web."
# atualiza licença: recebe um xpath e clica no botão de atualizar licença
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class PlataformaAcesso:

    def __init__(self,user, password, url):
        self.user = user
        self.password = password
        self.url = url
        self.driver = webdriver.Chrome()

    def faz_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "USUARIO")))
        self.driver.find_element(By.ID, "USUARIO").send_keys(self.user)
        self.driver.find_element(By.ID, "SENHA").send_keys(self.password)
        
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/form/div[2]/div[1]/input")))
        login_button.click();


    def fecha_navegador(self):
        self.driver.quit()



'''
Exemlo de uso da classe PlataformaAcesso
from classes.PlataformaAcesso import PlataformaAcesso

def main():
    try:
        user
        password
        url
        plataforma = PlataformaAcesso(user, password, url)
        plataforma.faz_login()
        plataforma.fecha_navegador()
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False
    

'''