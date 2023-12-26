import dangerousstrangers.json_loader
import random

#Class definition for the Archetype class that will become a component of the Character class, created via the CharacterBuilder class

# Has many set_COMPONENT methods as not all fields in JSON exist and therefore the creation requires setting them to empty before then updating to rules so that each class contains all of the expected components

class Archetype:
    def __init__(self, archetype, level=1, test_type=None) -> None:
        
        """Instantiates an object of class Archetype, and then reads the values from JSON files in order to populate the complex components.

        Args:
            archetype (str): The Archetype that the character should be 
            level (int, optional): Level that the character should be created at. Defaults to 1.
            test_type (str, optional): The top-level key to be loaded from the dict, based on the types of test called for in the pytest file. Defaults to None.
        """
        if archetype == "test":
            rules = dangerousstrangers.json_loader.load_test_file("archetype", test_type)
            self.rules = rules # Allows the test files to see what rules the class was based on and compare to final outputs
        else:
            rules = dangerousstrangers.json_loader.load_chosen_component("archetype", archetype)
            
        self.archetype = archetype
        self.level = level
        self.hitdice = rules["hitdice"]
        self.core_stat = rules["core_stat"]
        
        self.proficiencies = {
            "armor": [],
            "weapon": [],
            "tool": [],
            "save": [],
            "skill": [],
        }
        self.selectable_proficiencies = {
            "armor": [0, []],
            "weapon": [0, []],
            "tool": [0, []],
            "save": [0, []],
            "skill": [0, []],
        }
        self.equipment = []
        self.features = {}
        
        self.set_proficiencies(rules)
        self.set_equipment(rules)
        self.set_features(rules)

    
    def set_proficiencies(self, rules): 

        for key in self.proficiencies:
            if key in rules["proficiencies"]["standard"]:
                self.proficiencies[key] = rules["proficiencies"]["standard"][key]

        for key in self.selectable_proficiencies:
            if key in rules["proficiencies"]["selectable"]:
                self.selectable_proficiencies[key] = rules["proficiencies"]["selectable"][key]        



    def set_equipment(self, rules): 
        
        for choice in rules["equipment"]:
            if isinstance(choice[0], list):
                self.equipment.append(random.choice(choice))
            else:
                self.equipment.append(choice)
           
            

    def set_features(self, rules): 

        
        for level in range(self.level):
            level_feats = rules["feats"][f'{level+1}']
            for key in level_feats:
                self.features[key] = level_feats[key]        

        
"""
Components of Archetype:
    archetype type
    hitdice
    core_stat
    proficiencies
        standard
            armor
            weapon
            tool
            save
            skill
        selectable
            armor
            weapon
            tool
            save
            skill
    equipment
        choices
        standard
    features
        level
            feature, ...

"""