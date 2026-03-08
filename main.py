"""This program defines the home window of the application and runs it."""
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QMessageBox, QListWidget, QListWidgetItem, QWidget
from PyQt6.QtGui import QAction, QFont
from PyQt6.QtCore import Qt
from special_popups.create_circuit import *
import user_data.circuit_files
import user_data.circuit
import circuit_editor
import recent_activity

class HomeWindow(QMainWindow):
    """An instance of the application home window. It allows the user to create or open circuits."""
    def __init__(self):
        super().__init__() # Initialize the parent QMainWindow object

        # Minimum dimensions : 600*400
        self.setMinimumSize(600, 400)

        self.setWindowTitle("2D circuit editor - Home")


        parentLayout = QVBoxLayout() # Set a vertical layout for widgets

        self.editor = None # Current editor window

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
        open_circuit_action.triggered.connect(self.ask_open_circuit)
        file_menu.addAction(open_circuit_action)

        # Quit the application
        quit_action = QAction("Quit...", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        parentLayout = QVBoxLayout()
        central_widget.setLayout(parentLayout)


        self.recentActivity = recent_activity.open_recent_activity() # Get the recent activity saved in the 'recent_activity.json' file
        print(f"Recent activity: {self.recentActivity}")

        self.recentLabel = QLabel("No recent activity", alignment=Qt.AlignmentFlag.AlignCenter)
        self.recentList = QListWidget()
        self.openRecentButton = QPushButton("Open recent")
        self.openRecentButton.clicked.connect(self.open_recent)
    
        # If there is no recent activity
        if self.recentActivity == {}:
            # Widget displaying recently opened circuits

            self.recentList.hide()
            self.openRecentButton.hide()

            parentLayout.addWidget(self.recentLabel)

        else:
            self.recentLabel.hide()

            
            

            # Display a list of recent circuits
            for circuit_name, file_path in self.recentActivity.items():
                print(circuit_name, file_path)
                circuit_item = QListWidgetItem(f"{circuit_name + "|" + file_path}")
                # Display the recent circuits in bold
                circuit_item_font = QFont()
                circuit_item_font.setBold(True)
                circuit_item.setFont(circuit_item_font)

                self.recentList.addItem(circuit_item)

            parentLayout.addWidget(self.openRecentButton)
            parentLayout.addWidget(self.recentList)
            
                



    def open_recent(self) -> None:
        """Open a recent selected circuit into the editor."""


        # Get the item selected in the list
        selected_items = self.recentList.selectedItems()

        if selected_items == []:
            # Do nothing if no item is selected
            pass
        
        else:
            # Open the selected circuit in the editor otherwise
            selected_circuit_item = selected_items[0]
            circuit_name, file_path = selected_circuit_item.text().split("|")[0], selected_circuit_item.text().split("|")[1]

            self.open_circuit_editor(file_path)


    def open_circuit_editor(self, file:str="") -> None:
        """Open a circuit editor window and hides the home window."""

        self.hide() # Hide the home window

        self.editor = circuit_editor.CircuitEditorWindow(file)
        self.editor.show()

        self.editor.destroyed.connect(self.show) # Show the home window once the editor is closed


    def ask_open_circuit(self) -> None:
        """Display a user dialog to select a JSON circuit file and open it in a circuit editor window."""

        # File dialog to pick a JSON circuit file
        dialog = QFileDialog(self, "Open a circuit", "", "JSON circuit files (*.json)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile) # Ensure the user cannot open inexistant files

        result = dialog.exec()

        # If the user selected a JSON file, open it in the circuit editor
        if result: 
            selected_file = dialog.selectedFiles()[0]
            print(selected_file)
            self.open_circuit_editor(selected_file)



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
                new_circuit = user_data.circuit.Circuit(creation_data["circuit_name"], 
                                                        creation_data["save_location"],
                                                        creation_data["image_assets_folder"],
                                                        creation_data["dimensions_lines"],
                                                        creation_data["dimensions_columns"])
                
                # Save the circuit to a file
                user_data.circuit_files.save_circuit(new_circuit)

                # Create a new editor window
                file_name = user_data.sanitize_filenames.sanitize_filename(creation_data["circuit_name"] + ".json") # Sanitize the file name based on the circuit name
                save_location = creation_data["save_location"] # Save directory

                self.recentActivity[creation_data["circuit_name"]] = f"{Path(save_location) / file_name}"
                print(f"Recent activity: {self.recentActivity}")

                recent_activity.save_recent_activity(self.recentActivity)

                self.open_circuit_editor(f"{Path(save_location) / file_name}")


# Launch the app
app = QApplication([])
#app.setQuitOnLastWindowClosed(False)
home_window = HomeWindow()

home_window.show()
app.exec()