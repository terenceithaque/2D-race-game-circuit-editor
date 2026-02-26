"""This script defines a popup allowing to crate a new circuit"""
from PyQt6.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QGridLayout, QDialogButtonBox, QFileDialog, QMessageBox, QSpinBox
import os

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
        self.nameEdit.setText("New circuit")

        # Image assets folder
        self.imageLabel = QLabel("Image assets folder:")
        self.imageEdit = QLineEdit()
        self.imageEdit.setPlaceholderText("Image assets folder...")
        self.imageEdit.setReadOnly(True)

        self.imageAssetsButton = QPushButton("Browse...")

        self.imageAssetsButton.clicked.connect(self.browseImages)


        # Save location
        self.saveLocationLabel = QLabel("Save location:")
        self.saveLocationEdit = QLineEdit()
        self.saveLocationEdit.setPlaceholderText("Save folder...")
        self.saveLocationEdit.setReadOnly(True)

        self.saveLocationButton = QPushButton("Select folder...")

        self.saveLocationButton.clicked.connect(self.browseSaveFolder)

        # Circuit dimensions
        self.dimensionsLabel = QLabel("Circuit dimensions:")
        self.circuitGridLines = QSpinBox()
        self.circuitGridLines.setRange(48, 512)
        self.circuitGridColumns = QSpinBox()
        self.circuitGridColumns.setRange(48, 512)

        # Standard buttons ("OK" and "Cancel")
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                      QDialogButtonBox.StandardButton.Cancel)
        
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        
        parentLayout.addWidget(self.nameLabel, 0, 0)
        parentLayout.addWidget(self.nameEdit, 0, 1)

        parentLayout.addWidget(self.imageLabel, 1,0)
        parentLayout.addWidget(self.imageEdit, 1,1)
        parentLayout.addWidget(self.imageAssetsButton, 1,2)

        parentLayout.addWidget(self.saveLocationLabel, 2, 0)
        parentLayout.addWidget(self.saveLocationEdit, 2, 1)
        parentLayout.addWidget(self.saveLocationButton)

        parentLayout.addWidget(self.dimensionsLabel, 3,0)
        parentLayout.addWidget(self.circuitGridLines, 3,1)
        parentLayout.addWidget(self.circuitGridColumns, 3,2)

        parentLayout.addWidget(button_box, 4, 0, 1, 3)

        


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
            
            # Afficher une erreur si le dossier ne contient pas de fichiers image valides
            while not any(file.endswith(".jpg") or file.endswith(".png") for file in os.listdir(folder_path)):
                error_message = QMessageBox.critical(self, "Invalid images assets folder", "The selected folder does not contain valid PNG or JPEG files.", QMessageBox.StandardButton.Retry)
                folder_path = self.browseFolder("Select a folder containing image assets")



            self.imageEdit.setText(folder_path)


        return folder_path


    def browseSaveFolder(self) -> str:
        """Allows the user to browse the folder inside of which the circuit will be saved."""

        save_location = self.browseFolder("Select save location folder:")

        if save_location !="":
            self.saveLocationEdit.setText(save_location)

        return save_location
    

    def validInput(self) -> bool:
        """Checks the validity of all inputs in the dialog box and return True if everything is valid, or False otherwise."""

        inputData = self.getData()

        for value in inputData.values():
            if isinstance(value, str):
                if value.strip() == "":
                    return False

        return True        


    def getData(self) -> dict:
        """Returns a dictionnary containing the values of each input in the popup."""

        input_values = {
            "circuit_name":self.nameEdit.text(),
            "image_assets_folder":self.imageEdit.text(),
            "save_location":self.saveLocationEdit.text(),
            "dimensions_lines":self.circuitGridLines.value(),
            "dimensions_columns":self.circuitGridColumns.value()
        }


        return input_values





        