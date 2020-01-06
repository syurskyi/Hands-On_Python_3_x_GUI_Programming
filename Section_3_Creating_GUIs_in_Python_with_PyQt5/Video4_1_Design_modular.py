from PyQt5 import QtWidgets
from Section_3_Creating_GUIs_in_Python_with_PyQt5.Designer_code.Video3_First_Design import Ui_MainWindow



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    


















