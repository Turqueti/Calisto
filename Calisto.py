from selenium import webdriver
from selenium.webdriver.support import expected_conditions as WebDriverEC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from secret import user, password
import re
import Aula as AulaClasse
from Horario import Horario
from csvHandler import csvAula

urlBase = 'https://uspdigital.usp.br/jupiterweb/'

class JupiterBot():
    
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        #abre o jupiter
        self.driver.get(urlBase)

        #Procura e clicka na opcao de login
        self.findWaitClick('/html/body/div[1]/div[2]/ul[2]/li[2]/a')
        #Procura o campo usuario e preenche com o usuario(nusp) Definido no arquivo secret.py
        self.findWaitSendKeys('/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td[2]/input',user)
        #Procura o campo senha e preenche com a senha Definida em secret.py
        self.findWaitSendKeys('/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td[2]/input',password)
        #Procura o botao de login e clicka nele
        self.findWaitClick('/html/body/div[1]/div[3]/form/table/tbody/tr[3]/td[2]/input[1]')
        #espera dois segundos para que os pop-ups sumam da tela
        sleep(2)

    #move o scraper p/  a pagina de Grade do Usuario
    def goToGrade(self):

        self.findWaitClick('/html/body/div/div[2]/ul[2]/li[3]/a')
        self.findWaitClick("//*[@id='codpgm']/option[@value='1']")        
        self.findWaitClick('//*[@id="buscar"]')

    #Facilitador que espera o elemento ser clickavel e executa o click
    def findWaitClick(self, Xpath):
        wait = WebDriverWait(self.driver,10)
        btn = wait.until(WebDriverEC.element_to_be_clickable((By.XPATH,Xpath)))
        btn.click()
    
    #Facilitador que espera o elemento de input ser clickavel e insere a info no campo
    def findWaitSendKeys(self,Xpath, key):
        
        wait = WebDriverWait(self.driver,10)
        btn = wait.until(WebDriverEC.element_to_be_clickable((By.XPATH,Xpath)))
        btn.send_keys(key)


class Parser(JupiterBot):
    XpathAulas = []
    Aulas = []
    
    def __init__(self):
        super().__init__()

    def getAulas(self):
        while self.XpathAulas == []:
            self.XpathAulas = self.driver.find_elements_by_xpath('//td[@title]')
        
        
        self.XpathAulas = self.limpaResultadoHorarios(self.XpathAulas)
        self.XpathAulas = self.limpaResultadoDuplicatas(self.XpathAulas)

        for xpathAula in self.XpathAulas:
            self.Aulas.append(self.getAulaInfo(xpathAula))
        
        return self.Aulas

    # essa func tira os horarios da lista de XpathAulas
    def limpaResultadoHorarios(self,XpathAulas):
        regex = re.compile('\\d\\d:\\d\\d')
        XpathAulasAtt = []

        for aula in XpathAulas:
            if not (regex.match(aula.text)):
                XpathAulasAtt.append(aula)

        return XpathAulasAtt            

    # verifica se o Xpath da aula clickada ja foi inserido na lista de Xpaths caso não insere a aula na lista    
    def limpaResultadoDuplicatas(self, XpathAulas):
        XpathAulasAtt = []
        for aula in XpathAulas:
            if not self.aulaNaLista(aula,XpathAulasAtt):
                XpathAulasAtt.append(aula)
        return XpathAulasAtt

    def printAulasDebug(self):
        for aula in self.XpathAulas:
            print(aula.text)
            pass
        pass        
    
    #facilitador para func limpaResultadoDuplicatas
    def aulaNaLista(self, aula, XpathAulasAtt):
        for aulita in XpathAulasAtt:
            if aulita.text == aula.text:
                return True
        
        return False
    
    #clicka na na aula e faz o scrapping das infos
    def getAulaInfo(self, xpathAula):        
        while True:
            try:
                xpathAula.click()
                break
            except:
                #inserir throw de execao
                pass
        
        btnOferecimento = self.driver.find_element_by_xpath("//a[contains(@href,'div_oferecimento')]")
        
        while True:
            try:
                btnOferecimento.click()
                break
            except:
                # add throw
                pass

        Aula = AulaClasse.Aula()
        while Aula.codDisciplina == '' or Aula.nomeDisciplina == '':
            Aula.codDisciplina =  self.driver.find_elements_by_xpath("//p[starts-with(@class,'cabecalho')]/span[contains(@class,'coddis')]")[1].text
            Aula.nomeDisciplina = self.driver.find_elements_by_xpath("//p[starts-with(@class,'cabecalho')]/span[contains(@class,'nomdis')]")[1].text

    
        rowsTabelaInfos = []
        while rowsTabelaInfos == []:
            rowsTabelaInfos = self.driver.find_elements_by_xpath("//div[contains(@class,'adicionado')]/table[1]/tbody/tr")

        Aula.codTurma = rowsTabelaInfos[0].find_elements_by_tag_name('td')[1].text
        Aula.DiaInicio = rowsTabelaInfos[1].find_elements_by_tag_name('td')[1].text
        Aula.DiaFim = rowsTabelaInfos[2].find_elements_by_tag_name('td')[1].text
        Aula.TipoDaTurma = rowsTabelaInfos[3].find_elements_by_tag_name('td')[1].text
        Aula.Observacoes = rowsTabelaInfos[5].find_elements_by_tag_name('td')[1].text

        Aula.horarios = self.getHorarios()

        return Aula

    def getHorario(self, xpathHorario):
        horario = Horario()
        infos = xpathHorario.find_elements_by_tag_name('td')
        horario.diaSemana = infos[0].text
        horario.HrInicio = infos[1].text
        horario.HrFim = infos[2].text
        horario.Prof = infos[3].text

        return horario

    def getHorarios(self):
        horarios = []
        
        xpathHorarios = self.driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr/td/div/div[2]/div[3]/table[2]/tbody/tr")
        
        for horario in xpathHorarios:
            horarios.append(self.getHorario(horario))
        
        return horarios


def csvPrint(aulas):
    print("Subject,Start Date,Start Time,End Date,End Time,Description")
    for aula in aulas:
        csvAula(aula)


parser = Parser()

parser.login()
parser.goToGrade()
parser.getAulas()
parser.driver.close()

csvPrint(parser.Aulas)
