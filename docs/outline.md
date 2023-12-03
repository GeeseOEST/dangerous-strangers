*This is just an internal note for myself to work on the outline and try to think 'out-loud' as far as how I will be approaching the topic. I guess if you would like to see what the inside of my brain looks like this might be as good a place as any to start.*

Information in () are relevant information or examples
Information in *()* are bonus content thoughts that came after typing the line or at another time, on behalf of my brain

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

*Where can tests be done in order to ensure appropriate working of the system?*

Randomization of the classes
    Check that if run multiple times it does not return the same class infinitely
        Perhaps create a set, run the randomization multiple times and add the class/race/background to separate sets
        Then confirm that length of set is not 1
            There will be a statistically unlikely scenario where this still is == 1 but at that point you can run the test again and it will pass
                (Although I feel this is **bad** test design there may not be a better way, at least not that I can think of right now)
    Check that if given an input it does always return that class

Rolling Of Stats
    Check that if using the roll approach, an appropriate set of stats comes out
        Not too high/unrealistically high
        Not all identical
        Length of the list is 6
    Check that with point buy total sum of stats is not greater than points
    Check with standard array that the standard array is returned (not much more done here so easy enough to check)
        Could move the Standard Array out of this function to ensure no 'magic numbers' used, and then feed it a different standard array to test (worth it? Does this add any value?)
    Check that when done twice with random the numbers are not identical
        Again has the problem of statistical failure one day, but again I think this is unlikely enough that I can tolerate it (But for the future knowledge try to understand why this happens)

Printing of character
    Should provide a mocked object for this, since you need to know what the output is. Also good to practice mocking objects.

CharacterBuilder behavious
    This will be harder to mock and learn how it should work, but is also a more realistic scenario for the future that could show you what you do / do not need to do in a production environment or when working with a project that has multiple important classes, so this is something that you really should work out how to do for your own learning.

## Order Of Operations / Development

*Where should I start? What should I start with? What should I leave for later?*

Given the intention to do some TDD, I believe that I would be best suited to create the tests before writing the code.
However, since I want to use .json files to add in the functionality I will require, then I should also work out the format of those files
I also need to work out what the classes will look like if I am to test them properly - however I think testing the classes is going to be secondary to testing the functions in the main file, since that will have to be done before I can move on.
Working on the class definition stuff is more interesting but I think that might be best left for once I have already got the initial stuff in place, so that I can feel like I've made a strong start - I also need to make sure I'm able to build up the surrounding 'infrastructure' for the classes before I start on them, otherwise I won't really be able to do anything useful with them.

So, all that in mind, I will approach it as such;

1. Flesh out the main file with the functions that will need to be written and a comment on what they'll do
2. Add to each of these functions an expected set of arguments and a return value
3. Write the overview of the simple tests as suggested above (excluding mocking the classes)
4. Write those test so that they fail but predictably so
5. Create a simple version of the .json files for use with these initial functions *(added due to realisation in following paragraph)*
6. Implement the functions in the main file so that the tests begin to pass *(classic Red-Green-Red TDD at least from my understanding)*
7. Learn how to test the classes directly, create those tests
8. Once all of the core functions in the main file work, I can start to work on the class and the class builder
    1. Create the .json files or at least flesh them out further
    2. Create the Character class and have it set everything to 0
    3. Create the CharacterBuilder class 
    4. This is where the exciting stuff happens but I will leave that for the future 

I believe I will find things that will clash with this - for example, the class names will need to be available for the randomizer otherwise it won't be able to select which class it should use. This could be avoided by just letting it pick random numbers, however that will make it harder to test later since I may need to follow the path of the class to confirm. I don't want to have a magic number anywhere if avoidable, so it will probably be best to load in the class options JSON and then extract out the keys, add them to a list that can then be used in the rest of the program, and then close that JSON until needed again. The memory will be freed during that time, however will need a second load cycle which might not be most efficient. At this stage I think it's better to be explicit about what is being used and when rather than trying to minimize all load times, since the overall program will be small, but I can imagine this would be a bigger topic later down the line.