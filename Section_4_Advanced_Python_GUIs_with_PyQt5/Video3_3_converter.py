import sys
from PyQt5 import QtWidgets, QtGui
from Section_4_Advanced_Python_GUIs_with_PyQt5.Designer_code.Video3_7_converter_radio_text_Design import Ui_MainWindow


class RunDesignerGUI():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
      
        self.ui = Ui_MainWindow()                           
        self.ui.setupUi(self.MainWindow)
        
        self.update_widgets()
        self.widget_actions()
        self.tab2_actions()
        
        self.MainWindow.show()
        sys.exit(app.exec_())
    
    def tab2_actions(self):
        self.ui.radioButton_ui.clicked.connect(self.convert_ui_to_py)
        self.ui.radioButton_exe.clicked.connect(self.convert_py_to_exe)
           
    def convert_ui_to_py(self):    
        self.ui.label_convert.setText(' Browse to UI File:')
        
    def convert_py_to_exe(self):
        self.ui.label_convert.setText(' Browse to PY File:')
        
             
    
    def widget_actions(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)    # correct relative path to icon
        self.ui.actionNew.setIcon(icon)
        self.ui.actionNew.setShortcut('Ctrl+N')
        
        self.ui.actionExit.setStatusTip('Click to exit the application')        # use ui reference to update status bar
        self.ui.actionExit.triggered.connect(self.close_GUI)                    # connect widget to method when triggered (clicked)
        self.ui.actionExit.setShortcut('Ctrl+Q')                                # keyboard shortcut, window has focus 
                
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)   # modify icon location
        self.ui.actionExit.setIcon(icon1)                                                            # use: self.ui.  
        
        #-------------------------------
        self.ui.pushButton_clear.clicked.connect(self.ui.label.clear)           # removed slot and placed code here
        self.ui.pushButton_set_label.clicked.connect(self.set_label)            # add functionality to second button
    
    def set_label(self):
        window_text = self.MainWindow.windowTitle()
        self.ui.label.setText(window_text)                          # set label text to window title        
            
    def close_GUI(self): 
        self.MainWindow.close()         # call MainWindow close method, which closes the GUI
    
    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')           # use: self.MainWindow

 
if __name__ == "__main__":
    RunDesignerGUI()   


















