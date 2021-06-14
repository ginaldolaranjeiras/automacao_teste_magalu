from behave import given, when, then
from features.pages import magalu_page
from features.pages.magalu_page import MagaluPage
import time


@given(u'que estou na página de busca')
def step_impl(context):
    context.driver = MagaluPage(
        "drivers\chromedriver.exe"
        )
    context.driver.open_page("https://www.magazineluiza.com.br/busca/panela%20de%20press%C3%A3o/")


@when(u'quando clico no primeiro item')
def step_impl(context):
    context.driver.click_element_class('product-li')


@when(u'clico em adicionar à sacola')
def step_impl(context):
    context.driver.click_element_class(
        'button__buy'
        )  


@then(u'sou direcionado para página do carrinho')
def step_impl(context):
    time.sleep(2)
    context.driver.check_elements('/html/body/div[1]/div/div[1]')


@then(u'o produto está contido no carrinho')
def step_impl(context):
    time.sleep(2)
    context.driver.check_elements('//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]')
   