from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('que estou na página de cadastro')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/cadastrar")

@when('eu preencho o formulário com nome "{nome}", sobrenome "{sobrenome}", CPF "{cpf}", data de nascimento "{data}"')
def step_impl(context, nome, sobrenome, cpf, data):
    context.nome_teste = nome
    context.driver.find_element(By.ID, "nome").send_keys(nome)
    context.driver.find_element(By.ID, "sobrenome").send_keys(sobrenome)
    context.driver.find_element(By.ID, "cpf").send_keys(cpf)
    context.driver.find_element(By.ID, "data_nascimento").send_keys(data)

@when('eu clico no botão de cadastrar')
def step_impl(context):
    context.driver.find_element(By.TAG_NAME, "button").click()

@then('eu devo ver a mensagem "Pessoa cadastrada com sucesso"')
def step_impl(context):
    time.sleep(1)
    body_text = context.driver.page_source
    assert "Pessoa cadastrada com sucesso" in body_text

@then('a nova pessoa deve aparecer na lista')
def step_impl(context):
    context.driver.get("http://localhost:5000/listar")
    time.sleep(1)
    body_text = context.driver.page_source
    assert context.nome_teste in body_text

    rows = context.driver.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        if context.nome_teste in row.text:
            try:
                row.find_element(By.LINK_TEXT, "Remover").click()
                time.sleep(1)
            except:
                pass
            break

    context.driver.quit()
