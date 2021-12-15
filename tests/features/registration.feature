Feature: Register

  Scenario: Validate success message when register as a new user
    Given The tutorialsninja index page is displayed
    When I click the my_account button
    And I click the register button
    And I register as a new user
    Then I validate success message
