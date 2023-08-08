from PyQt5 import QtCore, QtGui, QtWidgets
import random

def generate_psw(len, self, upper, only_number, spec_sym, add_num, save_value):
    if len == 0:
        return
    old_value = self.txt_genpwd.toPlainText()

    leaner = 'abcdefghijklmnopqrstuvwxyz'
    a_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    a_spec_sym = '!@#$%&?><(){}[]_+=/*'

    lib_array = leaner
    if upper:
        lib_array = lib_array + a_upper
    if spec_sym:
        lib_array = lib_array + a_spec_sym
    if add_num:
        lib_array = lib_array + number
    if only_number:
        lib_array = number

    psw = ['0'] * len

    psw = [random.choice(lib_array) for x in psw]
    n_pwd = ''.join([str(elem) for elem in psw])

    if save_value:
        self.txt_genpwd.setText(old_value + '\n' + n_pwd)
    else:
        self.txt_genpwd.setText(n_pwd)





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("PasswordGenerator")
        MainWindow.resize(390, 160)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)


        self.onlyNumber = QtWidgets.QCheckBox(self.centralwidget)
        self.onlyNumber.setGeometry(QtCore.QRect(200, 10, 200, 17))
        self.onlyNumber.setObjectName("onlyNumber")

        self.addNumber = QtWidgets.QCheckBox(self.centralwidget)
        self.addNumber.setGeometry(QtCore.QRect(200, 100, 200, 17))
        self.addNumber.setObjectName("addNumber")

        self.add_head_symbol = QtWidgets.QCheckBox(self.centralwidget)
        self.add_head_symbol.setGeometry(QtCore.QRect(200, 40, 200, 17))
        self.add_head_symbol.setObjectName("add_head_symbol")
        self.spec_symbols = QtWidgets.QCheckBox(self.centralwidget)
        self.spec_symbols.setGeometry(QtCore.QRect(200, 70, 200, 17))
        self.spec_symbols.setObjectName("spec_symbols")

        self.save_value = QtWidgets.QCheckBox(self.centralwidget)
        self.save_value.setGeometry(QtCore.QRect(200, 130, 200, 17))
        self.save_value.setObjectName("save_value")

        self.len_pwd = QtWidgets.QSpinBox(self.centralwidget)
        self.len_pwd.setGeometry(QtCore.QRect(10, 10, 50, 41))

        self.len_pwd.setObjectName("len_pwd")
        self.txt_genpwd = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_genpwd.setGeometry(QtCore.QRect(10, 60, 180, 81))
        self.txt_genpwd.setObjectName("txt_genpwd")

        self.btn_generate.setGeometry(QtCore.QRect(70, 10, 121, 41))
        self.btn_generate.setObjectName("btn_generate")
        self.btn_generate.clicked.connect(lambda: generate_psw(self.len_pwd.value(), self, self.add_head_symbol.isChecked(), self.onlyNumber.isChecked(), self.spec_symbols.isChecked(), self.addNumber.isChecked(), self.save_value.isChecked()))

        self.len_pwd.setValue(8)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_generate.setText(_translate("MainWindow", "Сгенерировать"))
        self.onlyNumber.setText(_translate("MainWindow", "Только цифры"))
        self.add_head_symbol.setText(_translate("MainWindow", "Испольовать верхний регистр"))
        self.spec_symbols.setText(_translate("MainWindow", "Использовать спецсимволы"))
        self.addNumber.setText(_translate("MainWindow", "Использовать цифры"))
        self.save_value.setText(_translate("MainWindow", "Сохранять пароли"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
