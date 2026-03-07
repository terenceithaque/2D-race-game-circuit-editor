"""This script handles the circuit editor window of the app"""
from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel, QVBoxLayout, QMessageBox, QFileDialog
from PyQt6.QtGui import QAction
from pathlib import Path
import os
from PyQt6.QtCore import Qt
import user_data.circuit
import user_data.circuit_files
import special_popups.create_circuit


class CircuitEditorWindow(QMainWindow):
    """An instance of a circuit editor window."""
    def __init__(self, file:str=""):
        """Initializes the circuit editor window."""
        
        super().__init__()
        
        self.setMinimumSize(600, 400)

        self.setWindowTitle("Main Editor | 2D-race-game-circuit-editor")

        self.file = file # Current circuit file path

        # Menu bar of the editor window
        menu_bar = self.menuBar()

        # == File menu ==
        file_menu = menu_bar.addMenu("File")

        # == File menu actions ==

        # Create a circuit
        create_circuit_action = QAction("New circuit...", self)
        create_circuit_action.setShortcut("Ctrl+N")
        file_menu.addAction(create_circuit_action)


        # Open a circuit
        open_circuit_action = QAction("Open circuit...", self)
        open_circuit_action.setShortcut("Ctrl+O")
        open_circuit_action.triggered.connect(self.ask_open_circuit)
        file_menu.addAction(open_circuit_action)

        # Save circuit
        save_circuit_action = QAction("Save", self)
        save_circuit_action.setShortcut("Ctrl+S")
        file_menu.addAction(save_circuit_action)

        # Save as action
        save_as_action = QAction("Save as...", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        file_menu.addAction(save_as_action)

        

        print(f"Opened file: {self.file}")


        # If a file path was not specified or does not exists, ask the user to create a circuit
        if not self.file.strip() or not Path(self.file).exists():
            creation_popup = special_popups.create_circuit.CreateCircuitPopup()
            result = creation_popup.exec()
            if result:

                # Check input validity
                valid_input = creation_popup.validInput()

                # If there are invalid inputs, show an error message
                if not valid_input:
                    QMessageBox.critical(self, "Invalid inputs", "Invalid inputs were detected in the circuit creation popup.", QMessageBox.StandardButton.Ok)

                else: 
                    # Create the circuit otherwise 
                    creation_data = creation_popup.getData()
                    print(creation_data)
                    self.circuit = user_data.circuit.Circuit(creation_data["circuit_name"], 
                                                            creation_data["save_location"],
                                                            creation_data["image_assets_folder"],
                                                            creation_data["dimensions_lines"],
                                                            creation_data["dimensions_columns"])
                    
                    # Save the circuit to a file
                    self.setWindowTitle(f"{self.circuit.name} | 2D-race-game-circuit-editor") # Change the editor window title


        # Otherwise, create the Circuit object based on the file's internal data
        else:
            self.create_circuit_from_file() 


    def ask_open_circuit(self) -> None:
        """Displays a dialog allowing the user to open a circuit file and opens that file."""

        dialog = QFileDialog(self, "Open a circuit", "", "JSON circuit files (*json)") # File dialog
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile) # The user can open only existing files
        
        file_selected = dialog.exec()

        if file_selected:
            file_path = dialog.selectedFiles()[0]

            return user_data.circuit_files.open_circuit(file_path)
        

    def create_circuit_from_file(self) -> None:
        """Creates the Circuit object based on the editor's current circuit file and defines it as the current circuit in the editor."""
        circuit_data = user_data.circuit_files.open_circuit(self.file)
        print(f"Données du circuit chargé: {circuit_data}")
        self.circuit = user_data.circuit.Circuit(name=circuit_data["data"]["metadata"]["name"],
                                                    saveFolder=circuit_data["data"]["metadata"]["save_location"],
                                                    imageAssetsFolder=circuit_data["data"]["metadata"]["image_assets_folder"],
                                                    nbLines=circuit_data["data"]["metadata"]["nb_lines"],
                                                    nbColumns=circuit_data["data"]["metadata"]["nb_columns"])

        self.setWindowTitle(f"{self.circuit.name} | 2D-race-game-circuit-editor")   
        
        

