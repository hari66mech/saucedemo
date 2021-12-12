Feature: Registration


  Scenario Outline: Verify user is navigated to my account page when registered
    Given The automationpractice index page is displayed
    When I click the sign_in button on the index page
    And I create user account on signin page
    And I fill the user <first_name> and <last_name>
    And I fill the user details on the account_creation page
    Then I validate the my_account page
    Examples:
      | first_name | last_name |
      |    sam     |   dinesh  |
      |    ram     |   dinesh  |