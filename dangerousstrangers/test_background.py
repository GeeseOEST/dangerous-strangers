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
    
    def test_standard_languages_set(self, background_resource):
        try: 
            assert (background_resource.languages == background_resource.rules["languages"]["standard"]), "Standard languages should match JSON"
        except KeyError:
            pass
        
    def test_selectable_counter_incremented(self, background_resource):
        assert hasattr(background_resource, "language_choices"), "Selectable language counter 'language_choices' does not exist"
        try:
            assert (background_resource.language_choices == background_resource.rules["languages"]["selectable"]), "language_choices should match JSON"
        except KeyError:
            pass
    

class TestSetEquipment:
    
    def test_correct_amount_of_equipment(self, background_resource):
        assert len(background_resource.equipment) == len(
            background_resource.rules["equipment"]
        )

    def test_equipment_correctly_set(self, background_resource):
        try:
            for item in range(len(background_resource.rules["equipment"])):
                assert (
                    background_resource.equipment[item]
                    in background_resource.rules["equipment"][item]
                    or background_resource.equipment[item]
                    == background_resource.rules["equipment"][item]
                ), f"{background_resource.equipment[item]} should be in equipment[{item}]"
        except IndexError:
            assert (False), f"{item} is not a valid index, equipment list may not yet exist"
            
    def test_equipment_follows_correct_pattern(self, background_resource):
        if len(background_resource.equipment) > 0:
            # print(background_resource.equipment)
            for item in range(len(background_resource.equipment)):
                # print(item)
                # print(background_resource.equipment[item])
                assert isinstance(background_resource.equipment[item][0], str)
                assert isinstance(background_resource.equipment[item][1], int)
    

class TestSetMoney:
    ...
    

class TestSetFeatures:
    
    def test_features_is_dict(self, background_resource):
        assert isinstance(background_resource.features, dict), "self.features should be a dict"
    
    def test_features_match_level_simple(self, background_resource):
        correct_number_of_feats = 0
        
        for level in range(background_resource.level):
            correct_number_of_feats += len(background_resource.rules["feats"][f'{level+1}'])
            
        assert correct_number_of_feats == len(
            background_resource.features
        ), f"Archetype has {len(background_resource.features)} feats, should have {correct_number_of_feats}"
        
        
    def test_features_contain_correct_key_value(self, background_resource):
               
        correct_feats = {}
        for level in range(background_resource.level):
            for key in background_resource.rules["feats"][f"{level+1}"]:
                correct_feats[key] = background_resource.rules["feats"][f"{level+1}"][key]
                 
        for key in background_resource.features:
            assert background_resource.features[key] == correct_feats[key]