"""This script defines several special popups for specific operations like creating a circuit."""
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QGridLayout


class CreateCircuitPopup(QDialog):
    """A popup asking the user several informations about a circuit to be created (name, dimensions, assets folders, etc.)"""
    def __init__(self):
        super().__init__() # Initialize the QDialog object

        self.setWindowTitle("Create a new circuit")