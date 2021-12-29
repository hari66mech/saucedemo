Feature: Next generation automation signup

    Scenario: Verify the success message when signup as a user
        Given The nextgenerationautomation home_page is displayed
        When I click the login/signUp button
        And I signup as a user
        Then I validate the success message
