"""This script handles the circuit editor window of the app"""
from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel, QVBoxLayout, QMessageBox, QFileDialog
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import user_data.circuit_files


class CircuitEditorWindow(QMainWindow):
    """An instance of a circuit editor window."""
    def __init__(self, file:str=""):
        """Initializes the circuit editor window."""
        
        super().__init__()
        
        self.setMinimumSize(600, 400)

        self.setWindowTitle("Main Editor | 2D-race-game-circuit-editor")

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


    def ask_open_circuit(self) -> None:
        """Displays a dialog allowing the user to open a circuit file and opens that file."""

        dialog = QFileDialog(self, "Open a circuit", "", "JSON circuit files (*json)") # File dialog
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile) # The user can open only existing files
        
        file_selected = dialog.exec()

        if file_selected:
            file_path = dialog.selectedFiles()[0]

            return user_data.circuit_files.open_circuit(file_path)
        
        

