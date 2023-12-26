import pytest

from dangerousstrangers.json_loader import load_top_level_keys, load_chosen_component, load_test_file


class TestLoadTopLevelKeys: # Tests Top Level Keys

    def test_load_top_level_returns_list(self):
        result = load_top_level_keys("test")
        assert isinstance(
            result, list
        ), "Output from load_top_level should be a list"


    def test_load_top_level_extracts_correctly(self):
        keys = load_top_level_keys("test")
        assert (
            keys == ["top_level_key1", "top_level_key2", "top_level_key3"]
        ), "Keys should match the top level keys in the json file"
    


class TestLoadChosenComponent: # Tests Load Chosen Component

    def test_returns_dict(self):
        component = load_chosen_component("test","top_level_key2")
        assert isinstance(
            component, dict
        ), "Output from load_chosen_component should be a dictionary object"
        
    def test_load_chosen_component_indexes_correctly(self):
        component = load_chosen_component("test","top_level_key2")
        assert (component == {
            "string2": "string2",
            "list2": ["list2_item1", "list2_item2"],
            "int2": 2
        }), "Component contents should match the json file"
        
        
class TestLoadTestFile: # Tests Load Test File for the XXXs_mock.json files

    def test_returns_dict(self):
        component = load_test_file("test", "top_level_key1")
        assert isinstance(
            component, dict
        ), "Output from load_chosen_component should be a dictionary object"
        
    def test_contains_expected_contents(self):
        component = load_test_file("test", "top_level_key1")
        assert (component == {
                "string1": "string1",
                "list1": ["list1_item1", "list1_item2"],
                "int1": 1
            }
            ), "Component contents should match the json file"
        
