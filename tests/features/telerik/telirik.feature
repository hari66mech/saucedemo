Feature: Telerik registration and select subcategory

  Background:
    Given The telerik_demo page is displayed

  Scenario: Verify the success message on the registration page
    When I click the account icon on the demo page
    And I click the create_account_button on the login page
    And I fill in the details on the registration page
    Then I validate the registration-successful message

  Scenario: Verify the category heading when click the subcategory
    When I click the demos subcategory in demo page
    Then I validate the selected category heading
