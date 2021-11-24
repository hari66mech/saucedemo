Feature: Saucedemo login

    Scenario: Verify the user login with locked_out_user credential
        Given I am launching chrome browser
        When Login as the locked_out_user credential
        Then Validate error message