Feature: Plans and Prices
  Background:
    Given The phptravels home page is displayed
    When I click the pricing button on home_page

  Scenario: Verify the page is navigate to order-confirm page when select the platform and click buy now
    When I select the platform on order page
    And I click the buy_now button on order_page
    Then I validate the order_confirm page navigation

  Scenario: Verify the page is navigate to order-confirm page when select the feature and click buy now
    When I select the feature on order page
    And I click the buy_now button on order_page
    Then I validate the order_confirm page navigation

  Scenario: Verify the page is navigate to order-confirm page when select the module and click buy now
    When I select the module on order page
    And I click the buy_now button on order_page
    Then I validate the order_confirm page navigation

  Scenario: Verify the page is navigate to order-confirm page when select the supplier and click buy now
    When I select the supplier on order page
    And I click the buy_now button on order_page
    Then I validate the order_confirm page navigation

  Scenario: Verify the page is navigate to order-confirm page when select the payment_gateway and click buy now
    When I select the payment_gateway on order page
    And I click the buy_now button on order_page
    Then I validate the order_confirm page navigation

  Scenario: Verify the page is navigate to order-confirm page when select the extra and click buy now
    When I select the extra on order page
    And I click the buy_now button on order_page
    Then I validate the order_confirm page navigation
