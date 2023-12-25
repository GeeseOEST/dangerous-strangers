import pytest

'''import sys
import os

# Adjust sys.path to include the dangerousstrangers directory as no src directory exists currently. Not in use currently as test directory not used.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dangerousstrangers')))'''

from race import Race

# Setup and teardown using fixtures

@pytest.fixture
def resource_setup_teardown():
    test_resource = Race("test")
    print("Setup before test")
    yield test_resource
    
    print("Teardown after test")

# Test for the Race class definition

class TestCoreFunctions:
    
    def test_attributes_exist(self, resource_setup_teardown):
        assert hasattr(resource_setup_teardown, "age"), "age does not exist"
        
    def test_age_range_exist(self, resource_setup_teardown):
        assert hasattr(resource_setup_teardown, "age_range"), "age_range does not exist"
        
        