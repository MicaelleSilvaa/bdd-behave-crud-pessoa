Feature: Remoção de Pessoa

  Scenario: Criar e remover uma pessoa
    Given que estou na página de listagem
    When eu crio e depois clico no botão de remover da pessoa
    Then eu devo ver a mensagem "Pessoa removida com sucesso"
    And a lista não deve conter o nome da pessoa removida
