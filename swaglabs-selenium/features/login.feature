Feature: Login


@SuccessfulLogin
Scenario: El usuario hace login exitoso
    Given que el usuario se dirige a la pagina de SwagLabs
    #And el usuario no está logueado
    When el usuario ingresa su usuario y contraseña
    And efectúa el login exitoso
    #Then se muestra la lista de productos de forma exitosa
