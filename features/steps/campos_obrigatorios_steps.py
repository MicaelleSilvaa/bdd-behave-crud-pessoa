from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que estou na página de cadastro de pessoa')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/cadastrar")

@when('tento cadastrar uma pessoa sem preencher nenhum campo')
def step_impl(context):
    botao_cadastrar = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    botao_cadastrar.click()

@then('devo ver mensagens de erro para os campos obrigatórios:')
def step_impl(context):
    nome_para_campo = {
        'nome': 'nome',
        'sobrenome': 'sobrenome',
        'cpf válido': 'cpf',
        'data nasc.': 'data_nascimento',
    }

    erros_esperados = [row[0].strip().lower() for row in context.table]

    for erro in erros_esperados:
        campo_name = nome_para_campo.get(erro)
        assert campo_name is not None, f"Campo '{erro}' não mapeado no teste."

        campo = context.driver.find_element(By.NAME, campo_name)
        valido = context.driver.execute_script("return arguments[0].checkValidity();", campo)
        assert not valido, f"O campo '{campo_name}' foi considerado válido, mas deveria estar inválido."

    context.driver.quit()
