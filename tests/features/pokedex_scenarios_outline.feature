Feature: pokedex search

  Background:
    Given The pokedex page is displayed

  Scenario Outline: pokeman
     When I am calculating the total pokeman
     And I am searching <text> pokeman
     Examples:
       | text         |
       | Bulbasaur    |
       | Wartortle    |

  @pikachu
  Scenario: Click the pokeman
    When I am searching Pikachu pokeman
    And I am clicking Pikachu pokeman
    Then I am verifying the page url