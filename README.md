# dangerous-strangers

A character generator for D&amp;D 5e martial classes, created as a way of exploring different OOP ideas and languages while using a context that I am familiar with (creation of a character following the D&D 5e ruleset).

Currently, this is a fairly opinionated and not completely source-authentic implementation of the 5e rules. This is due to limitations with the 5e SRD, to architectural decisions I made at the start of the project, and also to the amount of time and attention I have available to spend on the project. Therefore I expect it will have limited value to people other than me. However, if I get a request to provide it as a package I will take the time to clean it up and package it properly with a documented way of using it in another project. For now though, feel free to take anything from what I have done and improve upon it or use it for your own project.

## Usage

Calling run_dangerousstrangers.py will return via the stdout a character with a name, age, race, class, background, stats, equipment, proficiencies, and the names of the feats that this character has. These can be referenced against the 5e SRD to get the full texts and contents, or as a way to prompt the imagination for further development by the DM.

## Program Components & Flow

The program makes use of classes to represent a majority of the information. The classes used are;

Race
Archetype
Background
Character
CharacterBuilder

Flow of information is;
run_dangerousstrangers -> randomizes information and provides to CharacterBuilder -> instantiates Character, Race, Archetype, Background -> updates and 'builds' the Character -> is provided to run_dangerousstrangers -> calls print() on the Character -> prints to stdout

### run_dangerousstrangers.py

Calling run_dangerousstrangers.py will generate a random selection of ability scores via the 5e dice roll approach. It also randomly selects a race, an archetype ('class' in 5e terminology), and a background, by loading in the top-level keys in the corresponding JSON files which hold the definitions of the different types. Based on the race, it then selects an appropriate random name from the names.json file, and provides this to the CharacterBuilder. Once the Character class is returned, it prints that out via the standard print() function.

### CharacterBuilder - character_builder.py

The CharacterBuilder class takes in the randomized ability scores, name, race, archetype, and background. It instantiates a blank/default Character object, and then instantiates objects of Race, Archetype, and Character. Then using methods inside the CharacterBuilder class, it combines the three sub-component classes and updates the Character object it created earlier.

### Character - character.py

This class describes the expected attributes for the Character class, and also implements a number of methods prefixed with print_prepare that create the different parts of the output of a character, which are provided to **str** for printing the Character.

### Race - race.py

This contains the calculation for Race class, as well as taking in information from the races.json file which is loaded via json_loader.

### Archetype - archetype.py

This contains the calculation for Archetype class, as well as taking in information from the archetypes.json file which is loaded via json_loader.

### Background - background.py

This contains the calculation for Background class, as well as taking in information from the backgrounds.json file which is loaded via json_loader.

### json_loader.py

Contains the logic for loading in JSON files - as well as some related functions regarding extracting the top-level keys of a JSON file (used mainly to provide the list of options to run_dangerousstrangers that can be selected from as random options, ensuring that the user only needs to update the appropriate JSON file in order to have the component be accessible to the program and avaialble in the random selection list). It also contains logic to switch to test JSON files for running of pytest tests that are written.

### test_XXX

A suite of tests for the different aspects of the program. The tests for the specific classes use mock data in JSON files named appropriately, to ensure consistant results during testing. These mock JSON files comply with the same schema as the regular JSON files which should ensure if the Schema is updated, all of the data files can be validated against it to ensure they stay correct.

## Considerations During Development

As this project was born from a desire to become more comfortable with OOP/classes, I decided early on to use the builder pattern for the creation of these classes, as it made sense to me in theory but the practice of it always felt a little hazy. Therefore, the Character class was a natural way to represent the character itself. I chose to place all of the elements related to selecting a Race, Archetype, and Background, in their coresponding classes, as this is the way that I found felt most natural when walking through the implementation before hand. It mirrors the approach I would take when manually creating a character in real life.

As I progressed, I realised that there were elements that I had not considered, two big examples are spells, and the handling of characters at higher levels where their lower level features are modified and overwritten. I chose to continue with the current implementation in order to have a working PoC, rather than changing how I handled things which would have also expanded the scope. If I was to re-write this, I would use more classes to represent things like spells, equipment, and features, which would allow for more flexibility with their usage and interactions. However, as this would then tie the project more tightly in with the SRD from WotC, I have not yet done so and am not certain I will do that with this project in its current form.

Overall, I have been able to expand my knowledge in usage of classes and JSON files, and now have a much better grasp of the Class concept and how it can help - so I consider this project a definite success even if it closes and does not progress any further.

## Toward The Future

As mentioned, this is currently just a basic implementation of some aspects of the 5e SRD, and the main purpose is for learning and understanding. Longer term, it has the potential to become a larger project if I feel I have the energy, focus, and can see value in it. In the future I would like to try to create additional features for this that can be used to generate random monsters, spells, and magical items. However, it may be better to separate this out from anything using the SRD so that it can have more widespread use.

In order to document my thoughts about what could be done into the future and what would be considered a success now, I wrote the following. As of now, everything in Minimum Components is implemented already.

### Minimum Components - Already implemented/realised as of 31st Dec 2023.

Ability to randomly generate a character, using the rulesets from 5e.

- Race
- Class
- Background

And this should inform;

- Name
- Scores (INT,...) (Shortned from Ability Scores for simplicity)
- Proficiencies
- Saving Throws
- Equipment
- Gold

### Longterm/Future Desires

- Ability to select the subcomponents (EG specify Race but then have the other aspects randomized)
- Add on things such as weight/height/age based on the information already created
- Random name generation using AI or similar meaning there is no need to repeat aspects
- Ability to have the weapons in the starting equipment be combined with stats to inform rolls
- PDF generation of character sheets
- A Web GUI that users can view and print the PDF character sheets from

### Even Further Term

- A set of rules for creating custom monsters, with automatic generation of CR and monster card
- Some type of combat simulation that can be used to put two characters against each other, or a character and a number of monsters, in order to see a simulated outcome
  - This would include some type of averaging, eg 'From 100 fights, the winner was X Y% of the time'

_Disclaimer:_
_This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document.
The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode_
