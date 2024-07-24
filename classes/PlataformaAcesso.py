
import re
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


#region Métodos Privados
    def _espera_elemento(self, xpath=None, element_id=None):
        wait = WebDriverWait(self.driver, 10)
        if xpath:
            return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        elif element_id:
            return wait.until(EC.presence_of_element_located((By.ID, element_id)))
#endregion

#region Métodos Públicos

    
    def extrai_dados(self, tr_xpath, td1_xpath, tds_xpath):
        # Inicializa uma lista vazia para armazenar os dados extraídos
        dados = []
        
        # Encontra todos os elementos <tr> que correspondem ao XPath fornecido
        trs = self.driver.find_elements(By.XPATH, tr_xpath)
        
        # Itera sobre cada elemento <tr> encontrado
        for tr in trs:
            # Encontra o primeiro <td> dentro do elemento <tr> atual usando o XPath fornecido
            td1 = tr.find_element(By.XPATH, td1_xpath)
            
            # Verifica se '10' não está presente no texto do primeiro <td>
            if '10' not in td1.text:
                continue  # Se '10' não estiver presente, passa para a próxima iteração
            
            # Encontra todos os <td>s desejados dentro do elemento <tr> atual usando o XPath fornecido
            tds = tr.find_elements(By.XPATH, tds_xpath)
            
            # Extrai o texto da terceira coluna <td> que contém informações de licença
            licenca_text = tds[2].text
            
            # Extrai os números da string da licença usando expressões regulares
            # Extrai o número de dias para "Manager"
            manager_dias = int(re.search(r'Manager faltam (\d+) dias', licenca_text).group(1))
            
            # Extrai o número de dias para "PDV"
            pdv_dias = int(re.search(r'PDV faltam (\d+) dias', licenca_text).group(1))
            
            # Encontra o menor valor entre os dias de "Manager" e "PDV"
            menor_dias = min(manager_dias, pdv_dias)
            
            # Cria um dicionário com os dados extraídos e adiciona à lista 'dados'
            dicionario = {
                'filial': tds[0].text,     # Extrai o texto da primeira coluna <td>
                'nome': tds[1].text,       # Extrai o texto da segunda coluna <td>
                'licenca': licenca_text,    # Mantém a string original da licença
                'menor_dias': menor_dias   # Armazena o menor número de dias entre "Manager" e "PDV"
            }
            dados.append(dicionario)
        
        # Retorna a lista de dicionários com os dados extraídos
        return dados
   

    def faz_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self._espera_elemento(element_id="USUARIO").send_keys(self.user)
        self._espera_elemento(element_id="SENHA").send_keys(self.password)

        
        login_button = self._espera_elemento(xpath="/html/body/div[1]/form/div[2]/div[1]/input")
        login_button.click();

    def barra_de_pesquisa(self, texto,input_id = None, xpath=None):
        '''
        texto: Administração de licenças 
        id: menu-search
        xpath1: //*[@id="MP_4_480"]
        xpath que funciona: /html/body/div[1]/aside/div/section/ul/li[5]/ul/li[4]/a
        '''
       
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
            button = self._espera_elemento(xpath=xpath)
            button.click()
        elif button_id:
            button = self._espera_elemento(element_id=button_id)
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
            texto = self._espera_elemento(xpath=xpath)
            print(texto.text)
            self.clica_em_botao(xpath="/html/body/div[5]/div[7]/div/button")
            return texto.text

        elif element_id:
            texto = self._espera_elemento(element_id=element_id)
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