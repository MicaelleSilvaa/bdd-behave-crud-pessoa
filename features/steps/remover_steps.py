from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def criar_pessoa(driver, nome_base):
    driver.get("http://localhost:5000/cadastrar")
    time.sleep(1)

    nome_unico = f"{nome_base}_{int(time.time())}"
    sobrenome = "Teste"
    cpf = f"13037116480{int(time.time()) % 10}"
    data_nasc = "2000-01-01"

    driver.find_element(By.ID, "nome").send_keys(nome_unico)
    driver.find_element(By.ID, "sobrenome").send_keys(sobrenome)
    driver.find_element(By.ID, "cpf").send_keys(cpf)
    driver.find_element(By.ID, "data_nascimento").send_keys(data_nasc)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)

    return nome_unico

@given('que estou na página de listagem')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/listar")

@when('eu crio e depois clico no botão de remover da pessoa')
def step_impl(context):
    # Criar pessoa
    nome_criado = criar_pessoa(context.driver, "PessoaRemover")
    context.nome_criado = nome_criado

    # Voltar para listagem
    context.driver.get("http://localhost:5000/listar")
    time.sleep(1)

    # Procurar e remover a pessoa criada
    rows = context.driver.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        if nome_criado in row.text:
            row.find_element(By.LINK_TEXT, "Remover").click()
            break

@then('eu devo ver a mensagem "Pessoa removida com sucesso"')
def step_impl(context):
    time.sleep(1)
    body_text = context.driver.page_source
    assert "Pessoa removida com sucesso" in body_text

@then('a lista não deve conter o nome da pessoa removida')
def step_impl(context):
    context.driver.get("http://localhost:5000/listar")
    time.sleep(1)
    assert context.nome_criado not in context.driver.page_source
    context.driver.quit()
