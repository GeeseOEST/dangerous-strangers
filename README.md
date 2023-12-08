# dangerous-strangers
A character generator for D&amp;D 5e, created as a way of exploring different OOP ideas and languages while using a context that I am familiar with (creation of a character following the D&D 5e ruleset).

## Roadmap/Hope

While this will start as a minimum implementation and the main purpose is for learning and understanding, it has the potential to become a larger project if I feel I have the energy, focus, and can see value from it. As it stands it will rely heavily on the SRD and therefore will need to be quite specific in what's included. However, as time goes by and once it reaches the stage of automated generation of monsters etc, it may be able to become something standalone that just uses terms from the SRD and is therefore less likely to be taken down.

To try to be explicit with my intentions; 

### Minimum Components;

- Ability to randomly generate a character, using the rulesets from 5E 
    The aspects of this will therefore be;
        Race
        Class
        Background

    And this should inform;
        Name
        Scores (INT,...) (Shortned from Ability Scores for simplicity)
        Proficiencies
        Saving Throws
        Equipment
        Gold

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


*Disclaimer:*
*This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. 
The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode*