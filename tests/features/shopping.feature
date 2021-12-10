Feature: Shopping

  Background:
    Given The demoblaze index page is displayed

  Scenario: Validate the success message when checkout
    When I add an item to the cart from the first_page
    And I validate items added to the cart
    And I add an item to the cart from the second_page
    And I click place order and fill in the details
    Then I validate the success message

  Scenario: Validate the success message when different types of items checkout
    When I add an item to the cart from the mobile
    And I add an item to the cart from the laptop
    And I add an item to the cart from the Monitor
    And I validate added items
    And I click place order and fill in the details
    Then I validate the success message
