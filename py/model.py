import sys
from PySide6.QtWidgets import (
    QApplication,QMainWindow,
    QWidget,QLabel, 
    QPushButton, QVBoxLayout, QMessageBox
)
from PySide6.QtGui import QPixmap
#======================f=========================================
#SECOND WINDOW
class AnotherWindow(QWidget):
    "image"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Imagem")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        self.image_label = QLabel(self)  
        pixmap = QPixmap("py/assets/image.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.setStyleSheet("background-color: black;")
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def closeEvent(self, event):
        """colored text"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("close window")
        msg_box.setText("close window?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        # text color style
        msg_box.setStyleSheet("""
            QMessageBox { background-color: #2b2b2b; }  /* Fundo da caixa de diálogo */
            QLabel { color: yellow; font-size: 14px; }  /* Cor e tamanho do texto */
            QPushButton { background-color: #444; color: white; padding: 5px; }
            QPushButton:hover { background-color: #666; }
        """)

        reply = msg_box.exec()
        if reply == QMessageBox.Yes:
            event.accept()  #close window
        else:
            event.ignore()  #cancel
#=================================================================
#Original WIndow 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window1")

        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self,cheked):
        self.x = AnotherWindow()
        self.x.show()


if __name__ in "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.setFixedSize(500,400)
    main.show()
    app.exec()