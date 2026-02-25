"""This script defines several special popups for specific operations like creating a circuit."""
from PyQt6.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QGridLayout, QDialogButtonBox, QFileDialog

class CreateCircuitPopup(QDialog):
    """A popup asking the user several informations about a circuit to be created (name, dimensions, assets folders, etc.)"""
    def __init__(self):
        super().__init__() # Initialize the QDialog object

        self.setWindowTitle("Create a new circuit")

        parentLayout = QGridLayout() # Set a grid layout for the widgets

        # Circuit name
        self.nameLabel = QLabel("Circuit name:")
        self.nameEdit = QLineEdit()
        self.nameEdit.setPlaceholderText("Circuit name...")

        # Image assets folder
        self.imageLabel = QLabel("Image assets folder:")
        self.imageEdit = QLineEdit()
        self.imageEdit.setPlaceholderText("Image assets folder...")

        self.imageAssetsButton = QPushButton("Browse...")

        self.imageAssetsButton.clicked.connect(self.browseImages)

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


    def browseFolder(self, dialogTitle:str="Browse folder") -> str:
        """Allows the user to browse folders and returns the absolute path of the selected folder.
        - dialogTitle: the title of the dialog window."""

        dialog = QFileDialog() # Dialog to browse folders
        dialog.setFileMode(QFileDialog.FileMode.Directory) # Configure the file dialog to accept only directories
        dialog.setWindowTitle(dialogTitle)

        opened_folder = dialog.exec()

        if opened_folder:
            print(dialog.selectedFiles()[0])
            return dialog.selectedFiles()[0] # Return the absolute path to the directory
        
        else:
            return ""
        

    def browseImages(self) -> str:
        """Allows the user to browse folders containing images an returns the absolute file path of the selected folder."""

        folder_path = self.browseFolder("Select a folder containing image assets")

        # Change the text in the imageEdit widget only if the user selected a valid folder
        if folder_path != "":
            self.imageEdit.setText(folder_path)


        return folder_path    



        