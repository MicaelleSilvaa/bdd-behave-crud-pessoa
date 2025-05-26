Feature: Remoção de Pessoa

  Scenario: Remover uma pessoa existente
    Given que estou na página de listagem
    When eu clico no botão de remover da pessoa "Mariana"
    Then eu devo ver a mensagem "Pessoa removida com sucesso"
    And a lista não deve conter o nome "Mariana"
