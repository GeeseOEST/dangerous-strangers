from dangerousstrangers.background import Background
from dangerousstrangers.archetype import Archetype
from dangerousstrangers.race import Race
from dangerousstrangers.character import Character

class CharacterBuilder:
    
    def __init__(self, core_components: dict, scores: list) -> None:
        
        # Will need to have here things like selectable proficiencies, selectable languages etc, so that they are able to be used in the character creation process and just pulled in via self.
        
        pass
    
    
    def set_race(self, race: Race):
        ...
    
    def set_background(self, background: Background):
        ...
        
    def set_archetype(self, archetype: Archetype):
        ...
        
    def combine_ability_scores(self, race: Race, scores: list):
        ...
        
    def combine_proficiencies(self, race: Race, background: Background, archetype: Archetype):
        ...        
        
    def combine_equipment(self, race: Race, background: Background, archetype: Archetype):
        ... 
        
    def combine_languages(self, race: Race, background: Background, archetype: Archetype):
        ...
        
    def combine_attributes_and_features(self, race: Race, background: Background, archetype: Archetype):
        ...

        
    def select_proficiencies(self):
        ...
        
    def select_langauges(self):
        ...
        
        
    def calc_proficiency_bonus(self):
        ...
    
    def calc_check_modifiers(self):
        ...