Feature: Saucedemo login

    Background: Lunch login page
        Given The saucedemo login page is displayed

    @login
    Scenario: Verify the user login with standard_user credential
        When Login as the standard_user credential
        And Validate the home page
        Then Redirect to the cart page

    @locked_out_user
    Scenario: Verify the user login with locked_out_user credential
        When Login as the locked_out_user credential
        Then Validate error message