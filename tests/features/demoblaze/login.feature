Feature: Login

  Scenario: Validate whether the user is logged in
    Given The demoblaze index page is displayed
    When I register as a user
    Then I validate the user is logged in
