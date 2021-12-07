Feature: Order pets randomly

  Background:
    Given The jpetstore demo login page is displayed

  Scenario: Verify the registration page and page navigation
    When I click the register link
    And  I fill the user information
    Then I navigate to jpetstore demo home page

  Scenario: Verify random pets selection and check my order statues
    When I login with valid credential
    And I add the first pet to the cart
    And I return to the home page
    And I add the second pet to the cart
    Then I validate the total amount
    And I order the pets
    And I validate my order is placed
