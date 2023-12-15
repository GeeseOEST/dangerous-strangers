import pytest
from dangerousstrangers import (
    set_scores,
    roll_scores,
    select_characteristics,
    randomize_characteristics,
    select_name,
)

# To begin with these are just simple tests to make sure that different components are returning the appropriate things
# Longer term I think I would like to split things out and either have one file per function with all the tests, or one file for simple tests and another for complex
# Depends on what the best practice is, although instinct would tell me that it should be one file per thing

# Test Characteristics

# fmt: off
def test_select_characteristics_returns_correct_dict():
    """Expected: {'name':{'name':_, 'name':_},'race':_, 'archetype':_, 'background':_}"""
    characteristics = select_characteristics()
    assert (
        isinstance(characteristics, dict)
    ), "select_characteristics should return a dict"
    assert (
        len(characteristics) == 4
    ), "output from select_characteristics should have 4 key:value pairs in top level"
    assert "name" in characteristics, "name should exist in dict"
    if "name" in characteristics:
        names = characteristics["name"]
        assert "first" in names, "key of first should exist in 'names' inside dict"
        assert "last" in names, "key of last should exist in 'names' inside dict"


def test_select_characteristics_returns_race():
    characteristics = select_characteristics()
    assert (
        "race" in characteristics
    ), "race key should exist in output from select_characteristics"


def test_select_characteristics_returns_archetype():
    characteristics = select_characteristics()
    assert (
        "archetype" in characteristics
    ), "archetype key should exist in output from select_characteristics"


def test_select_characteristics_returns_background():
    characteristics = select_characteristics()
    assert (
        "background" in characteristics
    ), "background key should exist in output from select_characteristics"


def test_randomize_characteristics_returns_correct_dict():
    """Expected: {'race':_, 'archetype':_, 'background':_}"""
    characteristics = randomize_characteristics()
    assert (
        isinstance(characteristics, dict)
    ), "randomize_characteristics should return a dict"
    assert (
        len(characteristics) == 3
    ), "output from randomize_characteristics should have 3 key:value pairs"


def test_randomize_characteristics_returns_race():
    characteristics = randomize_characteristics()
    assert (
        "race" in characteristics
    ), "race should exist in output from randomize_characteristics"


def test_randomize_characteristics_returns_archetype():
    characteristics = randomize_characteristics()
    assert (
        "archetype" in characteristics
    ), "archetype should exist in output from randomize_characteristics"


def test_randomize_characteristics_returns_background():
    characteristics = randomize_characteristics()
    assert (
        "background" in characteristics
    ), "background should exist in output from randomize_characteristics"


def test_select_name_returns_dict():
    """Expected: {'first':_, 'last':_}"""
    name = select_name("human")
    assert isinstance(name, dict), "Output from select_name should be a dict"
    assert len(name) == 2, "Output from select_name should have 2 key:value pairs"


def test_select_name_returns_first_name():
    name = select_name("human")
    assert "first" in name, "select_name output should contain first"


def test_select_name_returns_last_name():
    name = select_name("human")
    assert "last" in name, "select_name output should contain last"


# Test scores


def test_set_scores_returns_scores_list():
    scores_list = set_scores()
    assert isinstance(scores_list, list), "set_scores should return a list"
    assert len(scores_list) == 6, "set_scores return list should be 6 items long"


def test_roll_scores_returns_scores_list():
    scores_list = roll_scores()
    assert isinstance(scores_list, list), "roll_scores should return a list"
    assert len(scores_list) == 6, "roll_scores return list should be 6 items long"


def test_roll_scores_returns_different_scores():
    """
    Runs through the roll_scores function to confirm uniqueness.

    Runs through the roll_scores function 10 times so that there are 10 different sets of scores, and then compares them to make sure they're not all identical. As long as there are two lists that aren't identical we can be confident that they are random enough, and the scorestical chance of getting 10 x the exact same random numbers is low enough that I am comfortable with it.
    """

    list_of_lists = []
    for _ in range(10):
        new_scores = roll_scores()
        list_of_lists.append(new_scores)

    unique_lists = set()
    for scores in list_of_lists:
        list_tuple = tuple(scores)
        unique_lists.add(list_tuple)

    assert (
        len(unique_lists) > 7
    ), "Multiple returns from roll_scores should not be identical"
    if len(unique_lists) > 7:
        assert (
            len(unique_lists) == len(list_of_lists)
        ), "Multiple returns from roll_scores should not be identical - Statistical improbability may have occured, run tests again to confirm"


def test_roll_scores_returns_realistic_numbers():
    """
    Creates 10 sets of score lists, and then checks that none of the indivdual scores are over 18.
    """

    list_of_scores = []
    for _ in range(10):
        new_scores = roll_scores()
        for score in new_scores:
            list_of_scores.append(score)

    for score in list_of_scores:
        assert (
            score <= 18
        ), f"scores should not be higher than 18 from rolling, score was {score}"

# fmt: on

# TODO Test Print Ready Character Creation

"""
ALL COMMENTED OUT UNTIL IMPLEMENTATION OF CHARACTER OR MOCKING IS FIGURED OUT TODO

def test_print_character_provideds_string():
    
    print_ready_character = print_character()
    assert isinstance(print_ready_character,str), "print_character should return a string"
    
def test_print_ready_character_contains_scores():
    ...
    
def test_print_character_contains_name():
    ...
    
def test_print_character_contains_equipment():
    ...
    
def test_print_character_contains_gold():
    ...
    
"""
