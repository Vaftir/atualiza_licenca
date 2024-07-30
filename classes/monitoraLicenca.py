# Autor: Yago Assis Mendes Faria
from classes.atualizaLicenca import AtualizaLicenca
from modules.config.ConfigHandler import ConfigHandler
import datetime


'''
Essa classe é responsável por monitorar a licença de um sistema
ela depende da classe AtualizaLicenca para atualizar a licença


Atributos:
    licenca_atualizada: bool
    data_atualizacao: datetime.datetime
    superclasse: AtualizaLicenca
metodos:
    _verifica_licencas: bool
    _salva_dados: None
    monitora_licenca: None
dependencias:
    AtualizaLicenca
    datetime

'''
class MonitoraLicenca(AtualizaLicenca):
    
    def __init__(self):
        super().__init__()  # Chama o construtor da classe pai (AtualizaLicenca)
        self.dias = self._pega_numaronumero_de_dias(self.config)
        self.licenca_atualizada = False
        self.data_atualizacao = datetime.datetime.now()
        

#region Métodos Privados
 
    def _verifica_licencas(self, dados):
        # Método para verificar se há alguma licença com 16 dias nos dados extraídos
        # Itera sobre cada dicionário de dados passado como argumento
        for dado in dados:
            # Verifica se a chave 'licenca' no dicionário atual é igual a '16 dias'
            if dado['num_dias'] <= self.dias:
                # Se encontrar uma licença com 16 dias, marca a flag licenca_atualizada como False e retorna
                
                return False

        # Armazena a data e hora da última verificação
        self.data_atualizacao = datetime.datetime.now()


        return True
    
    def _salva_dados(self, dados):
        self.salva_dados.salvar(texto="Monitoramento sem atualização realizado com sucesso", status="SUCCESS", flag=False, dados=dados)
               
#endregion

#region Métodos Públicos

    def monitora_licenca(self):
        tr_xpath = '//tr[contains(@class, "even") or contains(@class, "odd") and not(contains(@style, "display: none"))]'
        td1_xpath = './td[1]'
        tds_xpath = './td[1] | ./td[2] | ./td[7]'
        
        if not self.plataforma:
            print("Erro ao obter dados da plataforma")
            return
        try:
            self.plataforma.faz_login()
            self.plataforma.barra_de_pesquisa(texto="Administração de licenças", input_id="menu-search")
            self.plataforma.clica_em_botao(xpath="/html/body/div[1]/aside/div/section/ul/li[5]/ul/li[4]")
            self.plataforma.scroll()
            dados = self.plataforma.extrai_dados(tr_xpath=tr_xpath, td1_xpath=td1_xpath, tds_xpath=tds_xpath)
            licenca = self._verifica_licencas(dados)
            if licenca:
                self.licenca_atualizada = True
                self._salva_dados(dados)
            else:
                self.licenca_atualizada = False
                super().atualiza_licenca(dados = dados)
           
        except Exception as e:
            print(f"Erro ao monitorar licença: {e}")
            self.licenca_atualizada = False
            self.data_atualizacao = datetime.datetime.now()
#endregion



'''
 def extrai_dados(self):
        dados = []
        trs = self.driver.find_elements(By.XPATH, '//tr[contains(@class, "even") or contains(@class, "odd") and not(contains(@style, "display: none"))]')
        for tr in trs:
            td1 = tr.find_element(By.XPATH, './td[1]')
            if td1.text == '2':
                continue
            else:
                tds = tr.find_elements(By.XPATH, './td[1] | ./td[2] | ./td[7]')
                dicionario = {
                    'filial': tds[0].text,
                    'nome': tds[1].text,
                    'licenca': tds[2].text
                }
                dados.append(dicionario)
        
        return dados
'''