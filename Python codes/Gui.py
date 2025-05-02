import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont , QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokedex")
        self.setGeometry(700, 300, 600, 600)
        self.setWindowIcon(QIcon("C:/Users/ariro/Downloads/pokedex.png"))
    
        self.initUI()
    
    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        self.redBackground = QWidget(self)
        self.redBackground.setStyleSheet("background-color: #9c2f27")
        self.redBackground.setMinimumHeight(100) 
        sideLayout = QVBoxLayout(self.redBackground)
        sideLayout.setAlignment(Qt.AlignCenter)
        
        self.picture = QLabel(self)
        self.pixmap = QPixmap("C:/Users/ariro/Downloads/pokedex frfr this time.png")
        self.picture.setPixmap(self.pixmap.scaled(self.width(), self.height()//11, Qt.KeepAspectRatio, Qt.SmoothTransformation)) 
        sideLayout.addWidget(self.picture)  
        
        mainLayout = QVBoxLayout()
        
        self.whiteBackground = QLabel(self)
        self.whiteBackground.setStyleSheet("background-color: #f0f0f0")
        self.whiteBackground.setMinimumHeight(100) 
        
        mainLayout.addWidget(self.redBackground)
        mainLayout.addWidget(self.whiteBackground)
        mainLayout.addWidget(self.whiteBackground)
        mainLayout.addWidget(self.whiteBackground)
        
        widget = QWidget()
        widget.setLayout(mainLayout)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(widget)
        
    def resizeEvent(self, event):
        if not self.pixmap.isNull():
            scaled = self.pixmap.scaled(self.width(), self.height() // 11, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.picture.setPixmap(scaled)
                  
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()        