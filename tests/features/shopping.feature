Feature: Shopping

  Background:
    Given The tutorialsninja index page is displayed

  Scenario: Verify the text summary items with the web items result
    When I get product from the text file
    Then I validate the text items summary with the web item results

  Scenario: Verify the success message when a product/item is added to cart
    When I click the product from the home_page
    And I fill the product options for placing an order
    Then I validate success message
