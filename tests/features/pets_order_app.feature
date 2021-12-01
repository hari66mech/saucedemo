Feature: Order pets randomly

  Scenario: Validate all the fields are accepting the valid data and click save account information button, it navigate home page.
    Given The jpetstore demo login page is displayed
    When  I fill the user information
    And I fill the account information
    And I fill the profile information
    When Validate i click save account information button, it navigate to jpetstore demo home page
    When I click the pet from the pets category
