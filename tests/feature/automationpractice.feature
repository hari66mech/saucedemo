Feature: Register on the Automationpractice application and shop items

  Background:
    Given The automationpractice index page is displayed

  Scenario Outline: Verify the page is navigates to the my_account page when clicking the register button
    When I click the sign_in on the index page
    And I click the create_account_button on the sign_in page
    And I fill the user <first_name> and <last_name>
    And I fill the details on the account_creation page
    Then I validate the my_account page
    Examples:
      | first_name | last_name |
      |    sam     |   dinesh  |
