from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("\n"
"background-color: rgb(50, 55, 61)")
        self.upload = QtWidgets.QPushButton(Form)
        self.upload.setGeometry(QtCore.QRect(150, 400, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.upload.setFont(font)
        self.upload.setAutoFillBackground(False)
        self.upload.setStyleSheet("color: rgb(221, 255, 255);\n"
"background-color: rgb(34, 37, 42);")
        self.upload.setFlat(False)
        self.upload.setObjectName("upload")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(150, 470, 201, 21))
        self.progressBar.setStyleSheet("color: rgb(221, 255, 255);\n"
"background-color: rgb(34, 37, 42);\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.choosefile = QtWidgets.QToolButton(Form)
        self.choosefile.setGeometry(QtCore.QRect(10, 290, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.choosefile.setFont(font)
        self.choosefile.setStyleSheet("color: rgb(221, 255, 255);\n"
"background-color: rgb(34, 37, 42);")
        self.choosefile.setCheckable(False)
        self.choosefile.setObjectName("choosefile")
        self.protocol = QtWidgets.QComboBox(Form)
        self.protocol.setGeometry(QtCore.QRect(100, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.protocol.setFont(font)
        self.protocol.setStyleSheet("color: rgb(221, 255, 255);\n"
"background-color: rgb(34, 37, 42);")
        self.protocol.setObjectName("protocol")
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(221, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 243, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(221, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_login = QtWidgets.QLineEdit(Form)
        self.lineEdit_login.setGeometry(QtCore.QRect(180, 30, 211, 21))
        self.lineEdit_login.setStyleSheet("background-color: rgb(255, 255, 255)\n"
"")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(221, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(180, 70, 211, 21))
        self.lineEdit_password.setAutoFillBackground(False)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 202, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(221, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(221, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_adress = QtWidgets.QLineEdit(Form)
        self.lineEdit_adress.setGeometry(QtCore.QRect(80, 161, 171, 21))
        self.lineEdit_adress.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_adress.setObjectName("lineEdit_adress")
        self.lineEdit_port = QtWidgets.QLineEdit(Form)
        self.lineEdit_port.setGeometry(QtCore.QRect(80, 202, 171, 21))
        self.lineEdit_port.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 110, 501, 6))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.resulttext = QtWidgets.QLabel(Form)
        self.resulttext.setGeometry(QtCore.QRect(434, 476, 71, 21))
        self.resulttext.setStyleSheet("color: rgb(7, 255, 106);")
        self.resulttext.setText("")
        self.resulttext.setObjectName("resulttext")
        self.filenametext = QtWidgets.QLabel(Form)
        self.filenametext.setGeometry(QtCore.QRect(45, 340, 171, 20))
        self.filenametext.setStyleSheet("color: rgb(7, 255, 106);")
        self.filenametext.setText("")
        self.filenametext.setAlignment(QtCore.Qt.AlignCenter)
        self.filenametext.setObjectName("filenametext")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 380, 501, 6))
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label.setBuddy(self.lineEdit_login)
        self.label_3.setBuddy(self.protocol)
        self.label_2.setBuddy(self.lineEdit_password)
        self.label_4.setBuddy(self.lineEdit_port)
        self.label_5.setBuddy(self.lineEdit_adress)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Helper v0.1"))
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        self.upload.setText(_translate("Form", "Загрузить"))
        self.progressBar.setFormat(_translate("Form", "%p%"))
        self.choosefile.setText(_translate("Form", "Выбрать файл"))
        self.protocol.setItemText(0, _translate("Form", "HTTP"))
        self.protocol.setItemText(1, _translate("Form", "HTTPS"))
        self.label.setText(_translate("Form", "Логин:"))
        self.label_3.setText(_translate("Form", "Протокол:"))
        self.label_2.setText(_translate("Form", "Пароль:"))
        self.label_4.setText(_translate("Form", "Порт:"))
        self.label_5.setText(_translate("Form", "Адрес:"))
