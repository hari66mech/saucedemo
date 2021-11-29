import time

from pytest_bdd import scenarios, given, when, parsers
from pageobjectmodel.pokeman import Pokeman

scenarios('../features/pokedex_scenarios_outline.feature')


@given('The pokedex page is displayed')
def pokedex_page(driver):
    """This method is used to get and open the URL"""
    driver.get('https://pokedex.org/')


@when("I am calculating the total pokeman")
def calculate_total_pokemon(driver):
    """This method is used to calculate the total pokeman"""
    Pokeman(driver).length_of_the_list()


@when(parsers.parse("I am searching {text} pokeman"))
def search_pokemon_name(driver, text):
    """This method is used to search the particular pokeman"""
    Pokeman(driver).search_pokeman(text)
