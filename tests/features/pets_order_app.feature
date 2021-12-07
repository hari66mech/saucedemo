Feature: Order pets randomly

  Background:
    Given The jpetstore demo login page is displayed

  Scenario: Verify the page navigates to the home page when registering on jpetstore demo application
    When I click the register link
    And I register on jpetstore demo application
    Then I validate the home page

  Scenario: Verify order status when random pets are added
    When I login with valid credential
    And I add the first pet to the cart
    And I return to the home page
    And I add the second pet to the cart
    And I validate the total cost
    And I order the pets
    Then I validate the order status
