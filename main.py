"""This program defines the home window of the application and runs it."""
from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from special_popups.create_circuit import *

class HomeWindow(QMainWindow):
    """An instance of the application home window. It allows the user to create or open circuits."""
    def __init__(self):
        super().__init__() # Initialize the parent QMainWindow object

        # Minimum dimensions : 600*400
        self.setMinimumSize(600, 400)

        self.setWindowTitle("2D circuit editor - Home")

        parentLayout = QVBoxLayout() # Set a vertical layout for widgets

        # Define the menu bar
        menu_bar = self.menuBar()


        # "File" menu
        file_menu = menu_bar.addMenu("File")

        # == "File" menu actions ==
        
        # Create a circuit
        create_circuit_action = QAction("New circuit...", self)
        create_circuit_action.setShortcut("Ctrl+N")
        create_circuit_action.triggered.connect(self.create_circuit) # Show a popup to create a new circuit when the "create circuit" action is triggered
        file_menu.addAction(create_circuit_action) # Add the action to the "File" menu


        # Open a circuit
        open_circuit_action = QAction("Open circuit...", self)
        open_circuit_action.setShortcut("Ctrl+O")
        file_menu.addAction(open_circuit_action)

        # Quit the application
        quit_action = QAction("Quit...", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)


        # Widget displaying recent opened circuits
        recentLabel = QLabel("No recent activity", alignment=Qt.AlignmentFlag.AlignCenter)
        parentLayout.addWidget(recentLabel)

        self.setLayout(parentLayout)
        self.setCentralWidget(recentLabel)


    def create_circuit(self):
        """Displays a popup meant to set up a new circuit"""
        
        # Display a popup to set up the new circuit
        create_popup = CreateCircuitPopup()
        result = create_popup.exec()

        if result:

            # Check input validity
            valid_input = create_popup.validInput()

            # If there are invalid inputs, show an error message
            if not valid_input:
                QMessageBox.critical(self, "Invalid inputs", "Invalid inputs were detected in the circuit creation popup.", QMessageBox.StandardButton.Ok)

            else: 
                # Create the circuit otherwise 
                creation_data = create_popup.getData()
                print(creation_data)


# Launch the app
app = QApplication([])
home_window = HomeWindow()

home_window.show()
app.exec()