Feature: Edição de Pessoa

  Scenario: Criar, editar e excluir uma pessoa com sucesso
    Given que estou na página de listagem de pessoas
    And cadastro uma nova pessoa chamada "TesteEditar"
    When eu clico no botão de editar da pessoa recém cadastrada
    And eu altero o campo nome para "TesteEditado"
    And eu clico no botão de salvar alterações
    Then eu devo ver a pessoa editada na lista
    And eu removo a pessoa editada
