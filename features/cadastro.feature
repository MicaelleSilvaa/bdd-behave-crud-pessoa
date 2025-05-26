Feature: Cadastro de Pessoa

  Scenario: Cadastro bem-sucedido de uma nova pessoa
    Given que estou na página de cadastro
    When eu preencho o formulário com nome "Maria", sobrenome "Silva", CPF "70183270401", data de nascimento "01/01/2000"
    And eu clico no botão de cadastrar
    Then eu devo ver a mensagem "Pessoa cadastrada com sucesso"
    And a nova pessoa deve aparecer na lista
