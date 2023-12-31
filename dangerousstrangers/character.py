# Just the character definition. Should only include methods that are called when USING the character, not when creating the character
# Created by the CharacterBuilder class
# Takes no arguements as all it needs to do is create the empty attributes, they will be set with the CharacterBuilder


class Character:
    def __init__(self):
        self.race = ""
        self.archetype = ""
        self.background = ""
        self.level = 0
        self.proficiency_bonus = 0

        self.age = 0
        self.name = {"first": "", "last": ""}
        self.alignment = ""  # Not yet used
        self.size = ""
        
        self.speed = 0
        self.hitdice = 0
        self.armor_class = 0 # Not yet used
        self.armor = ""

        self.ability_scores = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0,
        }
        self.check_modifiers = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0,
        }
        self.skills = {
            "acrobatics": 0,
            "animal handling": 0,
            "arcana": 0,
            "athletics": 0,
            "deception": 0,
            "history": 0,
            "insight": 0,
            "intimidation": 0,
            "investigation": 0,
            "medicine": 0,
            "nature": 0,
            "perception": 0,
            "performance": 0,
            "persuasion": 0,
            "religion": 0,
            "sleight of hand": 0,
            "stealth": 0,
            "survival": 0,
        }
        self.proficiencies = {
            "armor": [],
            "weapon": [],
            "tool": [],
            "save": [],
            "skill": [],
        }
        self.saves = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0,
        }
        
        self.languages = ["fuck", "me", "bitte"]
        self.equipment = []
        self.weapons = []
        self.money ={
            "CP": 0,
            "SP": 0,
            "EP": 0,
            "GP": 0,
            "PP": 0
        }   
        self.features = []
        
    def __str__(self):
        # Combine elements
        # Return STR that has those elements combined
        
             
        character_headline = self.print_prepare_headline()
        character_attributes = self.print_prepare_attributes()
        character_skill_proficiencies = self.print_prepare_skill_proficiencies()
        
        output_components = ["", "", character_headline, "", character_attributes, "", character_skill_proficiencies]
        
        complete_output = "\n".join(output_components)
        
        return complete_output
        
        
    def print_prepare_headline(self):
        '''
        Should be:
            FIRST NAME  LAST NAME
        RACE    ARCHETYPE   BACKGROUND
        '''
        
        name_line = f"{self.name["first"] + ' ' + self.name["last"]:^60}" #60
        core_line = f"{self.race.capitalize():>19} {self.archetype.capitalize():^20} {f"{self.background.capitalize()} {self.level}":<20}" # 60
        header_line = name_line + "\n" + core_line
        
        return header_line
    
    
    def print_prepare_attributes(self):
        title_line = "" # Ends up 6 x 10 long == 60
        score_line = "" # Ends up 6 x 10 long == 60
        
        for key in self.ability_scores:
            title = f"{key:^10}"
            check_modifier = f"{self.check_modifiers[key]:+}"
            ability_score = f"({self.ability_scores[key]})"
            content = f"{f"{check_modifier} {ability_score}":^10}"
            title_line += title
            score_line += content
        
        output_line = title_line + "\n" + score_line
        
        return output_line
    
    def print_prepare_skill_proficiencies(self):
        # go through proficiencies and for any that exist, grab their relevant score from the array
        # do 3 per line, so 20 char per thing
        
        proficiencies_added = 0
        proficiencies_line = ""
        
        for skill in self.proficiencies["skill"]:
            prof_phrase = f"{skill.capitalize()} {self.skills[skill]:+}"
            proficiencies_added += 1
            if proficiencies_added%3 != 0:
                proficiencies_line += f"{prof_phrase:^20}"
            else:
                proficiencies_line += f"{prof_phrase:^20}\n"

        return proficiencies_line