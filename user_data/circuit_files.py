"""This script handles common operations on circuit files.
Circuit files contains serialized JSON data reflecting the entire state of a circuit."""
import os
import json
import user_data.sanitize_filenames
import user_data.circuit



def check_structure_validity(json_file:str) -> bool:
    """Returns True if the given JSON file has a valid data structure for a Circuit object, otherwise returns False."""

    root_key = "data" # Expected root key for the JSON structure

    keys = ["metadata"] # Expected keys inside the JSON structure

    # Load the JSON file
    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)


    # Check if the root key is not present
    if not root_key in json_data:
        return False
    
    json_structure = json_data[root_key] # Get the JSON structure contained by the root key
    if not any([key in json_structure] for key in keys):
        return False
    
    return True

def open_circuit(file_path:str) -> dict:
    """Opens the given JSON circuit file and returns the dictionnary describing that circuit."""

    abs_file_path = os.path.abspath(file_path) # Absolute file path

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            circuit_data = json.load(f)

        return circuit_data
    
    except:
        circuit_data = {}  
        return circuit_data      




def save_circuit(circuit:user_data.circuit.Circuit) -> None:
    """Saves the given Circuit object to a JSON file.
    The save location and the file name are determined using the metada inside the JSON representation of that Circuit object."""

    # Get the metada inside the JSON representation of the circuit
    metadata = circuit.jsonRep["data"]["metadata"]

    circuit_name = metadata["name"] # Circuit name
    save_location = metadata["save_location"] # Save location as absolute path
    
    file_name = user_data.sanitize_filenames.sanitize_filename(circuit_name + ".json") # Sanitize the circuit's name to get the final file name

    file_path = os.path.join(save_location, file_name) # Full file path

    print(file_path)
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(circuit.jsonRep, f, indent=4, ensure_ascii=False)
        f.close()




