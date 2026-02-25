"""This script defines several special popups for specific operations like creating a circuit."""
from PyQt6.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QGridLayout, QDialogButtonBox


class CreateCircuitPopup(QDialog):
    """A popup asking the user several informations about a circuit to be created (name, dimensions, assets folders, etc.)"""
    def __init__(self):
        super().__init__() # Initialize the QDialog object

        self.setWindowTitle("Create a new circuit")

        parentLayout = QGridLayout() # Set a grid layout for the widgets

        # Circuit name
        self.nameLabel = QLabel("Circuit name:")
        self.nameEdit = QLineEdit()

        # Image assets folder
        self.imageLabel = QLabel("Image assets folder:")
        self.imageEdit = QLineEdit()
        self.imageAssetsButton = QPushButton("Browse...")

        # Standard buttons ("OK" and "Cancel")
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                      QDialogButtonBox.StandardButton.Cancel)

        
        parentLayout.addWidget(self.nameLabel, 0, 0)
        parentLayout.addWidget(self.nameEdit, 0, 1)

        parentLayout.addWidget(self.imageLabel, 1,0)
        parentLayout.addWidget(self.imageEdit, 1,1)
        parentLayout.addWidget(self.imageAssetsButton, 1,2)

        parentLayout.addWidget(button_box)

        


        self.setLayout(parentLayout)

        