Feature: Login

    New Login

    Scenario Outline: User logs in 
        Given the user is in the login page
        When the user logs in with "<username>" and "<password>"
            And reaches the inventory page
            And selects an item
        Then it should take them to the item's page
            And come back to the inventory page
            And log out
    
    Examples:
        | Username                | Password      |
        | standard_user           | secret_sauce  |
        | locked_out_user         | secret_sauce  |
        | problem_user            | secret_sauce  |
        | performance_glitch_user | secret_sauce  |