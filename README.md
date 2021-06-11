# Projeto de Automação do Site Magalu


## Projeto de Automação de Testes BDD

* Linguagem Python
* Framework BDD Behave
* Selenium
* Allure Report



# Configurando o ambiente


## Intalação do [Python](https://www.python.org/)

Faça o [download](https://www.python.org/downloads/) do Python 

Verifique a intalação do python no cmd:   *python --version*


## Criação do Diretório para o projeto

Crie um diretório no cmd:   *mkdir nome_do_diretorio*

## Criação de um [ambiente virtual](https://docs.python.org/3/library/venv.html?highlight=venv#module-venv) Python

Crie um ambiente virtual no cmd:  *python -m venv c:\path\to\nome_do_diretorio*

Ative seu ambiente virtual a partir do cmd:  _c:\path\to\nome_do_diretorio> **Scripts\activate.bat**_

## Instale o [Behave](https://behave.readthedocs.io/en/stable/index.html)

No ambiente virtual ativado, através do comando [pip](https://docs.python.org/3/tutorial/venv.html?highlight=pip), pelo cmd: _pip install [behave](https://pypi.org/project/behave/)_

## Instale o [Selenium](https://pypi.org/project/selenium/)

No ambiente virtual ativado, através do comando [pip](https://docs.python.org/3/tutorial/venv.html?highlight=pip), pelo cmd: _pip install selenium_

## Instale o webdriver correspondente ao navegador de teste, compatível com o sistema operacional e com o navegador utilizado

No caso do Chrome, baixar e descompactar o [ChromeDriver](https://chromedriver.chromium.org/home) e salve no diretório do projeto.


# Configurando o Projeto

## Adicionando suporte à escrita do Gherkin(GWT) em português.

Na pasta raíz do projeto, criar um arquivo _behave.ini_ .

Adicionar configuração da linguagem em português para os arquivos .feature no arquivo [_behave.ini_](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/blob/93c683ef1e2503651dee4d722cd46fadf7859f9e/behave.ini).


## Crie um diretório chamado [_features_](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features). 

##Crie um diretório chamado [_steps_](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features/steps) dentro do diretório [features](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features).



