import pytest

from json_loader import load_top_level_keys, load_chosen_component


# Tests Top Level Keys


def test_load_top_level_returns_list():
    result = load_top_level_keys("test")
    assert isinstance(
        result, list
    ), "Output from load_top_level should be a list"


def test_load_top_level_extracts_correctly():
    keys = load_top_level_keys("test")
    assert (
        keys == ["top_level_key1", "top_level_key2", "top_level_key3"]
    ), "Keys should match the top level keys in the json file"
    

# Tests Load Chosen Component

def test_load_chosen_component_returns_dict():
    component = load_chosen_component("test","top_level_key2")
    assert isinstance(
        component, dict
    ), "Output from load_chosen_component should be a dictionary object"
    
def test_load_chosen_component_indexes_correctly():
    component = load_chosen_component("test","top_level_key2")
    assert (component == {
        "string2": "string2",
        "list2": ["list2_item1", "list2_item2"],
        "int2": 2
    }), "Component contents should match the json file"