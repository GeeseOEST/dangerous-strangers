import json_loader

#Class definition for the Race class that will become a component of the Character class, created via the CharacterBuilder class

# Has many set_COMPONENT methods as not all fields in JSON exist and therefore the creation requires setting them to empty before then updating to rules so that each class contains all of the expected components

class Race:
    def __init__(self, race, test_type=None) -> None:
        
        ability_scores = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        proficiency_types = ["armor", "weapon", "tool", "save", "skill"]
        
        if race == "test":
            rules = json_loader.load_test_file("race", test_type)
            self.rules = rules # Allows the test files to see what rules the class was based on and compare to final outputs
        else:
            rules = json_loader.load_chosen_component("race", race)
        
        # Sets everything to intialized so all Race classes have the same attributes for adding together later
        
        self.race = race
        self.age = 0
        self.size = rules["size"]
        self.speed = rules["speed"]
        self.ability_score_modifiers = {}
        self.languages = []
        self.language_choices = 0
        self.proficiencies = {}
        self.attributes = {}
        
        for score in ability_scores:
            self.ability_score_modifiers[score] = 0
        
        for proficiency in proficiency_types:
            self.proficiencies[proficiency] = []
                  
        
    def set_ability_scores(self, rules):    # Updates ability scores
        ...
    
    def set_age(self, rules):   # Randomises age, return value and maturity level (potentially?)
        ...
        
    def set_languages(self, rules):     # Sets the standard languages and counts the selectable number of languages for later picking in CharacterBuilder class
        ...
        
    def set_proficiencies(self, rules):    # Sets the standard proficiencies
        ...
        
    def set_attributes(self, rules):   # Sets the standard attributes
        ...
        


"""
Components of Race:
    race type
    ability_score_modifiers
    age_range [adult, death]
    size
    languages
        standard
        selectable (INT)
    proficiencies
        armor []
        weapon []
        tool []
        save []
        skill []
    attributes 
        {name : attribute}
    
"""