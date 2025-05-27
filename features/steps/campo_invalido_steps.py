from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página de cadastrar')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/cadastrar")  # ajuste para sua URL

@when('eu preencho o campo "Nome" com "{nome}"')
def step_impl(context, nome):
    context.driver.find_element(By.NAME, "nome").send_keys(nome)

@when('eu preencho o campo "Sobrenome" com "{sobrenome}"')
def step_impl(context, sobrenome):
    context.driver.find_element(By.NAME, "sobrenome").send_keys(sobrenome)

@when('eu preencho o campo "CPF" com "{cpf}"')
def step_impl(context, cpf):
    context.driver.find_element(By.NAME, "cpf").send_keys(cpf)

@when('eu preencho o campo "Data Nascimento" com "{data}"')
def step_impl(context, data):
    context.driver.find_element(By.NAME, "data_nascimento").send_keys(data)

@when('eu submeto o formulário')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "form").submit()

@then('devo ver a mensagem de erro "{mensagem_erro}"')
def step_impl(context, mensagem_erro):
    try:
        elemento_erro = WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{mensagem_erro}')]"))
        )
        assert mensagem_erro in elemento_erro.text
    finally:
        context.driver.quit()
