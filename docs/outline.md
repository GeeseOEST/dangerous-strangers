*This is just an internal note for myself to work on the outline and try to think 'out-loud' as far as how I will be approaching the topic. I guess if you would like to see what the inside of my brain looks like this might be as good a place as any to start.*

# Brain Dump

## Happy Path

User calls program
    May or may not specify a component to use for one of the selectable aspects
        (Name, Race, Class, Background)
        Long term also want to be able to specify stat generation method, to begin with will use rolled since it's most fun and provides an additional bit of interest to the implementation for me to create

Specified components are combined with randomization to get the full list
    **Randomization of name cannot happen at this point - will need to work out a different approach to this**
    Will need to wait here for the base stats to be created, so save these details as a tuple perhaps? Or as a dict to ensure no funny business down the line.

Base Stats Rolled
    Will be either point buy, random from the standard array, or rolled. 
    Need to check what is allowed via OGL/what is referenced there
    Will be stored in a list/tuple as the order is not important, since later on they will be re-ordered from flags based in Class

CharacterBuilder will be called at this point
    Fed the information from the user and the randomization section
    Runs and passes each bit of information off to methods to set race, set class, set background, set name (here can be the randomization for the name if required) 

Set Race
    Takes info from a races.json file as a dict of structires, where KEY == Race Name and VALUE == Structure of all that will change
    Identifies correct race and then applies features

Set Class
    Does the same as set race from a classes.json file

Set Background
    Gets information from the same location, as in a background.json file
    Also adds the starting equipment and gold to the character
        In the future can be extended to provide the traits/ideals/bonds/flaws/whatever but that is probably outside of the SRD and also a 'desire' not a need

Builder then returns the object of the character class

Returned character object is printed
    Initially just in terminal, however the first QOL improvement here would be to create a PDF for the user and save it into the user directory.
        This will be somewhat complicated since there will be a lot of bouncing around the sheet, but there are surely libraries like FPDF that can assist with this
        Maybe there is a way to have a form-fillable PDF filled using a set of labelled variables, which would be convenient
            would just need to make an adaptor from the Character class to whatever the variables required to fill in the PDF are

## Test Locations

Where can tests be done in order to ensure appropriate working of the system?
