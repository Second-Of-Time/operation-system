# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from PyQt5.QtCore import pyqtRemoveInputHook,QCoreApplication
#导入designer工具生成的login模块
from main_login import Ui_Dialog

from windows import Ui_MainWindow

# from main.main import user_interface
from main.main import System_Init,file_system
from main.main import Create_UFD,Delete_UFD,Read_File,Open,Close,show_file,Write_File
from main.main import Print_UFD,Quit_System,show_free_disk,Print_Help

class MyMainForm(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.dipaly)
      
    def dipaly(self):
        user_name = self.lineEdit.text()
        user_passwd = self.lineEdit_2.text()
        System_Init(user_name,user_passwd)
        print('\t\t进入主系统！！！')
        # print(f'用户名 ：{user_name} \n密码：{user_passwd}')



class next_windows(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(next_windows,self).__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.lineEdit.text())
        # self.pushButton.setDefault(True)
        self.pushButton.clicked.connect(self.delete)       #删除文件
        self.pushButton_2.clicked.connect(self.creates)     #创建文件
        self.pushButton_3.clicked.connect(self.open_file)
        self.pushButton_4.clicked.connect(self.close_file)
        self.pushButton_5.clicked.connect(self.writes)
        self.pushButton_6.clicked.connect(self.reads)
        self.pushButton_7.clicked.connect(self.ls)
        self.pushButton_8.clicked.connect(self.shows)
        self.pushButton_9.clicked.connect(self.outs)
        self.pushButton_10.clicked.connect(self.helps)
        # self.pushButton.clicked.connect()
        # self.pushButton.clicked.connect()
        
    def handle_clink(self):
        self.show()

    def creates(self):
        if self.lineEdit.text():
            file_name = self.lineEdit.text()
            print(f'文件信息:{file_name}')
            Create_UFD(file_name)
        
    def delete(self):
        if self.lineEdit_2.text():
            file_name = self.lineEdit_2.text()
            # print(file_name)
            Delete_UFD(file_name)
        
    def open_file(self):
        if self.lineEdit_3.text():
            file_name = self.lineEdit_3.text()
            print(f'打开的文件：{file_name}')
            Open(file_name)
        
    def close_file(self):
        if self.lineEdit_4.text():
            file_name = self.lineEdit_4.text()
            print(f'关闭的文件名：{file_name}')
            Close(file_name)
        
    def writes(self):
        if self.lineEdit_5.text():
            file_name = self.lineEdit_5.text()
            
            Write_File(file_name)
        
    def ls(self):
        contents = Print_UFD()
        print(f'磁盘存储内容：{contents}')
        contents = ','.join(contents)
        self.textEdit.setPlainText(contents)
        
    def reads(self):
        if self.lineEdit_6.text():
            file_name = self.lineEdit_6.text()
            print(f'读取的文件：{file_name}')
            show_file(file_name)
        
    def shows(self):
        free_content = show_free_disk()
        self.textEdit.setPlainText(','.join(free_content))
        
    def outs(self):
        Quit_System()
        
    def helps(self):
        Print_Help()
        

    #接收信号str的信号槽
    def outputWritten(self, text):  
        cursor = self.textEdit.textCursor()  
        cursor.movePosition(QtGui.QTextCursor.End)  
        cursor.insertText(text)  
        self.textEdit.setTextCursor(cursor)  
        self.textEdit.ensureCursorVisible()  

def main_thing(myWin):
    user_name = myWin.lineEdit.text()     #用户名
    user_passwd = myWin.lineEdit_2.text()   #密码
    System_Init(user_name,user_passwd)
    print(f'用户名 ：{user_name} \n密码：{user_passwd}')

if __name__ == "__main__":
    pyqtRemoveInputHook()
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # app = QCoreApplication(sys.argv)
    #初始化
    # main = QMainWindow
    myWin = MyMainForm()


    #将窗口控件显示在屏幕上
    butt = myWin.pushButton
    next_win = next_windows()
    myWin.show()
    butt.clicked.connect(myWin.dipaly)
    butt.clicked.connect(next_win.handle_clink)     #开启自创刊
    butt.clicked.connect(myWin.close)       #关掉主窗口
    # #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

    
    # username = 0
    # user_passwd = 0
    # System_Init(username,user_passwd)

