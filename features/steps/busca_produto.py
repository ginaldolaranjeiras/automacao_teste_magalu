from behave import given, when, then
from features.pages import magalu_page
from features.pages.magalu_page import MagaluPage
import time

@given(u'que estou na página inicial do Magalu')
def step_impl(context):
    context.driver = MagaluPage(
        "https://www.magazineluiza.com.br/",
        "drivers\chromedriver.exe"
        )
    context.driver.open_page()



@when(u'digito o termo "panela de pressão"')
def step_impl(context):
    context.driver.fill_search_text(
        "inpHeaderSearch",
        "panela de pressão"
        )


@when(u'clico em Buscar')
def step_impl(context):
    context.driver.search_click(
        "btnHeaderSearch"
        )
    time.sleep(5)


@then(u'sou direcionado para a página de resultados')
def step_impl(context):
    context.driver.check_elements(
        '//*[@id="__next"]/div/div[5]/div/ul'
        )