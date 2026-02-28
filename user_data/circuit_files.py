"""This script handles common operations on circuit files.
Circuit files contains serialized JSON data reflecting the entire state of a circuit."""
import os
import json
import user_data.sanitize_filenames
import user_data.circuit

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




