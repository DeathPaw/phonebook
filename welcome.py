import sqlite3
import datetime
from PyQt5.QtCore import QRect, Qt, QCoreApplication, QMetaObject, pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import *
import login

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(220, 230, 431, 51))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        #self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(240, 120, 211, 51))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
      #  self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setGeometry(QRect(490, 730, 50, 40))
        font = QFont()
        font.setPointSize(18)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")

        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setGeometry(QRect(540, 730, 50, 40))
        font = QFont()
        font.setPointSize(18)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")

        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setGeometry(QRect(590, 730, 50, 40))
        font = QFont()
        font.setPointSize(18)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")

        self.button_4 = QPushButton(self.centralwidget)
        self.button_4.setGeometry(QRect(640, 730, 50, 40))
        font = QFont()
        font.setPointSize(18)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")

        self.button_5 = QPushButton(self.centralwidget)
        self.button_5.setGeometry(QRect(690, 730, 50, 40))
        font = QFont()
        font.setPointSize(18)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")

        self.button_6 = QPushButton(self.centralwidget)
        self.button_6.setGeometry(QRect(740, 730, 50, 40))
        font = QFont()
        font.setPointSize(18)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")

        self.button_unlog = QPushButton(self.centralwidget)
        self.button_unlog.setGeometry(QRect(690, 770, 100, 30))
        font = QFont()
        font.setPointSize(9)
        self.button_unlog.setFont(font)
        self.button_unlog.setObjectName("button_unlog")

        self.button_add = QPushButton(self.centralwidget)
        self.button_add.setGeometry(QRect(360, 710, 80, 30))
        font = QFont()
        font.setPointSize(9)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")

        self.button_update = QPushButton(self.centralwidget)
        self.button_update.setGeometry(QRect(360, 740, 80, 30))
        font = QFont()
        font.setPointSize(9)
        self.button_update.setFont(font)
        self.button_update.setObjectName("button_update")

        self.button_delete = QPushButton(self.centralwidget)
        self.button_delete.setGeometry(QRect(360, 770, 80, 30))
        font = QFont()
        font.setPointSize(9)
        self.button_delete.setFont(font)
        self.button_delete.setObjectName("button_delete")

        self.birthsday_lineEdit = QLineEdit(self.centralwidget)
        self.birthsday_lineEdit.setGeometry(QRect(40, 770, 150, 20))
        self.birthsday_lineEdit.setObjectName("birthsday_lineEdit")

        self.id_lineEdit = QLineEdit(self.centralwidget)

        self.id_lineEdit.setGeometry(QRect(200, 710, 150, 80))
        self.id_lineEdit.setObjectName("id_lineEdit")

        self.contact_lineEdit = QLineEdit(self.centralwidget)
        self.contact_lineEdit.setGeometry(QRect(40, 710, 150, 20))
        self.contact_lineEdit.setObjectName("contact")

        self.phone_lineEdit = QLineEdit(self.centralwidget)
        self.phone_lineEdit.setGeometry(QRect(40, 740, 150, 20))
        self.phone_lineEdit.setObjectName("phone")


        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QRect(580, 630, 200, 300))
        self.listWidget.setObjectName("listWidget")
        #item = QListWidgetItem()
        #self.listWidget.addItem(item)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        #QMetaObject.connectSlotsByName(self.listWidget)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        self.loginDatabase = LoginDatabase('phone.db')
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.contact_lineEdit.setText(_translate("MainWindow", "contact"))
        self.birthsday_lineEdit.setText(_translate("MainWindow", "date"))
        self.phone_lineEdit.setText(_translate("MainWindow", "phone"))
        self.id_lineEdit.setText(_translate("MainWindow", "1"))
        #self.label(_translate("MainWindow", "date"))
        self.button_1.setText(_translate("MainWindow", "a-e"))
        self.button_2.setText(_translate("MainWindow", "f-h"))
        self.button_3.setText(_translate("MainWindow", "i-k"))
        self.button_4.setText(_translate("MainWindow", "l-o"))
        self.button_5.setText(_translate("MainWindow", "p-s"))
        self.button_6.setText(_translate("MainWindow", "t-z"))
        self.button_unlog.setText(_translate("MainWindow", "unlog"))
        self.button_add.setText(_translate("MainWindow", "add"))
        self.button_delete.setText(_translate("MainWindow", "delete"))
        self.button_update.setText(_translate("MainWindow", "update"))
        if self.loginDatabase.is_table('CONTACTBOOK'):
            pass
            #print(self.loginDatabase.conn.execute("select * from CONTACTS").fetchall())
        else:
            self.loginDatabase.conn.execute("CREATE TABLE CONTACTBOOK(CONTACTID INTEGER PRIMARY KEY AUTOINCREMENT, CONTACT TEXT NOT NULL, PHONE TEXT, BIRTHSDAY date)")
            self.loginDatabase.conn.execute("INSERT INTO CONTACTBOOK (CONTACT, PHONE, BIRTHSDAY) VALUES ('FRIEND', '82727326116', '2019-05-21')")
            self.loginDatabase.conn.execute("INSERT INTO CONTACTBOOK (CONTACT, PHONE, BIRTHSDAY) VALUES ('FRIEND2', '82727326116', '2019-05-21')")
            self.loginDatabase.conn.commit()
        item = self.loginDatabase.conn.execute("SELECT * FROM CONTACTBOOK "#where (strftime('%d-%m', BIRTHSDAY) between strftime('%d-%m', date('now')) and strftime('%d-md', date('now', '+13 day'))")
                                              "WHERE strftime('%m-%d', BIRTHSDAY) between "
                                              "strftime('%m-%d', 'now', '+1 day')"
                                              "and strftime('%m-%d', 'now', '+8 day')").fetchall()
        #item = self.loginDatabase.conn.execute("select * from CONTACTBOOK").fetchall()
        self.listWidget.addItem('ПОМНИТЕ У ЭТИХ ЛЮДЕЙ СКОРО ДЕНЬ РОЖДЕНИЯ')
        for i in item:
            self.listWidget.addItem(str(i))

    def validContactAdd(self, name_to_add, phone_to_add, birthsday_to_add):
        try:
            datetime.date.fromisoformat(birthsday_to_add)
            res = self.loginDatabase.conn.execute("select * from contactbook where contact = ? "
                                                 "and phone = ? and birthsday = ?",
                                            (name_to_add, phone_to_add, birthsday_to_add)).fetchall()
            #print(res)
            if not res:
                self.loginDatabase.conn.execute("INSERT INTO CONTACTBOOK (CONTACT, PHONE, BIRTHSDAY) VALUES (?, ?, ?)",
                                                (name_to_add, phone_to_add, birthsday_to_add))
                self.loginDatabase.conn.commit()
            else:
                msg = QMessageBox.information(self, 'Внимание!', 'Такой пользователь уже существует.')
        except ValueError:
            msg = QMessageBox.information(self, 'Внимание!', 'Некорректная дата.')
            return
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    def validContactUpdate(self, name_to_update, phone_to_update, birthsday_to_update, id_to_update):
        try:
            datetime.date.fromisoformat(birthsday_to_update)
            res = self.loginDatabase.conn.execute("select * from contactbook where contact = ? "
                                                  "and phone = ? and birthsday = ?",
                                                  (name_to_update,phone_to_update, birthsday_to_update))\
                .fetchall()
            # print(res)
            if not res:
                self.loginDatabase.conn.execute(
                    "UPDATE CONTACTBOOK SET CONTACT=?, PHONE=?, BIRTHSDAY=? WHERE CONTACTID = ?",
                    (name_to_update, phone_to_update, birthsday_to_update, id_to_update))
                self.loginDatabase.conn.commit()
            else:
                msg = QMessageBox.information(self, 'Внимание!', 'Такой пользователь уже существует.')
        except ValueError:
            msg = QMessageBox.information(self, 'Внимание!', 'Некорректная дата.')
            return
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @pyqtSlot()
    def on_click1(self):
        print('PyQt5 button click')
        self.listWidget.clear()

        item = self.loginDatabase.conn.execute("select * from CONTACTBOOK where contact like 'D%' or contact like 'A%' "
                                               "or contact like 'B%' or contact like 'C%' or contact like 'E%'"
                                               ).fetchall()

        for i in item:
            self.listWidget.addItem(str(i))
        #res = self.loginDatabase.conn.execute("SELECT * FROM CONTACTBOOK "#where (strftime('%d-%m', BIRTHSDAY) between strftime('%d-%m', date('now')) and strftime('%d-md', date('now', '+13 day'))")
        #                                      "WHERE strftime('%m-%d', BIRTHSDAY) between "
        #                                      "strftime('%m-%d', 'now', '+1 day')"
        #                                      "and strftime('%m-%d', 'now', '+8 day')").fetchall()
        #print(res)


    @pyqtSlot()
    def on_click2(self):
        print('PyQt5 button click')
        self.listWidget.clear()

        item = self.loginDatabase.conn.execute("select * from CONTACTBOOK where contact like 'F%' or contact like 'G%' "
                                               "or contact like 'H%'"
                                               ).fetchall()
        for i in item:
            self.listWidget.addItem(str(i))

    @pyqtSlot()
    def on_click3(self):
        print('PyQt5 button click')
        self.listWidget.clear()

        item = self.loginDatabase.conn.execute("select * from CONTACTBOOK where contact like 'I%' or contact like 'J%' "
                                               "or contact like 'K%'"
                                               ).fetchall()
        for i in item:
            self.listWidget.addItem(str(i))

    @pyqtSlot()
    def on_click4(self):
        print('PyQt5 button click')
        self.listWidget.clear()

        item = self.loginDatabase.conn.execute("select * from CONTACTBOOK where contact like 'L%' or contact like 'M%' "
                                               "or contact like 'N%' or contact like 'O%'"
                                               ).fetchall()
        for i in item:
            self.listWidget.addItem(str(i))
    @pyqtSlot()
    def on_click5(self):
        print('PyQt5 button click')
        self.listWidget.clear()

        item = self.loginDatabase.conn.execute("select * from CONTACTBOOK where contact like 'P%' or contact like 'Q%' "
                                               "or contact like 'R%' or contact like 'S%'"
                                               ).fetchall()
        for i in item:
            self.listWidget.addItem(str(i))

    @pyqtSlot()
    def on_click6(self):
        print('PyQt5 button click')
        self.listWidget.clear()

        item = self.loginDatabase.conn.execute("select * from CONTACTBOOK where contact like 'T%' or contact like 'U%' "
                                               "or contact like 'V%' or contact like 'W%' or contact like 'X%' "
                                               "or contact like 'Y%' or contact like 'Z%' "
                                               ).fetchall()
        for i in item:
            self.listWidget.addItem(str(i))


    @pyqtSlot()
    def on_click_add(self):

        print('add contact request')
        name_to_add = self.contact_lineEdit.text()
        phone_to_add = self.phone_lineEdit.text()
        birthsday_to_add = self.birthsday_lineEdit.text()
        self.validContactAdd(name_to_add, phone_to_add, birthsday_to_add)

    @pyqtSlot()
    def on_click_update(self):

        print('update contact request')
        name_to_update = self.contact_lineEdit.text()
        phone_to_update = self.phone_lineEdit.text()
        birthsday_to_update = self.birthsday_lineEdit.text()
        id_to_update = self.id_lineEdit.text()
        self.validContactUpdate(name_to_update, phone_to_update, birthsday_to_update, id_to_update)
        print(id_to_update+name_to_update+phone_to_update+birthsday_to_update)
        #self.loginDatabase.conn.execute("UPDATE ")


    @pyqtSlot()
    def on_click_delete(self):

        print('delete contact request')
        #name_to_update = self.contact_lineEdit.text()
        #phone_to_update = self.phone_lineEdit.text()
        #birthsday_to_update = self.birthsday_lineEdit.text()
        id_to_delete = self.id_lineEdit.text()
        print(id_to_delete)
        #self.loginDatabase.conn.execute("UPDATE ")
        self.loginDatabase.conn.execute("DELETE FROM CONTACTBOOK WHERE CONTACTID = ?",
                                        (id_to_delete))
        self.loginDatabase.conn.commit()

    @pyqtSlot()
    def on_click_unlog(self):
        self.loginDatabase.conn.execute(
            "UPDATE DEFAULTUSER SET USERNAME = 'UNLOG', PASSWORD = 'UNLOG'")
        self.loginDatabase.conn.commit()
        self.close()
        self.loginDatabase.conn.close()
        self.mainWindow = login.MainDialog()
        self.mainWindow.show()




class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, name='admin'):
        super().__init__()
        self.setupUi(self)
        self.loginDatabase = LoginDatabase('phone.db')
        #print(self.loginDatabase.is_table("CONTACTS"))

        #self.label.setText('{} {}'.format(self.label.text(), name))
        #NAME CAN BE USED
        #print(name)
        self.button_1.clicked.connect(self.on_click1)
        self.button_2.clicked.connect(self.on_click2)
        self.button_3.clicked.connect(self.on_click3)
        self.button_4.clicked.connect(self.on_click4)
        self.button_5.clicked.connect(self.on_click5)
        self.button_6.clicked.connect(self.on_click6)

        self.button_add.clicked.connect(self.on_click_add)
        self.button_update.clicked.connect(self.on_click_update)
        self.button_delete.clicked.connect(self.on_click_delete)

        self.button_unlog.clicked.connect(self.on_click_unlog)
        #self.button_1.pressed(print("asd"))
        gridLayout = QGridLayout(self.centralwidget)
        gridLayout.addWidget(self.listWidget)
        gridLayout.addWidget(self.label)
        gridLayout.addWidget(self.label_2)
        #self.button_2.clicked.connect(self.listWidget.clear())


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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())