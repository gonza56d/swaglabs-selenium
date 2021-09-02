Feature: Login


    @SuccessfulLogin
    Scenario: User perfoms a successful login
        Given The user is in the login page
        When The user enters username and password
        # And Clicks the login button
        Then It takes the user to the inventory page
        

    @LockedoutUser
    Scenario: A locked out user tries to login
        Given The user gets to the login page
        When It enters username and password
        # And Click the login button
        Then An error message should appear
    
    @ProblemUser
    Scenario: User encounters a problem after loggin in
        Given The user logs in
        And is in the inventory page
        When they select an item
        Then it should take them to the item's page

    @PerformanceGlitchUser
    Scenario: User encounters a performance glitch
        Given The user may encounter a performance glitch
        When They enter username and password
        Then it should immediatly take them to the inventory page

      








