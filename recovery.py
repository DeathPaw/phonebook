#from PyQt5.Qt import *
from PyQt5.QtCore import QRect, Qt, QCoreApplication, QMetaObject, pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class Ui_signUp(object):
    def setupUi(self, Recover):
        Recover.setObjectName("Recover")
        Recover.resize(800, 800)

        self.label_2 = QLabel(Recover)
        self.label_2.setGeometry(QRect(150, 120, 90, 31))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(Recover)
        self.label_3.setGeometry(QRect(150, 80, 90, 31))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.email_lineEdit = QLineEdit(Recover)
        self.email_lineEdit.setGeometry(QRect(250, 80, 200, 20))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_lineEdit = QLineEdit(Recover)
        self.password_lineEdit.setGeometry(QRect(250, 120, 200, 20))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.reset_pass_btn = QPushButton(Recover)
        self.reset_pass_btn.setGeometry(QRect(150, 160, 300, 23))
        self.reset_pass_btn.setObjectName("reset_pass_btn")
        self.label_4 = QLabel(Recover)
        self.label_4.setGeometry(QRect(150, 10, 321, 81))
        font = QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.retranslateUi(Recover)
        QMetaObject.connectSlotsByName(Recover)

    def retranslateUi(self, Recover):
        _translate = QCoreApplication.translate
        Recover.setWindowTitle(_translate("Recover", "Recover"))
        self.label_2.setText(_translate("Recover", "PASSWORD"))
        self.label_3.setText(_translate("Recover", "Email"))
        self.reset_pass_btn.setText(_translate("Recover", "Update password"))
        self.label_4.setText(_translate("Recover", "Set new passsword"))


class Recover(QDialog, Ui_signUp):
    def __init__(self, parent=None):
        super(Recover, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.reset_pass_btn.clicked.connect(self.insertData)

    @pyqtSlot()
    def insertData(self):
        email    = self.email_lineEdit.text()
        password = self.password_lineEdit.text()

        if (not password) or (not email):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return

        result = self.parent.loginDatabase.conn.execute("SELECT * FROM MYUSERS WHERE EMAIL = ?", (email,))
        if not result.fetchall():
            msg = QMessageBox.information(self, 'Внимание!', 'Пользоватеть с такой почтой не зарегистрирован.')
        else:
            self.parent.loginDatabase.conn.execute("UPDATE MYUSERS SET PASSWORD = ? WHERE EMAIL = ?",
                                                   (password, email,))
            self.parent.loginDatabase.conn.commit()
            self.close()


if __name__ == "__main__":
    import sys
    app    = QApplication(sys.argv)
    w = Recover()
    w.show()
    sys.exit(app.exec_())