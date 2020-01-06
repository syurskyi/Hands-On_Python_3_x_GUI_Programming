import sys
from PyQt5 import QtWidgets
from Section_3_Creating_GUIs_in_Python_with_PyQt5.Designer_code.Video3_First_Design import Ui_MainWindow


class RunDesignerGUI():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        
        self.ui = Ui_MainWindow()                           
        self.ui.setupUi(self.MainWindow)
        
        self.MainWindow.setWindowTitle('PyQt5 GUI')         # change window title        
        
        self.MainWindow.show()
        sys.exit(app.exec_())
    
 
if __name__ == "__main__":
    RunDesignerGUI()   


















