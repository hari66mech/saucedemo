Feature: saucedemo items shopping

  Background:
    Given The saucedemo login page is displayed

  Scenario: Verify the quantity on the cart page.
    When I login as standard user
    And I validate the home page
    And I add an item to the cart
    And I navigate to the cart page
    And I remove the item on cart page
    And I click the continue shopping button on cart page
    And I add two items to the cart
    Then I validate the quantity on the cart page
