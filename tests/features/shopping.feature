Feature: Shopping

  Background:
    Given The tutorialsninja index page is displayed

  Scenario: Verify the text summary items with the web items result
    When I get product from the .txt file
    Then I validate the text summary items Data with the web items result

  Scenario: Verify the success message when added to cart
    When I click the product from the home_page
    When I fill the available options for placing an order
    Then I validate success message
