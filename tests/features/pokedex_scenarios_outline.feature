Feature: pokedex search

  Background:
    Given The pokedex page is displayed

  @pokemon
  Scenario Outline: pokeman
     When I am calculating the total pokeman
     And I am searching <text> pokeman
     Examples:
       | text         |
       | Bulbasaur    |
       | Wartortle    |