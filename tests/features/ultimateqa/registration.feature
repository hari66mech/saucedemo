Feature: Signup

  Scenario: Validate collections page when register as a user
    Given The ultimateqa index page is displayed
    When I register as a user
    And I store the courses list in text file
    Then I validate the collections page
