Feature: Cadastro de Pessoa - Validação de Campos Obrigatórios

  Scenario: Tentar cadastrar uma pessoa sem preencher os campos obrigatórios
    Given que estou na página de cadastro de pessoa
    When tento cadastrar uma pessoa sem preencher nenhum campo
    Then devo ver mensagens de erro para os campos obrigatórios:
      | Nome       |
      | Sobrenome  |
      | CPF válido |
      | Data Nasc. |
