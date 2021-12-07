Feature: shopping items manipulation

  Background:
    Given The saucedemo login page is displayed

  Scenario: Verify the number of items that have been added
    When I login with standard user credential
    And I validate the home page
    And I add three items to the cart
    And I click the shopping icon
    And I validate cart page title
    Then I validate the three items added to cart

  Scenario: Verify the number of items available to the card
    When I login with standard user credential
    And I validate the home page
    And I add two items to the cart
    And I click the shopping icon
    And I remove one item from cart page
    Then I validate the one item added to cart

  Scenario: Verify the continue shopping button action
    When I login with standard user credential
    And I validate the home page
    And I add an item to the cart
    And I click the shopping icon
    And I click the continue shopping button
    Then I validate the home page
