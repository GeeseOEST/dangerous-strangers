import json_loader
import random

#Class definition for the Archetype class that will become a component of the Character class, created via the CharacterBuilder class

class Archetype:
    def __init__(self, archetype) -> None:
        self.archetype = archetype
        
        rules = json_loader.load_chosen_component("archetype", archetype)

        self.hitdice = rules["hitdice"]
        self.core_stat = rules["core_stat"]
        
        self.proficiencies = {
            "armor": [],
            "weapon": [],
            "tool": [],
            "save": [],
            "skill": []
        }
        self.equipment = []
        self.features = []

    
    def set_proficiencies(self, rules)

    # Set standard proficiencies off the bat

        for key in self.proficiencies:
            if key in rules["proficiencies"]["standard"]:
                self.proficiencies[key] = rules["proficiencies"]["standard"][key]

    # Add selectable proficiencies with random choice - Doing this inside individual classes for each component means we will possibly run into duplicate proficiencies. For NPCs it's okay to handwave and say it just provides more randomness, but that needs to be documented or fixed later. Again, might not even be worth it outside of scope of the course stuff.










# TODO - Work out logic for selecting randomly selectable proficiencies


# TODO - Create logic for selecting equipment - SORT OF DONE BUT NEEDS CHECKING FOR SURE

    for item in rules["equipment"]:
        number_of_choices = len(item)
        choice = random.randint(0, number_of_choices - 1)
        self.equipment.append(item[choice]) 


# TODO - Create logic for adding features appropriate to the level of the character










    
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