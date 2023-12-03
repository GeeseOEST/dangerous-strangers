import pytest

# Test Characteristics

def test_select_characteristics_returns_correct_dict():
    """Expected: {race:_, class:_, background:_}"""
    ...

def test_select_characteristics_returns_race():
    ...
    
def test_select_characteristics_returns_class():
    ...

def test_select_characteristics_returns_background():
    ...
    
def test_randomize_characteristics_returns_correct_dict():
    """Expected: {race:_, class:_, background:_}"""
    ...

def test_randomize_characteristics_returns_race():
    ...
    
def test_randomize_characteristics_returns_class():
    ...

def test_randomize_characteristics_returns_background():
    ...


# Test Stats
    
def test_set_stats_returns_stats_list():
    stats_list = set_stats()
    assert isinstance(stats_list, list) "set_stats should return a list"
    assert len(stats_list) == 6  "set_stats return list should be 6 items long"
    
def test_roll_stats_returns_stats_list():
    stats_list = roll_stats()
    assert isinstance(stats_list, list) "roll_stats should return a list"
    assert len(stats_list) == 6 "roll_stats return list should be 6 items long"
    
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
        
    assert len(unique_lists) > 7 "Multiple returns from roll_stats should not be identical"
    if len(unique_lists) > 7:
        assert len(unique_lists) == len(list_of_lists) "Multiple returns from roll_stats should not be identical - Statistical improbability may have occured, run tests again to confirm"
    

# Test Print Ready Character Creation

def test_print_character_provideds_string():
    
    print_ready_character = print_character()
    assert isinstance(print_ready_character,str) "print_character should return a string"
    
def test_print_ready_character_contains_stats():
    ...
    
def test_print_character_contains_name():
    ...
    
def test_print_character_contains_equipment():
    ...
    
def test_print_character_contains_gold():
    ...