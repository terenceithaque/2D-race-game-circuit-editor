"""This script defines a Circuit file representing a circuit and all its data."""


class CircuitGrid:
    """A circuit grid is a matrix with a predefined number of lines and columns. It contains string identifiers referring to blocks located inside that circuit."""
    def __init__(self, nbLines:int=48, nbColumns:int=48) -> None:
        """Intializes the grid with the given number of lines and columns. In its initial state, the grid is a list of lists filled with empty strings."""

        assert nbLines > 0 and nbColumns > 0, "Cannot create a grid with negative number of lines or columns."

        # Grid dimentions
        self.nbLines = nbLines
        self.nbColumns = nbColumns

        # Grid content
        self.content = [[""]*self.nbColumns for _ in range(self.nbLines)]
        print(f"Grid content: {self.content}")


class Circuit:
    """A circuit object."""
    def __init__(self, name:str="New circuit", saveFolder:str="", imageAssetsFolder:str="", nbLines:int=48, nbColumns:int=48):
        """Creates a new circuit."""

        self.name = name
        self.saveFolder = saveFolder # Save location of the circuit
        self.imageAssetsFolder = imageAssetsFolder # Location of the image assets
        self.nbLines = nbLines # Number of lines
        self.nbColumns = nbColumns # Number of columns

        self.grid = CircuitGrid(self.nbLines, self.nbColumns) # Create a grid to store blocks in the circuit

        self.jsonRep = {} # JSON representation of the circuit object
        self.jsonRep["data"] = {} # The 'data' key is the root of the JSON representation
        self.jsonRep["data"] = {
            "metadata":{
                "name":self.name,
                "save_location":self.saveFolder,
                "image_assets_folder":self.imageAssetsFolder,
                "nb_lines":self.nbLines,
                "nb_columns":self.nbColumns

            }
        }

        print(self.jsonRep)