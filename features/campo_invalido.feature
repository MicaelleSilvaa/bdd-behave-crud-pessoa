Feature: Validação de CPF inválido

  Scenario: Inserir um CPF inválido no formulário de cadastro
    Given que estou na página de cadastro
    When eu preencho o campo "Nome" com "Mariah"
    And eu preencho o campo "Sobrenome" com "Silva"
    And eu preencho o campo "CPF" com "12345678900"
    And eu preencho o campo "Data Nascimento" com "1990-01-01"
    And eu submeto o formulário
    Then devo ver a mensagem de erro "O CPF informado é inválido."
