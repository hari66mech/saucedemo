Feature: saucedemo items shopping

  Background:
    Given The saucedemo_login page is displayed

  @add
  Scenario: Verify the quantity on the cart page.
    When I login as an standard user
    And I validate the home page
    And I add an_item to the cart
    And I remove an item from the cart page
    And I click the continue_shopping button on cart page
    And I add two_items to the cart
    Then I validate the quantity on the cart page
