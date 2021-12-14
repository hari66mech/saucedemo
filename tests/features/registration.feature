Feature: Register

  Scenario: Validate success message when register
    Given The tutorialsninja index page is displayed
    When I click the my_account button
    And I click the register button
    And I register as a user
    Then I validate success message
