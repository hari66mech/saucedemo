Feature: Register on the Automationpractice application and shop items

  Background:
    Given The automationpractice index page is displayed
    When I click the sign_in button on the index page
    And I signin as a user on the signin page

  Scenario: Verify order is placed after completed the checkout process
    When I select items on index page
    And I accept the checkout process
    And I select payment method
    Then I validate order confirmation on order confirmation page

  Scenario: Verify order is placed after women offer wear is checkout
    When I select women wear items on index page
    And I accept the checkout process
    And I select payment method
    Then I validate order confirmation on order confirmation page
