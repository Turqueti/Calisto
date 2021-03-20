# Calisto JupiterWeb Web Scrapper

## Instalação
Para rodar a Calisto é necessário instalar os seguintes pre-requisitos:
* o navegador [firefox](https://www.mozilla.org/pt-BR/firefox/new/)
* o [geckcodriver](https://github.com/mozilla/geckodriver/releases) responsável por criar uma janela que o robô possa controlar
* o [python3](https://www.python.org/downloads/)
* e o [pip3](https://pip.pypa.io/en/stable/installing/)

Uma vez que as dependências foram instaladas basta clonar o repositório:

```Shell
git clone https://github.com/Turqueti/Calisto.git

```
mudar para a pasta do projeto:

```Shell
cd Calisto
```

E instalar as bibliotecas requeridas:

```Shell
pip3 install -r requirements.txt
```
## Descrição
Calisto é um projeto inicialmente pessoal, ela é um scrapper do jupiterweb, que tem como objetivo retirar as informações de horário das aulas do site e gerar um csv que seja "importavel" para o google calendar

## Funcionamento e dependências
Para usar a ferramenta o usuário deve baixar o webdriver do selenium para o seu navegador e na pasta do arquivo criar um arquivo secret.py com a seguinte formatação(ver tópico próximos passos): 

```Python
user = '' #Nusp do usuário
password = ''#Senha de acesso ao jupiterweb
```
lembrando que, em nenhum momento a ferramenta grava ou envia as credenciais do usuário para nenhum serviço a não ser o próprio jupiterweb


## Próximos Passos
 * Refatorar o código para cumprir as boas praticas de POO(principalmente em tratamento de erros)
 * Criar um instalador com as dependências
 * Criar uma GUI

## Hábilidades treinadas/desenvolvidas
* familiaridade com a ferramenta selenium
* regex python
* POO(Clases)
