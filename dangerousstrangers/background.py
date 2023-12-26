#Class definition for the Background class that will become a component of the Character class, created via the CharacterBuilder class

# Has many set_COMPONENT methods as not all fields in JSON exist and therefore the creation requires setting them to empty before then updating to rules so that each class contains all of the expected components

class Background:
    def __init__(self, background) -> None:
        pass
    
    def set_proficiencies(self, rules):    # Set the standard proficiences and + the number of selectable proficiencies for selection in the CharacterBuilder class
        ...
        
    def set_languages(self, rules):    # Set the standard languages and also + the number of selectable languages for selection in the CharacterBuilder class
        ...
    
    def set_equipment(self, rules):    # Sets the list of equipment provided by the background
        ...
        
    def set_money(self, rules):    # Sets the amount of money the character holds based on the background
        ...
        
    def set_features(self, rules):  # Sets the feature list for the character
        ...
    
    
"""
Components of Background:
    background type
    proficiencies
        standard
            armour []
            weapon []
            tool []
            save []
            skill []
        selectable
            armor [(INT), []]
            weapon [(INT), []]
            tool [(INT), []]
            save [(INT), []]
            skill [(INT), []]
    languages
        standard []
        selectable (INT)
    equipment []
    money {coin: quantity}
        CP
        SP
        EP
        GP
        PP
    feature
        {feature: description}

"""