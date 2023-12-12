import random
import json_loader

"""
Takes in the user info, randomizes the other components, and then sends it to the CharacterBuilder class. Once finished, this recieves that back and then prints it out. 
This somewhat makes this file complex as we're not taking the randomization or printing/exporting logic out.I would like to do in order to be able to have some type of adaptor/dependency injection/whatever to be able to substitute different ways of export (pdf, print, view in web page, ...) but for now is a requirement of the CS50 approach to submitting a final project.
"""

def main():
    roll_scores()


# TODO - Define function to take in and filter through user input


def select_characteristics() -> dict:
    """
    Creates a list of characteristics combined from user-generated input and randomized choices.

    TODO - In future this should check the args with the above filter input function, for now it will just randomize directly and that's it

    select_charcteristics() takes any preselections from the user, then combines them with randomized scores for the others, and then returns the set of characteristics required to make a character. Does not take in the name from the user as this is not applied at this stage.

    Returns:
        dict: 'names':{'first_name', 'last_name'}, 'race':_, 'class':_, 'background':_
    """

    core = randomize_characteristics()
    name = select_name(core["race"])

    characteristics = core
    characteristics["name"] = name

    return characteristics


def randomize_characteristics() -> dict:
    """
    Selects random characteristics and provides them for later use.

    Loads in individual json files that contain the races, classes, and backgrounds available in the ruleset.

    Returns:
        dict: 'race':_, 'class':_, 'background':_
    """
    ...
    return characteristics


def select_name(race: str) -> dict:
    """
    Selects names based on the race of the character from a preprepared list stored as a .json file.

    Args:
        race (str): Race of the character

    Returns:
        dict: 'first_name':_, 'last_name':_
    """
    ...
    return name


def set_scores() -> list:
    """
    set_scores() generates the scores for the character. To begin with this will always just call roll_scores, but in the future it could also call point buy or standard array if required.

    Returns:
        list: 6 ints
    """
    scores = roll_scores()
    return scores


def roll_scores() -> list:
    """
    Rolls dice to create randomized scores, and then returns a list of 6 scores.

    In 5e, each character's ability scores can be determined by rolled dice. The approach is to roll 4 d6, drop the lowest number, and add them together. This is done 6 times as there are 6 core ability scores.

    Returns:
        list: 6 ints
    """
    scores = []

    for _ in range(6):
        four_d6 = []
        for _ in range(4):
            four_d6.append(random.randint(1, 6))
        lowest_roll = min(four_d6)
        four_d6.remove(lowest_roll)
        score = sum(four_d6)
        scores.append(score)

    return scores


'''DOCUMENTED OUT WHILE WAITING FOR CHARACTER IMPLEMENTATION
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
'''


if __name__ == "__main__":
    main()
