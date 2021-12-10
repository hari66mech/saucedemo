Feature: Login

  Scenario: Validate whether the user is logged in
    Given The demoblaze index page is displayed
    When I sign_up as a user
    And I login with valid credential
    Then I validate the user is logged in
