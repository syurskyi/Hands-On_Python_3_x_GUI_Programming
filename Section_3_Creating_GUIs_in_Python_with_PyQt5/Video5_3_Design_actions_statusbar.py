import sys
from PyQt5 import QtWidgets
from Section_3_Creating_GUIs_in_Python_with_PyQt5.Designer_code.Video5_First_Design import Ui_MainWindow


class RunDesignerGUI():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        
        self.ui = Ui_MainWindow()                           
        self.ui.setupUi(self.MainWindow)
        
        self.update_widgets()
        self.widget_actions()
        
        self.MainWindow.show()
        sys.exit(app.exec_())
    
    def widget_actions(self):
        self.ui.actionExit.setStatusTip('Click to exit the application')    # use ui reference to update status bar
     
    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')         # use: self.MainWindow
        self.ui.pushButton.setText('New Button text')       # use: self.ui to access widgets

 
if __name__ == "__main__":
    RunDesignerGUI()   


















