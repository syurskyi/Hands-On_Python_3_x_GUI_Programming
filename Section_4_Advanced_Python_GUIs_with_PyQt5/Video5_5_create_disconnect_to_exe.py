import sys, os
from PyQt5 import QtWidgets, QtGui
from Section_4_Advanced_Python_GUIs_with_PyQt5.Designer_code.Video4_Design import Ui_MainWindow


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
        def init_toolbutton(): pass
        self.ui.toolButton.clicked.connect(init_toolbutton)             # avoid first exception when disconnect
        self.ui.pushButton_convert.clicked.connect(init_toolbutton)     # avoid first exception when disconnect
        
        self.ui.radioButton_ui.clicked.connect(self.label_ui_to_py)
        self.ui.radioButton_exe.clicked.connect(self.label_py_to_exe)
        
        self.ui.radioButton_ui.click()                                      # programmatically click radio button
        
    #-------------------------------------------------------       
    def label_ui_to_py(self):    
        self.ui.label_convert.setText(' Browse to UI File:')
        self.ui.lineEdit.setText('')
        self.disconnect_buttons()
        self.ui.toolButton.clicked.connect(self.convert_ui_to_py)
        self.ui.pushButton_convert.clicked.connect(self.create_py_file)
      
    def convert_ui_to_py(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', "", 'Designer UI files (*.ui)')
        self.ui.lineEdit.setText(file_name)
        
    def create_py_file(self):
        ui_file = self.ui.lineEdit.text()
        if ui_file:
            file_path, file_ext = os.path.splitext(ui_file)
            if file_ext == '.ui':
                py_file = file_path + '.py'
                cmd = 'pyuic5 -x -o {} {}'.format(py_file, ui_file)
                os.system(cmd)
                print('File created: ', cmd)
    
    #-------------------------------------------------------            
    def label_py_to_exe(self):
        self.ui.label_convert.setText(' Browse to PY File:')
        self.ui.lineEdit.setText('')
        self.disconnect_buttons()
        self.ui.toolButton.clicked.connect(self.convert_py_to_exe)
        self.ui.pushButton_convert.clicked.connect(self.create_exe_file)
        
    def convert_py_to_exe(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', "", 'Python files (*.py)')
        self.ui.lineEdit.setText(file_name)    

    def create_exe_file(self):
        py_file = self.ui.lineEdit.text()
        if py_file:
            _file_path, file_ext = os.path.splitext(py_file)
            if file_ext == '.py':
                cmd = 'pyinstaller --onefile --noconsole {}'.format(py_file)
                os.system(cmd)
                print('EXE File created: ', cmd)
                    
    #-------------------------------------------------------         
    def disconnect_buttons(self):
        # Disconnect previously connected buttons - ignore exception if not connected
        try:
            self.ui.toolButton.clicked.disconnect()
            self.ui.pushButton_convert.clicked.disconnect()
        except Exception as ex:
            print(ex)                       # disconnect() failed between 'clicked' and all its connections
        
        
            
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


















