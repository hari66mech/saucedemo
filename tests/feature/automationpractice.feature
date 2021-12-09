Feature: Register on the Automationpractice application and shop items

  Background:
    Given The automationpractice index page is displayed

  Scenario Outline: Verify user is navigated to my account page when registered
    When I click the sign_in button on the index page
    And I click the create_account button on the sign_in page
    And I fill the user <first_name> and <last_name>
    And I fill the user details on the account_creation page
    Then I validate the my_account page
    Examples:
      | first_name | last_name |
      |    sam     |   dinesh  |

  Scenario: Verify order is placed after completed the checkout process
    When I click the sign_in button on the index page
    And I signin as a user on the sign_in page
    And I select items on index page
    And I accept the checkout process
    And I select payment method
    Then I validate order confirmation on order confirmation page

  Scenario: Verify order is placed after women offer wear is checkout
    When I click the sign_in button on the index page
    And I signin as a user on the sign_in page
    And I select items on women wear index page
    And I accept the checkout process
    And I select payment method
    Then I validate order confirmation on order confirmation page
