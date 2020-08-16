import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGraphicsScene, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

#use this "pyinstaller -F -w Knee_Angle_Analysis_V3.py" to pack into exe

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1122, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ChoseFile = QtWidgets.QPushButton(self.centralwidget)
        self.ChoseFile.setGeometry(QtCore.QRect(570, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.ChoseFile.setFont(font)
        self.ChoseFile.setObjectName("ChoseFile")
        self.FileRoot = QtWidgets.QTextBrowser(self.centralwidget)
        self.FileRoot.setGeometry(QtCore.QRect(50, 40, 511, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.FileRoot.setFont(font)
        self.FileRoot.setTabChangesFocus(False)
        self.FileRoot.setObjectName("FileRoot")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(600, 240, 480, 360))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(60, 240, 480, 360))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.MaxAngle = QtWidgets.QTextBrowser(self.centralwidget)
        self.MaxAngle.setGeometry(QtCore.QRect(220, 130, 111, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.MaxAngle.setFont(font)
        self.MaxAngle.setObjectName("MaxAngle")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(430, 130, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Check = QtWidgets.QPushButton(self.centralwidget)
        self.Check.setGeometry(QtCore.QRect(960, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Check.setFont(font)
        self.Check.setObjectName("Check")
        self.MiniAngle = QtWidgets.QTextBrowser(self.centralwidget)
        self.MiniAngle.setGeometry(QtCore.QRect(600, 130, 111, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.MiniAngle.setFont(font)
        self.MiniAngle.setObjectName("MiniAngle")
        self.labelp1 = QtWidgets.QLabel(self.centralwidget)
        self.labelp1.setGeometry(QtCore.QRect(60, 240, 480, 360))
        self.labelp1.setText("")
        self.labelp1.setObjectName("labelp1")
        self.labelp2 = QtWidgets.QLabel(self.centralwidget)
        self.labelp2.setGeometry(QtCore.QRect(600, 240, 480, 360))
        self.labelp2.setText("")
        self.labelp2.setObjectName("labelp2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(240, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(650, 190, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.MachineAngle = QtWidgets.QTextBrowser(self.centralwidget)
        self.MachineAngle.setGeometry(QtCore.QRect(980, 130, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.MachineAngle.setFont(font)
        self.MachineAngle.setObjectName("MachineAngle")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(760, 130, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(700, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 600, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 630, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(600, 610, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(870, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "膝關節角度分析系統"))
        self.ChoseFile.setText(_translate("MainWindow", "選擇檔案"))
        self.FileRoot.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; font-size:18pt;\">資料路徑</span></p></body></html>"))
        self.MaxAngle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\';\">最大值</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "量測最大角度"))
        self.label_3.setText(_translate("MainWindow", "量測最小角度"))
        self.Check.setText(_translate("MainWindow", "確認"))
        self.MiniAngle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\';\">最小值</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "膝關節角度"))
        self.label_5.setText(_translate("MainWindow", "股骨相對於脛骨的External/Internal Rotation 角度"))
        self.MachineAngle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">調整角度</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "建議下次目標角度"))
        self.label_7.setText(_translate("MainWindow", "當前目標角度"))
        self.label_8.setText(_translate("MainWindow", "在60~90度的區間 82%的機率誤差在正負3度內"))
        self.label_9.setText(_translate("MainWindow", "在90~112.5度的區間 87%的機率誤差在正負3度內"))
        self.label_10.setText(_translate("MainWindow", "若此角度差超過10度以上，膝關節角度誤差有機率超過5度"))

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.ChoseFile.clicked.connect(self.pickfile)
        self.Check.clicked.connect(self.startcaculate)
        self.lineEdit.setValidator(QtGui.QIntValidator())  # 设置只能输入int类型的数据
        self.step1 = 0

    def pickfile(self):
        self.fileName1, filetype = QFileDialog.getOpenFileName(self,"選取檔案", "./","Text Files (*.txt);;All Files (*)")  # 設定副檔名過濾,注意用雙分號間隔
        self.FileRoot.setText(self.fileName1)

        self.labelp1.setPixmap(QPixmap(""))
        self.labelp2.setPixmap(QPixmap(""))

        self.MaxAngle.setText("")
        self.MiniAngle.setText("")

        self.step1 = 1

    def startcaculate(self):

        if self.step1 == 0:
            return

        f = open(self.fileName1)

        # 讀檔轉換成陣列
        line = f.readline()
        data_array = []
        while line:
            num = list(map(str, line.split('\t')))
            data_array.append(num)
            line = f.readline()
        f.close()
        data_array = np.array(data_array)

        [m] = data_array.shape
        print(m)
        data_size = int((m-2)/2)
        print(data_size)

        # 去頭尾找大小
        Noise = 400  # 頭尾要去掉的size

        # 資料大小篩選
        if data_size <= 3 * Noise:
            self.FileRoot.setText("資料大小不足，請重新選擇測量時間5分以上的紀錄")
            self.fileName1 = ""
            return

        sensor_X1 = np.zeros((data_size, 1))
        sensor_Y1 = np.zeros((data_size, 1))

        sensor_X2 = np.zeros((data_size, 1))
        sensor_Y2 = np.zeros((data_size, 1))

        if data_array[2][0] != data_array[3][0]:
            flat = 1
            print('odd')
        else:
            flat = 0
            print('even')

        k = 0
        for i in range(data_size*2-1):
            #讓數據成對收集 與txt裡的第2,3筆資料順序一樣 (1,2)為系統字串
            if data_array[3 + i][0] != data_array[2][0] and data_array[2 + i][0] == data_array[2][0]:
                print(i)
                sensor_X1[k] = float(data_array[2 +  i][9])
                sensor_Y1[k] = float(data_array[2 +  i][10])

                sensor_X2[k] = float(data_array[3 +  i][9])
                sensor_Y2[k] = float(data_array[3 +  i][10])
                print(sensor_X2[k])
                print(k)
                k = k + 1

        print(k)
        YXG = np.zeros((data_size, 1))
        knee_angle_degree = np.zeros((data_size, 1))

        for i in range(data_size):
            x50x = sensor_X1[i]
            x50y = sensor_Y1[i]

            x51x = sensor_X2[i]
            x51y = sensor_Y2[i]

            YXG[i] = abs(sensor_Y1[i] - sensor_Y2[i])

            th_vecx_1 = math.cos(math.radians(x50x))
            th_vecx_3 = math.sin(math.radians(x50x))
            th_vecy_2 = math.cos(math.radians(x50y))
            th_vecy_3 = math.sin(math.radians(x50y))

            sh_vecx_1 = math.cos(math.radians(x51x))
            sh_vecx_3 = math.sin(math.radians(x51x))
            sh_vecy_2 = math.cos(math.radians(x51y))
            sh_vecy_3 = math.sin(math.radians(x51y))

            th_cross_1 = th_vecx_3 * th_vecy_2
            th_cross_2 = th_vecx_1 * th_vecy_3
            th_cross_3 = th_vecx_1 * th_vecy_2

            sh_cross_1 = sh_vecx_3 * sh_vecy_2
            sh_cross_2 = sh_vecx_1 * sh_vecy_3
            sh_cross_3 = sh_vecx_1 * sh_vecy_2

            knee_angle_rad = math.acos(th_cross_1 * sh_cross_1 + th_cross_2 * sh_cross_2 + th_cross_3 * sh_cross_3)
            knee_angle_degree[i] = math.degrees(knee_angle_rad)
            #print(knee_angle_degree[i])
        self.MaxAngle.setText(str(round(float(max(knee_angle_degree[Noise:k - Noise])), 2)))
        self.MiniAngle.setText(str(round(float(min(knee_angle_degree[Noise:k - Noise])), 2)))
        #print(str(round(float(max(knee_angle_degree[Noise:k - Noise])), 2)))
        #print(str(round(float(min(knee_angle_degree[Noise:k - Noise])), 2)))
        """
        peak = np.zeros((k-800, 1))
        peak_label = knee_angle_degree[400:k - 400]
        print(peak)
        
        shreshhold = (float(max(knee_angle_degree[400:k - 400]))+float(min(knee_angle_degree[400:k - 400])))/2
        
        for i in range(400, (k-400)):
            midum = 0
            for j in range(i-2, i+2):
                midum = midum + knee_angle_degree[j]
            peak[i-400] = midum/5 
            print(peak)
        """
        # 計算各峰值
        peak_window = 50  # 一個區間的大小
        peak_window_num = int((k - Noise * 2) / peak_window) + 1  # 切成幾組
        peak_angle = [0] * (peak_window_num + 2)  # 要比較波峰 所以加2

        # 計算各區間最大值
        for i in range(peak_window_num + 2):
            peak_angle[i] = float(max(knee_angle_degree[Noise + ((i - 1) * peak_window):Noise + (i * peak_window)]))

        # 前後區間比較小就算是波峰
        peak_maxangle = []
        for i in range(1, peak_window_num + 1):
            if peak_angle[i] >= peak_angle[i - 1] and peak_angle[i] >= peak_angle[i + 1]:
                peak_maxangle.append(peak_angle[i])

        peak_maxangle_num = len(peak_maxangle)
        print(peak_maxangle)
        # 計算有效區間波峰最大角度個數有沒有75%達標
        if len(self.lineEdit.text()) != 0:
            reach_num = 0
            avg_reach_angle = 0
            machineangle = int(self.lineEdit.text())

            for i in range(peak_maxangle_num):
                if peak_maxangle[i] >= machineangle:
                    reach_num = reach_num + 1
                    avg_reach_angle = avg_reach_angle + peak_maxangle[i]

            if (reach_num / peak_maxangle_num) >= 0.75:
                self.MachineAngle.setText(str(round(avg_reach_angle / reach_num) + 5))
            else:
                self.MachineAngle.setText(str(machineangle))

        p1 = plt.figure(num=1)
        plt.clf()
        x1 = np.linspace(1, data_size - 2, data_size - 2)
        y1 = knee_angle_degree[:data_size - 2]
        picture1 = plt.plot(x1, y1)
        plt.legend(labels=['Knee Angle'], loc='best')
        plt.xlabel('Index')
        plt.ylabel('Knee Angle')
        # self.graphicsView_2.show(figure(num=1))
        plt.savefig('Knee_Angle.png')

        plt.figure(num=2)
        plt.clf()
        x2 = np.linspace(1, data_size - 2, data_size - 2)
        y2 = YXG[:data_size - 2]
        picture2 = plt.plot(x2, y2)
        plt.axhline(10, color='r', linestyle='--')
        plt.legend(labels=['External/Internal Rotation Angle Difference', 'Confidence Threshold'], loc='best')
        plt.xlabel('Index')
        plt.ylabel('Rotation Angle Difference')
        plt.savefig('Angle_Difference.png')
        # plt.show()
        # showpicture()

        self.im1 = QPixmap("Knee_Angle.png")
        self.labelp1.setPixmap(self.im1)  # 將 image 加入 label
        self.labelp1.setScaledContents(True)

        self.im2 = QPixmap("Angle_Difference.png")
        self.labelp2.setPixmap(self.im2)
        self.labelp2.setScaledContents(True)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())