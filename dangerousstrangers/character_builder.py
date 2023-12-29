from dangerousstrangers.background import Background
from dangerousstrangers.archetype import Archetype
from dangerousstrangers.race import Race
from dangerousstrangers.character import Character
import random


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
    ARMOR_TYPES = {
        "light": ["Padded", "Leather", "Studded Leather"],
        "medium": ["Hide", "Chain Shirt", "Scale Mail", "Breastplate", "Half Plate"],
        "heavy": ["Ring Mail", "Chain Mail", "Splint", "Plate"],
    }
    WEAPON_TYPES = {
        "Simple Melee": [
            "Club",
            "Dagger",
            "Greatclub",
            "Handaxe",
            "Javelin",
            "Light Hammer",
            "Mace",
            "Quarterstaff",
            "Sickle",
            "Spear",
        ],
        "Simple Ranged": [
            "Light Crossbow", 
            "Dart", 
            "Shortbow", 
            "Sling"
        ],
        "Martial Melee": [
            "Battleaxe",
            "Flail",
            "Glaive",
            "Greataxe",
            "Greatsword",
            "Halberd",
            "Lance",
            "Longsword",
            "Maul",
            "Morningstar",
            "Pike",
            "Rapier",
            "Scimitar",
            "Shortsword",
            "Trident",
            "War Pick",
            "Warhammer",
            "Whip",
        ],
        "Martial Ranged": [
            "Blowgun",
            "Hand Crossbow",
            "Heavy Crossbow",
            "Longbow",
            "Net",
        ],
    }
    SKILL_INHERITANCE = {
        "acrobatics": "DEX",
        "animal handling": "WIS",
        "arcana": "INT",
        "athletics": "STR",
        "deception": "CHA",
        "history": "INT",
        "insight": "WIS",
        "intimidation": "CHA",
        "investigation": "INT",
        "medicine": "WIS",
        "nature": "INT",
        "perception": "WIS",
        "performance": "CHA",
        "persuasion": "CHA",
        "religion": "INT",
        "sleight of hand": "DEX",
        "stealth": "DEX",
        "survival": "WIS"
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
        self.combine_proficiencies(
            character_race, character_background, character_archetype
        )
        self.combine_equipment(character_background, character_archetype)
        self.combine_languages(character_race, character_background, character_archetype)
        self.combine_attributes_and_features(character_race, character_background, character_archetype)
        
        self.calc_check_modifiers()
        self.calc_proficiency_bonus()
        self.calc_saves()

    def set_race(self, race: Race):
        self.character.race = race.race
        self.character.age = race.age
        self.character.size = race.size
        self.character.speed = race.speed

    def set_archetype(self, archetype: Archetype):
        self.character.archetype = archetype.archetype
        self.character.level = archetype.level
        self.character.hitdice = archetype.hitdice
        self.core_stat = archetype.core_stat  # Used only inside builder

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
                self.selectable_proficiencies[key] = archetype.selectable_proficiencies[
                    key
                ]
            if background.selectable_proficiencies[key][0] != 0:
                self.selectable_proficiencies[key][
                    0
                ] += background.selectable_proficiencies[key][0]
                self.selectable_proficiencies[key][
                    1
                ] += background.selectable_proficiencies[key][1]

        self.select_proficiencies()

    def combine_equipment(self, background: Background, archetype: Archetype):
        self.character.equipment += archetype.equipment
        self.character.equipment += background.equipment

        self.generate_weapon()
        self.apply_weapon()
        self.apply_armor()

    def generate_weapon(self):
        weapon_options = self.WEAPON_TYPES
        
        removed_items = []
        
        for item in self.character.equipment:
            simple = False
            martial = False
            ranged = False
            melee = False
            
            item_lower = item[0]
            item_lower = item_lower.lower()
            
            if "martial" in item_lower:
                martial = True
            if "simple" in item_lower:
                simple = True
            if "ranged" in item_lower:
                ranged = True
            if "melee" in item_lower:
                melee = True
            
            weapon_picked = ["",0]
            
            if martial == True:
                if ranged == True:
                    weapon_picked[0] = random.choice(weapon_options["Martial Ranged"])
                elif melee == True:
                    weapon_picked[0] = random.choice(weapon_options["Martial Melee"])
                else:
                    weapon_picked[0] = random.choice(weapon_options["Martial Melee"] + weapon_options["Martial Ranged"])
            
            if simple == True:
                if ranged == True:
                    weapon_picked[0] = random.choice(weapon_options["Simple Ranged"])
                elif melee == True:
                    weapon_picked[0] = random.choice(weapon_options["Simple Melee"])
                else:
                    weapon_picked[0] = random.choice(weapon_options["Simple Melee"] + weapon_options["Simple Ranged"])
            
            weapon_picked[1] = item[1]
            
            if weapon_picked[0] != "":
                removed_items.append(item)
                self.character.equipment.append(weapon_picked)
                
        for item in removed_items:
            self.character.equipment.remove(item)
                    
    def apply_weapon(self):
        
        weapon_options = self.WEAPON_TYPES         
        
        for item in self.character.equipment:        
            if not isinstance(item, list):
                continue
        
            item_name = ""
            if item[0][-1] == "s":
                item_name = item[0][:-1]
            else:
                item_name = item[0]
            for key in weapon_options:
                if item_name not in weapon_options[key]:
                    continue
                self.character.weapons.append(item_name)
            
    def apply_armor(self):
        armor_options = []
        for key in self.ARMOR_TYPES:
            armor_options += self.ARMOR_TYPES[key]
        for item in self.character.equipment:
            if item in armor_options:
                self.character.armor = item

    def combine_languages(
        self, race: Race, background: Background, archetype: Archetype
    ):
        try:
            self.character.languages = background.languages + race.languages
        except AttributeError:
            pass
        
        self.language_choices = 0
        
        if race.language_choices != 0:
            self.language_choices += race.language_choices
            
        if background.language_choices != 0:
            self.language_choices += background.language_choices
        
        if self.language_choices != 0:
            for _ in range(self.language_choices):
                self.character.languages.append(random.choice(self.LANGUAGES))
        
        self.character.languages = set(self.character.languages)
        

    def combine_attributes_and_features(
        self, race: Race, background: Background, archetype: Archetype
    ):
        self.character.features = race.attributes | background.features | archetype.features


    def select_proficiencies(self):
        for key in self.selectable_proficiencies:
            # Overly verbose but it helps step through the stages as it selects how to do it.
            number_choices = self.selectable_proficiencies[key][0]
            choices = set(self.selectable_proficiencies[key][1])
            current_proficiencies = set(self.character.proficiencies[key])
            actual_choices = list(choices - current_proficiencies)

            for _ in range(number_choices):
                random_proficiency = random.choice(actual_choices)
                self.character.proficiencies[key].append(random_proficiency)

    def calc_proficiency_bonus(self):
        for skill in self.character.skills:
            attribute_controlling = self.SKILL_INHERITANCE[skill]
            self.character.skills[skill] = self.character.check_modifiers[attribute_controlling]
            if skill in self.character.proficiencies["skill"]:
                    self.character.skills[skill] += self.PROFICIENCY_BONUSES[self.character.level]

    def calc_check_modifiers(self):
        for ability, score in self.character.ability_scores.items():
            modifier = (score - 10)/2
            if modifier.is_integer():
                self.character.check_modifiers[ability] = int(modifier)
                continue
            
            modifier -= modifier%1
            self.character.check_modifiers[ability] = int(modifier)

    def calc_saves(self):
        for save in self.character.saves:
            self.character.saves[save] = self.character.check_modifiers[save]
            try:
               if save in self.character.proficiencies["save"]:
                    self.character.saves[save] += self.PROFICIENCY_BONUSES[self.character.level]                
            except KeyError: 
               pass

    def build(self):
        return self.character
