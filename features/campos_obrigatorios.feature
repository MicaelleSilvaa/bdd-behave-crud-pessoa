Feature: Cadastro de Pessoa - Validação de Campos Obrigatórios

  Scenario: Tentativa de cadastrar uma pessoa sem preencher campos obrigatórios
    Given que estou na página de cadastro de pessoa
    When tento cadastrar uma pessoa sem preencher nenhum campo
    Then devo ver mensagens de erro para os campos obrigatórios:
      | nome         |
      | sobrenome    |
      | cpf válido   |
      | data nasc.   |
