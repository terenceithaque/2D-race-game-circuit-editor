"""This script handles the circuit editor window of the app"""
from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt


class CircuitEditorWindow(QMainWindow):
    """An instance of a circuit editor window."""
    def __init__(self):
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
        file_menu.addAction(open_circuit_action)

        # Save circuit
        save_circuit_action = QAction("Save", self)
        save_circuit_action.setShortcut("Ctrl+S")
        file_menu.addAction(save_circuit_action)

        # Save as action
        save_as_action = QAction("Save as...", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        file_menu.addAction(save_as_action)

        

