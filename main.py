# Form implementation generated from reading ui file 'bot.ui'



from PyQt5 import QtCore, QtGui, QtWidgets
from sys import exit
import scraper
import webdriverdownloader as wdd


# For Firefox gecko driver: 
gecko_dd = wdd.GeckoDriverDownloader()
gecko_dd.download_and_install()

# For Chrome driver:
# chrome_dd = wdd.ChromeDriverDownloader()
# chrome_dd.download_and_install()

# For Opera driver:
# opera_dd = wdd.OperaChromiumDriverDownloader()
# opera_dd.download_and_install()


class Ui_MainWindow(object):
    def run_bot(self):
        uname = self.username.text()
        print(uname)
        pwd = self.password.text()
        print(pwd)
        hashtags = self.hashtags.text()
        if len(hashtags) > 2:
            hashtags = hashtags.split(',')

        if uname != '' and pwd != '' and len(hashtags) > 0:
            me = scraper.InstagramBot(uname, pwd)
            me.login()
            print("Logged in as " + uname)
            for hashtag in hashtags:
                me.like_posts_in(hashtag)
            else:
                print("Enter all the relevant inputs.")
                
    def reset_textfieds(self):
        self.username.setText("")
        self.password.setText("")
        self.hashtags.setText("")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 415)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/presplash.xpm"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(190, 260, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.submit_button.setObjectName("submit_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif CJK TC")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(320, 90, 171, 25))
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEnabled(True)
        self.password.setGeometry(QtCore.QRect(320, 140, 171, 25))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.hashtags = QtWidgets.QLineEdit(self.centralwidget)
        self.hashtags.setGeometry(QtCore.QRect(320, 190, 171, 25))
        self.hashtags.setObjectName("hashtags")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 90, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 140, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 190, 91, 17))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 260, 131, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.username, self.password)
        MainWindow.setTabOrder(self.password, self.hashtags)
        MainWindow.setTabOrder(self.hashtags, self.submit_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instagram Bot"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Instagram Like Bot"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.hashtags.setPlaceholderText(_translate("MainWindow", "Hashtags"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Hashtags"))
        self.pushButton.setText(_translate("MainWindow", "Reset"))
        self.submit_button.clicked.connect(self.run_bot)
        self.pushButton.clicked.connect(self.reset_textfieds)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    