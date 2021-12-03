Feature: shopping items manipulation

  Background:
    Given The saucedemo login page is displayed

  Scenario: Validate the number of items that have been added after items selection
    When I login with standard user credential
    And  I validate home page
    And I select three items randomly
    And I click the shopping icon
    Then I validate the three items added to cart

  Scenario: Validate the number of items available after one item removed
    When I login with standard user credential
    And  I validate home page
    And I select two items randomly
    And I click the shopping icon
    And I remove one item
    Then I validate the one item added to cart

  Scenario: Validate i am navigate to homepage after clicking the continue shopping button
    When I login with standard user credential
    And  I validate home page
    And I select one item randomly
    And I click the shopping icon
    And I click the continue shopping button
    Then I validate home page
