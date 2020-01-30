# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
# import Qt
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
#导入designer工具生成的login模块
from main_login import Ui_Dialog
# from logins import Ui_Dialog
from windows import Ui_MainWindow

from main.main import user_interface
from main.main import System_Init,file_system
from main.main import Create_UFD,Delete_UFD,Read_File,Open,Close,show,Write_File
from main.main import Print_UFD,Quit_System,show_free_disk,Print_Help


class MyMainForm(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.dipaly)
        
    def dipaly(self):
        user_name = self.lineEdit.text()
        user_passwd = self.lineEdit_2.text()
        System_Init(user_name,user_passwd)
        print(f'用户名 ：{user_name} \n密码：{user_passwd}')



class next_windows(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(next_windows,self).__init__(parent=parent)
        self.setupUi(self)
        
        '''
        self.pushButton.clicked.connect(self.delete)       #删除文件
        self.pushButton_2.clicked.connect(self.create)     #创建文件
        self.pushButton_3.clicked.connect(self.open_file)
        self.pushButton_4.clicked.connect(self.close_file)
        self.pushButton_5.clicked.connect(self.write)
        self.pushButton_6.clicked.connect(self.read)
        self.pushButton_7.clicked.connect(self.ls)
        self.pushButton_8.clicked.connect(self.show)
        self.pushButton_9.clicked.connect(self.out)
        self.pushButton_10.clicked.connect(self.help)
        # self.pushButton.clicked.connect()
        # self.pushButton.clicked.connect()
    '''
    def create(self):
        Create_UFD()
        
    def delete(self):
        Delete_UFD()
        
    def open_file(self):
        Open()
        
    def close_file(self):
        Close()
        
    def write(self):
        Write_File()
        
    def ls(self):
        Print_UFD()
        
    def read(self):
        show()
        
    def show(self):
        show_free_disk()
        
    def out(self):
        Quit_System()
        
    def help(self):
        Print_Help()
         
        
    
if __name__ == "__main__":
    
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    # main = QMainWindow
    myWin = MyMainForm()
    # myWin = Ui_Form()

    #将窗口控件显示在屏幕上
    butt = myWin.pushButton
    
    myWin.show()
    # user_name = myWin.lineEdit.text()     #用户名
    # user_passwd = myWin.lineEdit_2.text()   #密码
    # print(f'用户名 ：{user_name} \n密码：{user_passwd}')
    # butt.clicked.connect(System_Init(user_name,user_passwd))#
    butt.clicked.connect(myWin.close)       #关掉主窗口
    next_win = next_windows()
    butt.clicked.connect(next_win.show)     #开启自创刊
    
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

  # class MyMainForm(QMainWindow, Ui_Form):
#     def __init__(self, parent=None):
#         super(MyMainForm, self).__init__(parent)
#         self.setupUi(self)
#         #添加登录按钮信号和槽。注意display函数不加小括号()
#         self.pushButton.clicked.connect(self.display)
#         # self.pushButton.clicked.connect(self.close)
#         #添加退出按钮信号和槽。调用close函数
#         # self.cancel_Button.clicked.connect(self.close)
#     def display(self):
#         #利用line Edit控件对象text()函数获取界面输入
#         username = self.user_lineEdit.text()
#         password = self.pwd_lineEdit.text()
#         #利用text Browser控件对象setText()函数设置界面显示
          
    # username = 0
    # user_passwd = 0
    # System_Init(username,user_passwd)

