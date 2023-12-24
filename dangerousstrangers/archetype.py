import json_loader
import random

#Class definition for the Archetype class that will become a component of the Character class, created via the CharacterBuilder class

class Archetype:
    def __init__(self, archetype, level = 1) -> None:
        
        """Instantiates an object of class Archetype, and then reads the values from JSON files in order to populate the complex components.

        Args:
            archetype (_type_): The Archetype that the character should be 
            level (int, optional): Level that the character should be created at. Defaults to 1.
        """
        
        self.archetype = archetype
        
        rules = json_loader.load_chosen_component("archetype", archetype)

        self.hitdice = rules["hitdice"]
        self.core_stat = rules["core_stat"]
        
        self.proficiencies = {
            "armor": [],
            "weapon": [],
            "tool": [],
            "save": [],
            "skill": [],
        }
        self.optional_proficiencies = {
            "armor": [0, []],
            "weapon": [0, []],
            "tool": [0, []],
            "save": [0, []],
            "skill": [0, []],
        }
        self.equipment = []
        self.features = []

    
    def set_proficiencies(self, rules): # TODO - Work out logic for selecting randomly selectable proficiencies

    # Set standard proficiencies off the bat

        for key in self.proficiencies:
            if key in rules["proficiencies"]["standard"]:
                self.proficiencies[key] = rules["proficiencies"]["standard"][key]

    # Add selectable proficiencies with random choice - Doing this inside individual classes for each component means we will possibly run into duplicate proficiencies. For NPCs it's okay to handwave and say it just provides more randomness, but that needs to be documented or fixed later. Again, might not even be worth it outside of scope of the course stuff.
    # DECISION - Will actually create a third run which is the selectable proficiencies, then in the CharacterBuilder process or inside the Character class will have it combine all three and then select, avoiding any overlap. Need to ensure then that this is implemented.
    # TODO - Logic for adding to this decision list

        ... 


    def select_equipment(self, rules): # TODO - Create logic for selecting equipment - SORT OF DONE BUT NEEDS CHECKING FOR SURE

        
        for item in rules["equipment"]:
            number_of_choices = len(item)
            choice = random.randint(0, number_of_choices - 1)
            self.equipment.append(item[choice]) 

    

    def set_features(self, rules): # TODO - Create logic for adding features appropriate to the level of the character

        ...



    
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