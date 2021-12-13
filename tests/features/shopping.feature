Feature: Shopping

  Background:
    Given The demoblaze index page is displayed

  Scenario: Verify the success message on the checkout
    When I add an item from the first_page
    And I validate items added to the cart
    And I add an item from the second_page
    And I click the cart button
    And I click the place order button
    And I fill the user_info for placing an order
    Then I validate the success message

  Scenario: Verify the success message when multiple category items the checkout
    When I add an item to the cart from the mobile
    And I add an item to the cart from the laptop
    And I add an item to the cart from the Monitor
    And I validate added items
    And I click the cart button
    And I click the place order button
    And I fill the user_info for placing an order
    Then I validate the success message
