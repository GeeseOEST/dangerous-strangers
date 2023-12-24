#Class definition for the Race class that will become a component of the Character class, created via the CharacterBuilder class

# Has many set_COMPONENT methods as not all fields in JSON exist and therefore the creation requires setting them to empty before then updating to rules so that each class contains all of the expected components

class Race:
    def __init__(self, race) -> None:
        pass
    

    def set_age(self, rules):   # Randomises age, return value and maturity level (potentially?)
        ...
        
    def set_languages(self, rules):     # Sets the standard languages and counts the selectable number of languages for later picking in CharacterBuilder class
        ...
        
    def set_proficiencies():    # Sets the standard proficiencies
        ...
        
    def set_attributes():   # Sets the standard attributes
        ...
        


"""
Components of Race:
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