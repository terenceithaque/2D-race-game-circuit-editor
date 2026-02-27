"""This script defines a Circuit file representing a circuit and all its data."""


class Circuit:
    """A circuit object."""
    def __init__(self, name:str="New circuit", saveFolder:str="", imageAssetsFolder:str="", nbLines:int=48, nbColumns:int=48):
        """Creates a new circuit."""

        self.name = name
        self.saveFolder = saveFolder # Save location of the circuit
        self.imageAssetsFolder = imageAssetsFolder # Location of the image assets
        self.nbLines = nbLines # Number of lines
        self.nbColumns = nbColumns # Number of columns

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