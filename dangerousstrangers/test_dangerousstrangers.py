import pytest
from dangerousstrangers import set_stats, roll_stats, select_characteristics, randomize_characteristics, select_name

# Test Characteristics

def test_select_characteristics_returns_correct_dict():
    """Expected: {'name':{'first_name':_, 'last_name':_},'race':_, 'class':_, 'background':_}"""
    characteristics = select_characteristics()
    assert isinstance(characteristics, dict), "select_characteristics should return a dict"
    assert len(characteristics) == 4, "output from select_characteristics should have 4 key:value pairs in top level"
    assert 'name' in characteristics, "name should exist in dict"
    if 'name' in characteristics:
        names = characteristics['name']
        assert 'first_name' in names, "first_name should exist in 'names' inside dict"
        assert 'last_name' in names, "last_name should exist in 'names' inside dict"

def test_select_characteristics_returns_race():
    characteristics = select_characteristics()
    assert 'race' in characteristics, "race should exist in output from select_characteristics"
    
def test_select_characteristics_returns_class():
    characteristics = select_characteristics()
    assert 'class' in characteristics, "class should exist in output from select_characteristics"

def test_select_characteristics_returns_background():
    characteristics = select_characteristics()
    assert 'background' in characteristics, "background should exist in output from select_characteristics"

    
def test_randomize_characteristics_returns_correct_dict():
    """Expected: {'race':_, 'class':_, 'background':_}"""
    characteristics = randomize_characteristics()
    assert isinstance(characteristics, dict), "randomize_characteristics should return a dict"
    assert len(characteristics) == 3, "output from randomize_characteristics should have 3 key:value pairs"

def test_randomize_characteristics_returns_race():
    characteristics = randomize_characteristics()
    assert 'race' in characteristics, "race should exist in output from randomize_characteristics"
    
def test_randomize_characteristics_returns_class():
    characteristics = randomize_characteristics()
    assert 'class' in characteristics, "class should exist in output from randomize_characteristics"

def test_randomize_characteristics_returns_background():
    characteristics = randomize_characteristics()
    assert 'background' in characteristics, "background should exist in output from randomize_characteristics"


def test_select_name_returns_dict():
    """Expected: {'first_name':_, 'last_name':_}"""
    name = select_name()
    assert isinstance(name, dict), "Output from select_name should be a dict"
    assert len(name) == 2, "Output from select_name should have 2 key:value pairs"
    
def test_select_name_returns_first_name():
    name = select_name()
    assert 'first_name' in name, "select_name output should contain first_name"
    
def test_select_name_returns_last_name():
    name = select_name()
    assert 'last_name' in name, "select_name output should contain last_name"

# Test Stats
    
def test_set_stats_returns_stats_list():
    stats_list = set_stats()
    assert isinstance(stats_list, list), "set_stats should return a list"
    assert len(stats_list) == 6,  "set_stats return list should be 6 items long"
    
def test_roll_stats_returns_stats_list():
    stats_list = roll_stats()
    assert isinstance(stats_list, list), "roll_stats should return a list"
    assert len(stats_list) == 6, "roll_stats return list should be 6 items long"
    
def test_roll_stats_returns_different_stats():
    """
    Runs through the roll_stats function to confirm uniqueness.
    
    Runs through the roll_stats function 10 times so that there are 10 different sets of stats, and then compares them to make sure they're not all identical. As long as there are two lists that aren't identical we can be confident that they are random enough, and the statstical chance of getting 10 x the exact same random numbers is low enough that I am comfortable with it.
    """
    
    list_of_lists = []
    for _ in range(10):
        new_stats = roll_stats()
        list_of_lists.append(new_stats)
    
    unique_lists = set()
    for stats in list_of_lists:
        list_tuple = tuple(stats)
        unique_lists.add(list_tuple)
        
    assert len(unique_lists) > 7, "Multiple returns from roll_stats should not be identical"
    if len(unique_lists) > 7:
        assert len(unique_lists) == len(list_of_lists), "Multiple returns from roll_stats should not be identical - Statistical improbability may have occured, run tests again to confirm"
    

# Test Print Ready Character Creation

"""
ALL COMMENTED OUT UNTIL IMPLEMENTATION OF CHARACTER OR MOCKING IS FIGURED OUT TODO

def test_print_character_provideds_string():
    
    print_ready_character = print_character()
    assert isinstance(print_ready_character,str), "print_character should return a string"
    
def test_print_ready_character_contains_stats():
    ...
    
def test_print_character_contains_name():
    ...
    
def test_print_character_contains_equipment():
    ...
    
def test_print_character_contains_gold():
    ...
    
"""