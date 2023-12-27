from dangerousstrangers.background import Background
from dangerousstrangers.archetype import Archetype
from dangerousstrangers.race import Race
from dangerousstrangers.character import Character


class CharacterBuilder:
    LANGUAGES = [
        "Common",
        "Dwarvish",
        "Elvish",
        "Giant",
        "Gnomish",
        "Goblin",
        "Halfling",
        "Orc",
        "Abyssal",
        "Celestial",
        "Draconic",
        "Deep Speech",
        "Infernal",
        "Primordial",
        "Sylvan",
        "Undercommon",
    ]
    PROFICIENCY_BONUSES = {
        1: 2,
        2: 2,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 3,
        8: 3,
        9: 4,
        10: 4,
        11: 4,
        12: 4,
        13: 5,
        14: 5,
        15: 5,
        16: 5,
        17: 6,
        18: 6,
        19: 6,
        20: 6,
    }


    def __init__(self, core_components: dict, scores: list) -> None:
        # Will need to have here things like selectable proficiencies, selectable languages etc, so that they are able to be used in the character creation process and just pulled in via self.

        self.character = Character()
        self.character.name = core_components["name"]
        character_race = Race(core_components["race"])
        character_archetype = Archetype(core_components["archetype"])
        character_background = Background(core_components["background"])

        self.set_race(character_race)
        self.set_archetype(character_archetype)
        self.set_background(character_background)
        
        self.combine_ability_scores(character_race, scores)
        self.combine_proficiencies(character_race, character_background, character_archetype)


    def set_race(self, race: Race):
        self.character.race = race.race
        self.character.age = race.age
        self.character.size = race.size
        self.character.speed = race.speed
        
    def set_archetype(self, archetype: Archetype):
        self.character.archetype = archetype.archetype
        self.character.level = archetype.level
        self.character.hitdice = archetype.hitdice
        self.core_stat = archetype.core_stat # Used only inside builder
        
    def set_background(self, background: Background):
        self.character.background = background.background
        self.character.money = background.money


    def combine_ability_scores(self, race: Race, scores: list):
        
        highest_score = max(scores)
        self.character.ability_scores[self.core_stat] = highest_score
        scores.remove(highest_score)
        
        for key in self.character.ability_scores:
            if key != self.core_stat:
                score = scores[0]
                self.character.ability_scores[key] = score
                scores.remove(score)
            
        for key in self.character.ability_scores:
            self.character.ability_scores[key] += race.ability_score_modifiers[key]


    def combine_proficiencies(
        self, race: Race, background: Background, archetype: Archetype
    ):
        for key in self.character.proficiencies:
            self.character.proficiencies[key] += race.proficiencies[key]
            self.character.proficiencies[key] += archetype.proficiencies[key]
            self.character.proficiencies[key] += background.proficiencies[key]

        self.selectable_proficiencies = {
            "armor": [0, []],
            "weapon": [0, []],
            "tool": [0, []],
            "save": [0, []],
            "skill": [0, []],
        }
        
        for key in self.character.proficiencies:
            if archetype.selectable_proficiencies[key][0] != 0:
                self.selectable_proficiencies[key] = archetype.selectable_proficiencies[key]
            if background.selectable_proficiencies[key][0] != 0:
                self.selectable_proficiencies[key][0] += background.selectable_proficiencies[key][0]
                self.selectable_proficiencies[key][1] += background.selectable_proficiencies[key][1]


    def combine_equipment(
        self, race: Race, background: Background, archetype: Archetype
    ):
        ...

    def combine_languages(
        self, race: Race, background: Background, archetype: Archetype
    ):
        ...

    def combine_attributes_and_features(
        self, race: Race, background: Background, archetype: Archetype
    ):
        ...

    def select_proficiencies(self):
        ...

    def select_langauges(self):
        ...

    def calc_proficiency_bonus(self):
        ...

    def calc_check_modifiers(self):
        ...

    def build(self):
        return self.character