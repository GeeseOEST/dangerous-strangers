import json


def load_top_level_keys(component: str) -> list:
    """Loads in a JSON file, extracts the top-level keys, and then closes the JSON file again.

    Args:
        component (str): The type of the component that should be loaded EG Race

    Returns:
        list: List of all keys in the JSON file at the top level
    """
    if component == "test":
        file_name = "test.json"
    else:
        file_name = f"{component}s.json"

    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"File {file_name} not found in same folder as json_loader"
        )
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file")

    keys = [key for key in data]

    return keys

def load_chosen_component(component_type: str, component: str) -> dict:
    """Loads the randomly selected component into memory for use when creating classes

    Args:
        component_type(str): The type of component that is being addressed EG race
        component (str): The selected component from the above type EG human

    Returns:
        dict: Full dictionary object of everything contained in the JSON description that can be used to create a class of that object
    """
    if component_type == "test":
        file_name = "test.json"
    else:
        file_name = f"{component_type}s.json"
        
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            
        if component in data:
            component_dict = data[component]
        else: 
            raise KeyError(f"Component {component} is not a key in {file_name}")
            
    except FileNotFoundError:
        raise FileNotFoundError(
            f"File {file_name} not found in same folder as json_loader"
        )
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file")
    
    return component_dict