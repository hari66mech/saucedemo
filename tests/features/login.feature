Feature: Saucedemo login

    Scenario: Verify the user login with standard_user credential
        Given I am launching chrome browser
        When Login as the standard_user credential
        Then Redirect to the card page