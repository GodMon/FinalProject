# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TheSoftware1.3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from Evaluation import Evaluations
from faker import Faker
from SimulatedDataCreation import MyProvider
from GraphsAndInterface import Graph
from NVisualization import NVisualization
from OVisualization import OVisualization
from Odatacreation import Odatacreation


class Ui_MainWindow(object):
    def __init__(self):
        self.evaluation = Evaluations()
        self.od = Odatacreation()
        self.od.creation()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 390, 73))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 373, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 3, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 5, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 5, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 200, 385, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_3.addWidget(self.pushButton_12, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSimulating_Data = QtWidgets.QAction(MainWindow)
        self.actionSimulating_Data.setObjectName("actionSimulating_Data")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.action1_Outcome_Distribution = QtWidgets.QAction(MainWindow)
        self.action1_Outcome_Distribution.setObjectName("action1_Outcome_Distribution")
        self.action2_Cost_in_Healthcare_Pathway = QtWidgets.QAction(MainWindow)
        self.action2_Cost_in_Healthcare_Pathway.setObjectName("action2_Cost_in_Healthcare_Pathway")

        self.retranslateUi(MainWindow)

        self.pushButton.clicked.connect(Ui_MainWindow.opennvcsv)
        self.pushButton_2.clicked.connect(Ui_MainWindow.openovcsv)
        self.pushButton_3.clicked.connect(nv.Nbasicinformation)
        self.pushButton_4.clicked.connect(ov.Obasicinformation)
        self.pushButton_5.clicked.connect(nv.Noutcomedistribution)
        self.pushButton_6.clicked.connect(ov.Ooutcomedistribution)

        self.pushButton_7.clicked.connect(graph.TheBarChart1)
        self.pushButton_7.clicked.connect(self.evaluation.time_caculation1)

        self.pushButton_8.clicked.connect(graph.ThePieChart1)
        self.pushButton_8.clicked.connect(self.evaluation.time_caculation1)

        self.pushButton_9.clicked.connect(graph.TheBarChart2)
        self.pushButton_9.clicked.connect(self.evaluation.time_caculation1)

        self.pushButton_10.clicked.connect(graph.TheBoxPlot2)
        self.pushButton_10.clicked.connect(self.evaluation.time_caculation1)

        self.pushButton_12.clicked.connect(self.evaluation.time_caculation2)

        self.pushButton_13.clicked.connect(nv.Ncostrelation)
        self.pushButton_14.clicked.connect(ov.Ocostrelation)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def opennvcsv(self):
        The_data = np.loadtxt(open('NETIMISModel.csv', 'r'), delimiter=',', skiprows=0, dtype=str)
        np.set_printoptions(threshold=np.inf)
        print(The_data)

    def openovcsv(self):
        The_data = np.loadtxt(open('NRandomGeneratorData.csv', 'r'), delimiter=',', skiprows=0, dtype=str)
        np.set_printoptions(threshold=np.inf)
        print(The_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Visualizing Healthcare Pathway"))
        self.groupBox.setTitle(_translate("MainWindow", "File"))
        self.pushButton.setText(_translate("MainWindow", "NETIMIS Data"))
        self.pushButton_2.setText(_translate("MainWindow", "Random Generators Data"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Visualization"))
        self.label_2.setText(_translate("MainWindow", "1. Basic Information"))
        self.pushButton_3.setText(_translate("MainWindow", "NETIMIS"))
        self.pushButton_4.setText(_translate("MainWindow", "Random Generators"))
        self.label_3.setText(_translate("MainWindow", "2. Outcome Distribution"))
        self.pushButton_5.setText(_translate("MainWindow", "NETIMIS"))
        self.pushButton_6.setText(_translate("MainWindow", "Random Generators"))
        self.label_5.setText(_translate("MainWindow", "3. Average Cost in Outcomes"))
        self.pushButton_13.setText(_translate("MainWindow", "NETIMIS"))
        self.pushButton_14.setText(_translate("MainWindow", "Random Generators"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Evaluation"))
        self.pushButton_10.setText(_translate("MainWindow", "Box-Plot 1"))
        self.pushButton_8.setText(_translate("MainWindow", "Pie Chart 1"))
        self.pushButton_7.setText(_translate("MainWindow", "Bar Chart 1"))
        self.pushButton_9.setText(_translate("MainWindow", "Bar Chart 2"))
        self.label_4.setText(_translate("MainWindow", "Running time of finding maximum and minimum "))
        self.pushButton_12.setText(_translate("MainWindow", "Stop"))
        self.actionSimulating_Data.setText(_translate("MainWindow", "Simulating Data"))
        self.actionOpen.setText(_translate("MainWindow", "Open Data"))
        self.action1_Outcome_Distribution.setText(_translate("MainWindow", "1. Outcome Distribution"))
        self.action2_Cost_in_Healthcare_Pathway.setText(_translate("MainWindow", "2. Cost in Healthcare Pathway"))


if __name__ == "__main__":
    import sys

    fake = Faker()
    fake.add_provider(MyProvider)
    fake.Creation()
    graph = Graph()
    nv = NVisualization()
    ov = OVisualization()
    evaluation = Evaluations()
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
