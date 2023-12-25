import pytest

'''import sys
import os

# Adjust sys.path to include the dangerousstrangers directory as no src directory exists currently. Not in use currently as test directory not used.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dangerousstrangers')))'''

from race import Race

# Setup and teardown using fixtures

@pytest.fixture(params=[
    ("test", "simple_test"),
    ("test", "realistic_test"),
    ("test", "absurd_test")
])
def race_resource(request):
    print("Start setup before test")
    test_resource = Race(*request.param)
    print("End setup before test")

    yield test_resource
    
    print("Teardown after test")

# Test for the Race class definition

class TestCoreFunctions:
    
    def test_initialization(self, race_resource):
        assert race_resource is not None
    
    # This checks the CLASS not the JSON, so keep in mind that you will need to ensure the labels match what they're called in the CLASS *after* they have been modified
    @pytest.mark.parametrize("attribute", ["age_range", "size", "speed", "languages", "proficiencies", "attributes", "ability_score_modifiers"]) 
    def test_attributes_exist(self, attribute, race_resource):
        assert hasattr(race_resource, attribute), f"{attribute} does not exist"

    
class TestSetAge:
    
    def test_age_not_negative(self, race_resource):
        assert (race_resource.age > 0), "Age should not be negative"
        
    def test_age_is_in_range(self, race_resource):
        age_range = race_resource.rules["age_range"] # List of [maturity, maximum]
        assert (race_resource.age < age_range[1]), "Age should be below maximum age provided"
        
    def test_maturity_level_configured(self, race_resource):
        assert hasattr(race_resource, "maturity"), "'maturity' does not exist"
        
    def test_maturity_level_correct(self, race_resource):
        age_range = race_resource.rules["age_range"] # List of [maturity, maximum]
        if race_resource.age < age_range[0]:
            assert (race_resource.age == "immature"), "Should be considered immature"
        else:
            assert (race_resource.age == "mature"), "Should be considered mature"

        
class TestSetLanguage:
    
    def test_standard_languages_set(self, race_resource):
        assert (race_resource.languages == race_resource.rules["languages"]["standard"]), "Standard languages should match JSON"
        
    def test_selectable_counter_incremented(self, race_resource):
        assert hasattr(race_resource, "language_choices"), "Selectable language counter 'language_choices' does not exist"
        assert (race_resource.language_choices == race_resource.rules["languages"]["selectable"]), "language_choices should match JSON"
        
class TestSetProficiencies:
    
    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_standard_proficiencies_set(self, area, race_resource):
        assert (race_resource.proficiencies[area] == race_resource.rules["proficiencies"][area])
               
class TestSetAttributes:
    
    def test_attributes_set(self, race_resource):
        assert (len(race_resource.attributes) == len(race_resource.rules["attributes"]))