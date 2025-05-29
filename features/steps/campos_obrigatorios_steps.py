from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@given('que estou na página de cadastro de pessoa')
def step_impl(context):
    options = Options()
    options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("http://localhost:5000/cadastrar")

@when('tento cadastrar uma pessoa sem preencher nenhum campo')
def step_impl(context):
    botao_cadastrar = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    botao_cadastrar.click()
    time.sleep(1)

from selenium.webdriver.common.by import By

@then('devo ver mensagens de erro para os campos obrigatórios')
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
        assert campo_name is not None, f"Campo '{erro}' não está mapeado."

        campo = context.driver.find_element(By.NAME, campo_name)

        is_valid = context.driver.execute_script("return arguments[0].checkValidity();", campo)

        assert not is_valid, (
            f"O campo '{campo_name}' foi considerado válido, mas deveria estar inválido."
        )

    context.driver.quit()
