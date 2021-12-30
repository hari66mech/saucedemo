Feature: Form filling

  Scenario: Verify the submit button is clickable when fill form
    Given The demoqa practice_form page is displayed
    When I fill the practice_form
    Then I validate submit button is clickable
