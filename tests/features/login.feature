Feature: Saucedemo login

    Background:
        Given The saucedemo login page is displayed

    Scenario: Validate the cart page when the user login with standard_user credential
        When I login with the standard_user credentials
        And I validate the home page
        And I add random item to cart
        Then I validate the cart page

    Scenario: Verify the error message when logged in with a locked-out user.
        When I Login with the locked_out_user credential
        Then I validate the error message
