from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('que estou na página de listagem')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/listar")

@when('eu clico no botão de remover da pessoa "{nome}"')
def step_impl(context, nome):
    time.sleep(1)
    rows = context.driver.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        if nome in row.text:
            row.find_element(By.LINK_TEXT, "Remover").click()
            break

@then('eu devo ver a mensagem "Pessoa removida com sucesso"')
def step_impl(context):
    time.sleep(1)
    body_text = context.driver.page_source
    assert "Pessoa removida com sucesso" in body_text

@then('a lista não deve conter o nome "{nome}"')
def step_impl(context, nome):
    context.driver.get("http://localhost:5000/listar")
    time.sleep(1)
    assert nome not in context.driver.page_source
    context.driver.quit()
