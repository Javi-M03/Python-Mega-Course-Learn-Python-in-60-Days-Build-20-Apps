from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        #Create Widgets
        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()
        self.distance_combo_box = QComboBox()
        self.distance_combo_box.addItems(['Metric[Km]','Imperial[Miles]'])

        time_label = QLabel("Time [Hours]")
        self.time_line_edit = QLineEdit()


        calculate_button = QPushButton("Calculate Average Speed")
        calculate_button.clicked.connect(self.calculate_avg_speed)
        self.output_label = QLabel("")


        #Add Widgets
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.distance_combo_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)
    
    def calculate_avg_speed(self):
         if self.distance_combo_box.currentText() == 'Metric[Km]':
             avg_speed = int(self.distance_line_edit.text()) / int(self.time_line_edit.text())
             self.output_label.setText(f"{str(avg_speed)} km/h")
         avg_speed = int(self.distance_line_edit.text()) / int(self.time_line_edit.text())
         self.output_label.setText(f"{str(round(avg_speed * 0.621371,2))} mph")
        


app = QApplication(sys.argv)
avg_speed_calculator = SpeedCalculator()
avg_speed_calculator.show()
sys.exit(app.exec())
