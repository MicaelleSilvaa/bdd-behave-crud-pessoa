from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('que estou na página de listagem de pessoas')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/listar")

@given('cadastro uma nova pessoa chamada "{nome_base}"')
def step_impl(context, nome_base):
    context.driver.get("http://localhost:5000/cadastrar")

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "nome"))
    )
    
    nome_unico = f"{nome_base}_{int(time.time())}"
    sobrenome = "Teste"
    cpf = f"70183270401{int(time.time()) % 10}"
    data_nasc = "2000-01-01"

    context.driver.find_element(By.ID, "nome").send_keys(nome_unico)
    context.driver.find_element(By.ID, "sobrenome").send_keys(sobrenome)
    context.driver.find_element(By.ID, "cpf").send_keys(cpf)
    context.driver.find_element(By.ID, "data_nascimento").send_keys(data_nasc)
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    context.nome_cadastrado = nome_unico

@when('eu clico no botão de editar da pessoa recém cadastrada')
def step_impl(context):
    context.driver.get("http://localhost:5000/listar")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    linhas = context.driver.find_elements(By.TAG_NAME, "tr")
    for linha in linhas:
        if context.nome_cadastrado in linha.text:
            botao_editar = linha.find_element(By.CLASS_NAME, "btn-warning")
            botao_editar.click()
            break

@when('eu altero o campo nome para "{novo_nome}"')
def step_impl(context, novo_nome):
    campo_nome = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "nome"))
    )
    campo_nome.clear()

    nome_editado = f"{novo_nome}_{int(time.time())}"
    campo_nome.send_keys(nome_editado)
    context.nome_editado = nome_editado

    campo_sobrenome = context.driver.find_element(By.ID, "sobrenome")
    campo_sobrenome.clear()
    sobrenome_editado = "SobrenomeEditado"
    campo_sobrenome.send_keys(sobrenome_editado)
    context.sobrenome_editado = sobrenome_editado

    campo_cpf = context.driver.find_element(By.ID, "cpf")
    campo_cpf.clear()
    campo_cpf.send_keys("13037116480")
    context.cpf_editado = "13037116480"

    campo_data_nascimento = context.driver.find_element(By.ID, "data_nascimento")
    campo_data_nascimento.clear()
    data_nasc_editada = "1995-12-31"
    campo_data_nascimento.send_keys(data_nasc_editada)
    context.data_nasc_editada = data_nasc_editada


@when('eu clico no botão de salvar alterações')
def step_impl(context):
    botao_salvar = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    botao_salvar.click()

@then('eu devo ver a pessoa editada na lista')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    corpo_tabela = context.driver.find_element(By.TAG_NAME, "tbody")
    assert context.nome_editado in corpo_tabela.text

@then('eu removo a pessoa editada')
def step_impl(context):
    context.driver.get("http://localhost:5000/listar")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    linhas = context.driver.find_elements(By.TAG_NAME, "tr")
    for linha in linhas:
        if context.nome_editado in linha.text:
            botao_remover = linha.find_element(By.CLASS_NAME, "btn-danger")
            botao_remover.click()
            break
