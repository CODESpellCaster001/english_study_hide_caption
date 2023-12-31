
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QSlider, QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class TransparentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Transparent Dialog')
        
        self.layout = QVBoxLayout()
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(20)  # Minimum opacity set to 20%
        self.slider.setMaximum(100)
        self.slider.setValue(100)
        self.slider.valueChanged.connect(self.set_opacity)
        
        self.button = QPushButton('Toggle Opacity')
        self.button.clicked.connect(self.toggle_opacity)
        
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # Always on top
        
    def set_opacity(self, value):
        opacity = value / 100
        self.setWindowOpacity(opacity)
        
        # Set background color to black with the adjusted opacity
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(0, 0, 0, int(255 * opacity)))
        self.setPalette(palette)
    
    def toggle_opacity(self):
        current_value = self.slider.value()
        if current_value >= 50:
            self.slider.setValue(20)  # Set to minimum
        else:
            self.slider.setValue(100)  # Set to maximum

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = TransparentDialog()
    dialog.show()
    sys.exit(app.exec_())

    