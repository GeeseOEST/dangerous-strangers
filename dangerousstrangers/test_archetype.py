import pytest
from archetype import Archetype


@pytest.fixture(
    params=[
        ("test", 1, "simple_test"),
        ("test", 1, "realistic_test"),
        ("test", 1, "absurd_test"),
        ("test", 2, "simple_test"),
        ("test", 2, "realistic_test"),
        ("test", 2, "absurd_test"),
    ]
)
def archetype_resource(request):
    print("Start setup before test")
    test_resource = Archetype(*request.param)
    print("End setup before test")

    yield test_resource

    print("Teardown after test")


class TestCoreFunctions:
    def test_initialization(self, archetype_resource):
        assert archetype_resource is not None

    @pytest.mark.parametrize(
        "attribute",
        [
            "archetype",
            "level",
            "hitdice",
            "core_stat",
            "proficiencies",
            "selectable_proficiencies",
            "equipment",
            "features",
        ],
    )
    def test_attributes_exist(self, attribute, archetype_resource):
        assert hasattr(archetype_resource, attribute), f"{attribute} does not exist"


class TestSetProficiencies:
    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_standard_contains_all(self, archetype_resource, area):
        assert area in archetype_resource.proficiencies

    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_selectable_contains_all(self, archetype_resource, area):
        assert area in archetype_resource.selectable_proficiencies

    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_standard_set_correctly(self, archetype_resource, area):
        try:
            assert (
                archetype_resource.proficiencies[area]
                == archetype_resource.rules["proficiencies"]["standard"][area]
            )
        except KeyError:
            pass

    @pytest.mark.parametrize("area", ["armor", "weapon", "tool", "save", "skill"])
    def test_selectable_set_correctly(self, archetype_resource, area):
        try:
            assert (
                archetype_resource.selectable_proficiencies[area]
                == archetype_resource.rules["proficiencies"]["selectable"][area]
            )
        except KeyError:
            pass


class TestSetEquipment:  # Still missing a test to be 100% certain the random item selection is working, but currently it's fairly safe IMHO given that the len is correct and format is correct
    def test_correct_amount_of_equipment(self, archetype_resource):
        assert len(archetype_resource.equipment) == len(
            archetype_resource.rules["equipment"]
        )

    def test_equipment_correctly_set(self, archetype_resource):
        try:
            for item in range(len(archetype_resource.rules["equipment"])):
                assert (
                    archetype_resource.equipment[item]
                    in archetype_resource.rules["equipment"][item]
                    or archetype_resource.equipment[item]
                    == archetype_resource.rules["equipment"][item]
                ), f"{archetype_resource.equipment[item]} should be in equipment[{item}]"
        except IndexError:
            assert (False), f"{item} is not a valid index, equipment list may not yet exist"
            
    def test_equipment_follows_correct_pattern(self, archetype_resource):
        if len(archetype_resource.equipment) > 0:
            # print(archetype_resource.equipment)
            for item in range(len(archetype_resource.equipment)):
                # print(item)
                # print(archetype_resource.equipment[item])
                assert isinstance(archetype_resource.equipment[item][0], str)
                assert isinstance(archetype_resource.equipment[item][1], int)


class TestSetFeatures:
    
    def test_features_is_dict(self, archetype_resource):
        assert isinstance(archetype_resource.features, dict), "self.features should be a dict"
    
    def test_features_match_level_simple(self, archetype_resource):
        correct_number_of_feats = 0
        
        for level in range(archetype_resource.level):
            correct_number_of_feats += len(archetype_resource.rules["feats"][f'{level+1}'])
            
        assert correct_number_of_feats == len(
            archetype_resource.features
        ), f"Archetype has {len(archetype_resource.features)} feats, should have {correct_number_of_feats}"
        
        
    def test_features_complete(self, archetype_resource):
        
        # Check thorough resource.features that it includes the correct key and description
        # Use key, check in .features, check == between value and key
        
        correct_feats = {}
        for level in range(archetype_resource.level):
            for key in archetype_resource.rules["feats"][f"{level+1}"]:
                correct_feats[key] = archetype_resource.rules["feats"][f"{level+1}"][key]
        
        
          
        for key in archetype_resource.features:
            assert archetype_resource.features[key] == correct_feats[key]
        