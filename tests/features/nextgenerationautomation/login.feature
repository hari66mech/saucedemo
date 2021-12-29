Feature: Next generation automation login

    Scenario Outline: Verify the page is redirect to the home page when login with valid credential
        Given The nextgenerationautomation home_page is displayed
        When I click the login/signUp button
        And I click the log-in button
        And I login as a valid <email> and <password>
        Then I validate login button is clickable
        Examples:
            | email | password |
            | ram123@gamil.com | Ram!2021 |
            | raj123@gmail.com | raj!2021 |
