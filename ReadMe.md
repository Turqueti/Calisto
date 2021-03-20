# Calisto JupiterWeb Web Scrapper


## Descrição
Calisto é um projeto inicialmente pessoal, ela é um scrapper do jupiterweb, que tem como objetivo retirar as informações de horário das aulas do site e gerar um csv que seja "importavel" para o google calendar

## Funcionamento e dependências
Para usar a ferramenta o usuário deve baixar o webdriver do selenium para o seu navegador e na pasta do arquivo criar um arquivo secret.py com a seguinte formatação(ver tópico próximos passos): 

```Python
user = '' #Nusp do usuário
password = ''#Senha de acesso ao jupiterweb
```
lembrando que, em nenhum momento a ferramenta grava ou envia as credenciais do usuário para nenhum serviço a não ser o próprio jupiterweb

Calsito usa:
 * selenium: para fazer as funcionalidades de entrar no jupiter e retirar os conteudos
 * a função sleep da biblioteca time: para esperar que alguns elemenos da página carreguem
 * a biblioteca re: para fazer uma comparação de regex na hora de buscar os horários




## Próximos Passos
 * Refatorar o código para cumprir as boas praticas de POO(principalmente em tratamento de erros)
 * Criar um instalador com as dependências
 * Criar uma GUI

## Hábilidades treinadas/desenvolvidas
* familiaridade com a ferramenta selenium
* regex python
* POO(Clases)