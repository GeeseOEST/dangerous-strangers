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
    
    def test_age_appropriate(self, race_resource):
        ...
        
    def test_maturity_level_configured(self, race_resource):
        ...
        
class TestSetLanguage:
    
    def test_ss(self):
        ...