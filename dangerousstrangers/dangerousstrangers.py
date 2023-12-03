"""
Takes in the user info, randomizes the other components, and then sends it to the CharacterBuilder class. Once finished, this recieves that back and then prints it out. 
This somewhat makes this file complex as we're not taking the randomization or printing/exporting logic out.I would like to do in order to be able to have some type of adaptor/dependency injection/whatever to be able to substitute different ways of export (pdf, print, view in web page, ...) but for now is a requirement of the CS50 approach to submitting a final project.
"""
 
 
"""
TODO - All of the below
Functions required here;
    **HOLD - Not the simplest, so to begin with will not implement this.** Take input from user - Somewhat Outlined
    Randomize any aspectsuser hasn't provided via args - Outlined
    Roll Stats - Outlined
    Hand all off to CharacterBuilder class
    Print the character - Outlined
""" 
 

def main():
    ... 

   
# TODO - Define function to take in and filter through user input

def select_characteristics() -> dict: 
    """ 
    Creates a list of characteristics combined from user-generated input and randomized choices.
    
    NOTE - Not sure if should be done just inside the select_characteristics function or if it should have a secondary function for that purpose   
    TODO - In future this should check the args with the above filter input function, for now it will just randomize directly and that's it 
    
    select_charcteristics() takes any preselections from the user, then combines them with randomized stats for the others, and then returns the set of characteristics required to make a character. Does not take in the name from the user as this is not applied at this stage.
    
    Returns:
        dict: Race, Class, Background
    """
    ...
    return characteristics


def randomize_characteristics() -> dict:
    """
    Selects random characteristics and provides them for later use.
    
    Loads in individual json files that contain the races, classes, and backgrounds available in the ruleset.
    
    Returns:
        dict: Race, Class, Background
    """
    ...
    return characteristics


def select_name(race: str) -> dict:
    """_summary_

    Args:
        race (str): Race of the character

    Returns:
        dict: first_name, last_name
    """
    ...
    return name


def set_stats() -> list:
    """
    set_stats() generates the stats for the character. To begin with this will always just call roll_stats, but in the future it could also call point buy or standard array if required.
    
    Returns:
        list: list of 6 ints
    """
    statistics = roll_stats()
    return statistics


def roll_stats() -> list:
    """
    Rolls dice to create randomized stats, and then returns a list of 6 stats.
    
    In 5e, each character stat can be made up of rolled dice. The approach is to roll 4 d6, drop the lowest number, and add them together. This is done 6 times as there are 6 core stats.
    
    Returns:
        list: list of 6 ints
    """
    rolls = []
    ...
    return rolls 


def print_character(character: Character) -> str:
    """
    Provides an aesthetically pleasing formated character description to be printed out.
    
    Returns a string rather than printing inside the function to avoid using side-effects for functionality, and therefore allows for proper unit testing.

    Args:
        character (Character): This object is the previously generated instance of the Character class that the program has created earlier

    Returns:
        str: A multi-line f string that contains all of the information about the character, ready to be used by the generator of the character
    """
    
    ...
    return print_ready_character



if __name__ == '__main__':
    main()