Feature: Features


  Scenario: Verify the text summary features with the web features result
    Given The phptravels home page is displayed
    When I select the main_features in features on home_page
    And I get the features on features_page
    Then I validate the text summary features with the web features result
