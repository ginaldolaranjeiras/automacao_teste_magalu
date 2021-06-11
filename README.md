# Projeto de Automação do Site Magalu

### Este projeto possui uma estrutura simplificada para fins didáticos

## Projeto de Automação de Testes BDD

* Linguagem Python
* Framework BDD Behave
* Selenium
* Allure Framework



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

## Instale o webdriver

Instale a versão do webdriver correspondente ao navegador de teste e compatível com o sistema operacional utilizado

No caso do Chrome, baixar e descompactar o executável do [ChromeDriver](https://chromedriver.chromium.org/home) e salve no diretório do projeto.


# Configurando o Projeto

## Adicionando suporte à escrita do Gherkin(GWT) em português.

Na pasta raíz do projeto, criar um arquivo _behave.ini_ .

Adicionar configuração da linguagem em português para os arquivos .feature no arquivo [_behave.ini_](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/blob/93c683ef1e2503651dee4d722cd46fadf7859f9e/behave.ini).


## Crie um diretório chamado [_features_](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features). 

Escreva os cenários nos arquivos com extensão [_.feature_](features/busca_produto.feature) dentro do diretório [features](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features).

## Crie um diretório chamado [_steps_](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features/steps) dentro do diretório [features](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features).

Crie os arquivos de implementação das [steps](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features/steps) dentro do diretório [features] com a extenção [_.py_](features/steps/busca_produto.py).

## Executando as features com o comando _behave_.

No cmd digite o comando: _behave_ para executar os cenários.

O log dará o modelo das steps não implementadas

![implemente-me](https://user-images.githubusercontent.com/50729163/121734611-6107b900-cacb-11eb-9118-00c0f997d899.jpg)

Copie a implementação no [arquivo .py](features/steps/busca_produto.py) em steps

Implemente os [métodos do Selenium](features/steps/busca_produto.py).

Execute novamente o comando: __behave__

Os testes devem executar com sucesso.

Você pode adicionar Hooks adicionando um arquivo _environment.py_ na pasta [features](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/features).

Você pode aplicar o padrão Page Objects criando [modelos](features/pages/magalu_page.py) e abstraindo os métodos de teste.


# Gerando reports com [Allure Framework](https://docs.qameta.io/allure/)

## *Copyright*
The Allure reference guide is available as HTML documents. The latest copy is available at https://docs.qameta.io/allure/

Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.

## Preparando configuração do Allure Framework

## Instalação do [Java Runtime Environment (JRE)](https://www.java.com/pt-BR/download/manual.jsp).

## Instação do [Open JDK](https://openjdk.java.net/)

Baixe o JDK e descompacte os arquivos dentro do diretório Program Files

É preciso ainda configurar o JAVA_HOME nas variáveis de ambiente do Windows, com o caminho para o diretório do JDK descompactado.

## Instalação do [Allure Framework](https://docs.qameta.io/allure/#_get_started).

Baixe o gerenciador de pacotes [Scoop](https://scoop.sh/)

Intale o Allure executando: _scoop install allure_

## Instale o [allure-behave](https://pypi.org/project/allure-behave/)

No ambiente virtual do seu projeto execute: _pip install allure-behave_


# Gerando reports com  [Allure Framework](https://docs.qameta.io/allure/)

## Execute o behave com allure framework

Execute: _behave -f allure_behave.formatter:AllureFormatter -o report ./features_

Os testes devem sere executados e o resultado salvo na pasta [report](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/report).

## Exiba a página de relatórios

Execute: _allure serve report_

O navegador deve exibir o relatório
![serve-allure](https://user-images.githubusercontent.com/50729163/121743576-ee510a80-cad7-11eb-9ebf-c35b834d8af0.jpg)

A execução é detalhada
![serve-allure-behaviors](https://user-images.githubusercontent.com/50729163/121743615-0032ad80-cad8-11eb-923a-56b4ca9e8fe3.jpg)

## Salve o conteúdo do relatório

É possível salvar o [conteúdo do relatório](https://github.com/ginaldolaranjeiras/automacao_teste_magalu/tree/master/allure-report) executando: allure generate report

