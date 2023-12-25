import json
import os


def load_top_level_keys(file_name: str) -> list:
    """Loads in a JSON file, extracts the top-level keys, and then closes the JSON file again.

    Args:
        component (str): The type of the component that should be loaded EG Race

    Returns:
        list: List of all keys in the JSON file at the top level
    """
    if file_name == "test":
        file_name = "test.json"
    else:
        file_name = f"{file_name}s.json"  # JSON files are named with plurals however keywords in .py are not, so the s handles this. Not the best solution long term.

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


def load_chosen_component(file_name: str, top_level_key: str) -> dict:
    """Loads a subset of a json file based on top-level key.

    Only the sub-levels that correspond to the top-level key will be loaded to avoid loading the full JSON file into memory just to get access to a predictable subsection.

    Args:
        component_type(str): The type of component that is being addressed EG race
        component (str): The selected component from the above type EG human

    Returns:
        dict: Full dictionary object of everything contained in the JSON description that can be used to create a class of that object
    """
    if file_name == "test":
        file_name = "test.json"
    else:
        file_name = f"{file_name}s.json"

    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        if top_level_key in data:
            component_dict = data[top_level_key]
        else:
            raise KeyError(f"Component {top_level_key} is not a key in {file_name}")

    except FileNotFoundError:
        raise FileNotFoundError(
            f"File {file_name} not found in same folder as json_loader"
        )
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file")

    return component_dict



def load_test_file(mock_type: str, top_level_key: str) -> dict:
    
    file_name = mock_type + "s_mock.json"
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            
        if top_level_key in data:
            component_dict = data[top_level_key]
        else:
            raise KeyError(f"Component {top_level_key} is not a key in {file_name}")

    except FileNotFoundError:
        print("Current Working Directory: ", os.getcwd())
        raise FileNotFoundError(
            f"File {file_name} not found in same folder as json_loader"
        )
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file")

    return component_dict