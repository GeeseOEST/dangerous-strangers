import pytest
from archetype import Archetype

@pytest.fixture(params=[
    ("test", 1, "simple_test"),
    ("test", 1, "realistic_test"),
    ("test", 1, "absurd_test"),
    ("test", 2, "simple_test"),
    ("test", 2, "realistic_test"),
    ("test", 2, "absurd_test")
])
def archetype_resource(request):
    print("Start setup before test")
    test_resource = Archetype(*request.param)
    print("End setup before test")

    yield test_resource
    
    print("Teardown after test")
    
    
class TestCoreFunctions:
    
    def test_initialization(self, archetype_resource):
        assert archetype_resource is not None
        
    @pytest.mark.parametrize("attribute", ["archetype","hitedice", "core_stat", "proficiencies", "equipment", "feats"]) 
    def test_attributes_exist(self, attribute, archetype_resource):
        assert hasattr(archetype_resource, attribute), f"{attribute} does not exist"
        

class TestSetProficiencies:
    
    def test_standard_set_correctly(self, archetype_resource):
        ...
        
    def test_selectable_set_correctly(self, archetype_resource):
        ...
        
class TestSetEquipment:
    
    def test_equipment_correctly_set(self, archetype_resource):
        ...
        
    def test_correct_amount_of_equipment(self, archetype_resource):
        ... 
        
    def test_random_equipment_picks_only_one_item(self, archetype_resource):
        ...
    
class TestSetFeatures:
    
    def test_features_match_level_simple(self, archetype_resource):
        ...
        
    def test_features_match_level_deep(self, archetype_resource):
        ...