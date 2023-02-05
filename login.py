#from PyQt5.Qt import *
from PyQt5.QtCore import QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QDialog, QMessageBox, QApplication, QCheckBox

import welcome
import recovery
from signup  import Dialog
import sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)
        self.u_name_label = QLabel(Dialog)
        self.u_name_label.setGeometry(QRect(150, 110, 71, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QLabel(Dialog)
        self.pass_label.setGeometry(QRect(150, 150, 71, 21))
        font = QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.uname_lineEdit = QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QRect(230, 110, 113, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.pass_lineEdit = QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QRect(230, 150, 113, 20))
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.login_btn = QPushButton(Dialog)
        self.login_btn.setGeometry(QRect(230, 200, 51, 23))
        self.login_btn.setObjectName("login_btn")
        self.signup_btn = QPushButton(Dialog)
        self.signup_btn.setGeometry(QRect(290, 200, 51, 23))
        self.signup_btn.setObjectName("signup_btn")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(190, 10, 211, 51))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")



        self.checkbox=QCheckBox(Dialog)
        self.checkbox.setGeometry(QRect(150,250,200,50))
        #self.checkbox.setAlignment(Qt.AlignCenter)
        self.checkbox.setObjectName("check_remember_me")

        self.forgot_btn = QPushButton(Dialog)
        self.forgot_btn.setGeometry(QRect(150,300,200,50))
        self.forgot_btn.setObjectName("forgot_password_btn")

        self.signup_btn = QPushButton(Dialog)
        self.signup_btn.setGeometry(QRect(290, 200, 51, 23))
        self.signup_btn.setObjectName("signup_btn")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Form"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME "))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.label.setText(_translate("Dialog", "Login Form"))
        self.forgot_btn.setText(_translate("Dialog", "FORGOT"))
        self.checkbox.setText(_translate("Dialog", "REMEMBER ME"))



class LoginDatabase():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def is_table(self, table_name):
        query = "SELECT name from sqlite_master WHERE type='table' AND name='{}';".format(table_name)
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        #c.execute("SELECT Question FROM Flashcards")
        #resultq = c.fetchall()
        self.loginDatabase = LoginDatabase('phone.db')

        #self.loginDatabase.conn.execute("SELECT * FROM USERCONTACTS")

        if self.loginDatabase.is_table('MYUSERS'):
            pass

        else:
            self.loginDatabase.conn.execute("CREATE TABLE MYUSERS(USERNAME TEXT NOT NULL, EMAIL TEXT, BIRTHSDAY TEXT, PASSWORD TEXT)")
            self.loginDatabase.conn.execute("INSERT INTO MYUSERS VALUES(?, ?, ?,?)",
                                           ('admin', 'admin@gmail.com', '31','admin')
            )
            self.loginDatabase.conn.commit()

        self.login_btn.clicked.connect(self.loginCheck)
        self.signup_btn.clicked.connect(self.signUpCheck)
        self.forgot_btn.clicked.connect(self.recoveryWindowShow)

    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def welcomeWindowShow(self, username):
        self.welcomeWindow = welcome.MainWindow(username)
        self.welcomeWindow.show()

    def recoveryWindowShow(self):
        self.recoveryWindow = recovery.Recover(self)
        self.recoveryWindow.show()


    def signUpShow(self):
        self.signUpWindow = Dialog(self)
        self.signUpWindow.show()

    def loginCheck(self):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()
        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return

        result = self.loginDatabase.conn.execute("SELECT * FROM MYUSERS WHERE USERNAME = ? AND PASSWORD = ?",
                                                 (username, password))
        if len(result.fetchall()):
            self.remember_me_check()
            self.welcomeWindowShow(username)
            self.hide()
            self.loginDatabase.conn.close()
        else:
            self.showMessageBox('Внимание!', 'Неправильное имя пользователя или пароль.')

    def signUpCheck(self):
        self.signUpShow()
    def check_auto_login(self):
        if self.loginDatabase.is_table('DEFAULTUSER'):
            username = self.loginDatabase.conn.execute(
                "SELECT USERNAME FROM DEFAULTUSER").fetchone()
            password = self.loginDatabase.conn.execute(
                "SELECT PASSWORD FROM DEFAULTUSER").fetchone()
           # self.u_name_label.setText(_translate("Dialog", "USERNAME "))
            print(username[0]+' '+password[0])
            if username[0] != "UNLOG":
                self.uname_lineEdit.setText(username[0])
                self.pass_lineEdit.setText(password[0])
                self.loginCheck()
        else:
            self.loginDatabase.conn.execute(
                "CREATE TABLE DEFAULTUSER(USERNAME TEXT NOT NULL, PASSWORD TEXT)"
                )
            self.loginDatabase.conn.execute("INSERT INTO DEFAULTUSER VALUES(?, ?)",
                                            ('UNLOG', 'UNLOG')
                                            )
             # res = self.loginDatabase.conn.execute("SELECT * FROM DEFAULTUSER").fetchall()
            # print(res)
            self.loginDatabase.conn.commit()


    def remember_me_check(self):
        if self.checkbox.checkState():
            username = self.uname_lineEdit.text()
            password = self.pass_lineEdit.text()
            if self.loginDatabase.is_table('DEFAULTUSER'):
                self.loginDatabase.conn.execute(
                    "UPDATE DEFAULTUSER SET USERNAME=?, PASSWORD=?",
                    (username, password))
                #res = self.loginDatabase.conn.execute("SELECT * FROM DEFAULTUSER").fetchall()
                #print(res)
                self.loginDatabase.conn.commit()
            else:
                self.loginDatabase.conn.execute(
                    "CREATE TABLE DEFAULTUSER(USERNAME TEXT NOT NULL, PASSWORD TEXT)")
                self.loginDatabase.conn.execute("INSERT INTO DEFAULTUSER VALUES(?, ?)",
                                                (username, password)
                                                )
                #res = self.loginDatabase.conn.execute("SELECT * FROM DEFAULTUSER").fetchall()
                #print(res)
                self.loginDatabase.conn.commit()



if __name__ == "__main__":
    import sys
    app    = QApplication(sys.argv)
    w = MainDialog()
    w.show()
    w.check_auto_login()
    sys.exit(app.exec_())