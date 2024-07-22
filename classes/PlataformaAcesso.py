
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver




class PlataformaAcesso:

#region Construtores
    def __init__(self,user, password, url):
        self.user = user
        self.password = password
        self.url = url
        # self.soup = self._inicializa_soup()
        self.driver = webdriver.Chrome()
#endregion
    # def _inicializa_soup(self):
    #     url = self.driver.current_url
    #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    #     page = requests.get(url, headers=headers)
    #     soup = BeautifulSoup(page.content, 'html.parser')
    #     return soup, page
#region Métodos Públicos
    def faz_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "USUARIO")))
        self.driver.find_element(By.ID, "USUARIO").send_keys(self.user)
        self.driver.find_element(By.ID, "SENHA").send_keys(self.password)
        
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/form/div[2]/div[1]/input")))
        login_button.click();

    def barra_de_pesquisa(self, texto,input_id = None, xpath=None):
        # Administração de licenças
        # menu-search
        # //*[@id="MP_4_480"]
        # /html/body/div[1]/aside/div/section/ul/li[5]/ul/li[4]/a
        wait = WebDriverWait(self.driver, 10)
        if input_id:
            input = wait.until(EC.element_to_be_clickable((By.ID, input_id)))
        elif xpath:
            input = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input.clear()
        input.send_keys(texto)


    def clica_em_botao(self, xpath=None, button_id=None):
        # /html/body/div[1]/aside/div/section/ul/li[5]/ul/li[4] item da lista referencia a Administração de licenças
        wait = WebDriverWait(self.driver, 10)
        if xpath:
            button = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            button.click()
        elif button_id:
            button = wait.until(EC.visibility_of_element_located((By.ID, button_id)))
            button.click()

    def scroll(self):
        wait = WebDriverWait(self.driver, 10)
        # scrolla ate o final da pagina
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # espera 5 segundos e scrolla para o topo da pagina
        self.driver.execute_script("window.scrollTo(0, 0);")
    

    
    
    def trata_popup(self, element_id=None, xpath=None):
        wait = WebDriverWait(self.driver, 30)
        if xpath:
            texto = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            print(texto.text)
            self.clica_em_botao(xpath="/html/body/div[5]/div[7]/div/button")
            return texto.text

        elif element_id:
            texto = wait.until(EC.visibility_of_element_located((By.ID, element_id)))
            # verifica se a mensagem de erro esta na tela
            print(texto.text)
            self.clica_em_botao(xpath="/html/body/div[5]/div[7]/div/button")
            return texto.text
    
    def fecha_navegador(self):
        self.driver.quit()

#endregion
# destrutor

#region Destrutores
    def __del__(self):
        self.driver.quit()
        print("Objeto destruido")

#endregion



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