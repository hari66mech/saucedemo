Feature: Shopping

  Background:
    Given The competethemes index page is displayed

  Scenario: Verify the product_to_checkout is clickable when add on-sale-products
    When I select an on-sale-product randomly
    And I add an on-sale-product to the cart
    And I click the view_cart button
    Then I validate the product_to_checkout button is clickable

  Scenario: Verify the product_to_checkout is clickable when add top-rated-products
    When I select an top-rated-product randomly
    And I add an top-rated-product to the cart
    And I click the view_cart button
    Then I validate the product_to_checkout button is clickable

  Scenario: Verify the product_to_checkout is clickable when add latest-products
    When I select an latest-product randomly
    And I add an latest-product to the cart
    And I click the view_cart button
    Then I validate the product_to_checkout button is clickable
