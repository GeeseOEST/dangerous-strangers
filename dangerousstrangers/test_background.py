import pytest
from dangerousstrangers.background import Background

@pytest.fixture(params=[
    ("test", "simple_test"),
    ("test", "realistic_test"),
    ("test", "absurd_test")
])
def background_resource(request):
    print("Start setup before test")
    test_resource = Background(*request.param)
    print("End setup before test")

    yield test_resource
    
    print("Teardown after test")
    
class TestCoreFunctions:
    
    def test_initialization(self, background_resource):
        assert background_resource is not None
    
    # This checks the CLASS not the JSON, so keep in mind that you will need to ensure the labels match what they're called in the CLASS *after* they have been modified
    @pytest.mark.parametrize("attribute", ["race", "age", "size", "speed", "languages", "proficiencies", "attributes", "ability_score_modifiers"]) 
    def test_attributes_exist(self, attribute, background_resource):
        assert hasattr(background_resource, attribute), f"{attribute} does not exist"


class TestSetProficiencies:

    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_standard_contains_all(self, background_resource, area):
        assert area in background_resource.proficiencies

    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_selectable_contains_all(self, background_resource, area):
        assert area in background_resource.selectable_proficiencies

    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_standard_set_correctly(self, background_resource, area):
        try:
            assert (
                background_resource.proficiencies[area]
                == background_resource.rules["proficiencies"]["standard"][area]
            )
        except KeyError:
            pass

    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_selectable_set_correctly(self, background_resource, area):
        try:
            assert (
                background_resource.selectable_proficiencies[area]
                == background_resource.rules["proficiencies"]["selectable"][area]
            )
        except KeyError:
            pass

class TestSetLanguages:
    ...
    

class TestSetEquipment:
    ...
    

class TestSetMoney:
    ...
    

class TestSetFeatures:
    ...