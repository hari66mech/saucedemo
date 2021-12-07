Feature: shopping items manipulation

  Background:
    Given The saucedemo login page is displayed

  Scenario: Verify the number of items that have been added
    When I login as a standard user
    And I validate the home page
    And I add three_items to the cart
    And I click the shopping icon
    And I validate cart page title
    Then I validate three_items added in the cart

  Scenario: Verify the number of items available to the cart when remove an item
    When I login as a standard user
    And I validate the home page
    And I add two_items to the cart
    And I click the shopping icon
    And I remove one item from cart page
    Then I validate an_item added in the cart

  Scenario: Verify the page should navigate when click the continue shopping button
    When I login as a standard user
    And I validate the home page
    And I add an_item to the cart
    And I click the shopping icon
    And I click the continue shopping button
    Then I validate the home page
