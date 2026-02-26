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