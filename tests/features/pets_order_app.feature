Feature: Order pets randomly

  Scenario: Verify the registration page and select pets randomly
    Given The jpetstore demo login page is displayed
    When  I fill the user information
    And Navigate to jpetstore demo home page
    And I select the first pet
    And I add the first pet to the cart
    And I return to the home page
    And I select the second pet
    And I add the second pet to the cart
    Then I calculate the cost of each item and compare with  the total
    And I order the pets
    And Verify my order is placed
