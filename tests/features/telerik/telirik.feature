Feature: Telerik registration and select subcategory

  Background:
    Given The telerik demos page is displayed


  Scenario: Verify the registration page.
    When I click the your account icon on demo page
    And I click create an account for free on login page
    And I fill the details on account creation page
    Then I validate the registration-successful message


  Scenario: Verify subcategory
    When I click the demos subcategory in demo page
    Then I validate the selected category heading