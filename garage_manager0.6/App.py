
from PyQt5 import QtCore
from modules import *
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
import sys
from Uiapp import Ui_MainWindow
################################################################################################### the main app pages
class MainWindow(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.layoutSTACK = QStackedLayout()
        self.layoutSTACK.setStackingMode(QStackedLayout.StackAll)
        # table of all the costumers 
        self.allcostumer = []
        ###################################################### Add user  page
        Adduser.inint_ui(self)
        Adduser.actionbutton(self)
        ###################################################### Users page 
        Users.inint_ui(self)
        Users.actionbutton(self)
        ###################################################### Send sms  page
        Sendsms.inint_ui(self)
        Sendsms.actionbutton(self)
        ###################################################### Theme page
        Theme.inint_ui(self)
        Theme.actionbutton(self)
    

    def dialogue(self):
        self.verticalWidget = QtWidgets.QWidget()
        self.verticalWidget.setStyleSheet("background-color : rgba(0,0,0,100) ; ")
        self.verticalWidget.setObjectName("verticalWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalWidget)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalWidget_2 = QtWidgets.QWidget(self.verticalWidget)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(600, 0))
        self.verticalWidget_2.setStyleSheet("QWidget{\n"
                                        "background-color : rgb(35,35,35)  ;\n"
                                        "border-radius: 5px;\n"
                                        "border: 6px solid #2d3838;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QLable{\n"
                                        "color : white ; \n"
                                        "font: 12pt \"Segoe UI\";\n"
                                        "\n"
                                        "}")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titeldialgue = QtWidgets.QLabel(self.verticalWidget_2)
        self.titeldialgue.setStyleSheet("\n"
                                        "\n"
                                        "QLabel{\n"
                                        "font: 16pt \"BigNoodleTitling\";\n"
                                        "color : white ;\n"
                                        "padding-left : 10px ;\n"
                                        "border : none ; \n"
                                        "\n"
                                        "}")
        self.titeldialgue.setObjectName("titeldialgue")
        self.verticalLayout_2.addWidget(self.titeldialgue)
        self.bodymessage = QtWidgets.QLabel(self.verticalWidget_2)
        self.bodymessage.setStyleSheet("QLabel{\n"
                                        "\n"
                                        "font-size : 12px ; \n"
                                        "color : white ; \n"
                                        "background-color : #2d3838 ; \n"
                                        "border-radius: 5px;\n"
                                        "padding-left : 9px;\n"
                                        "padding-right : 9px;\n"
                                        "padding-top : 9px;\n"
                                        "padding-bottom : 20px;\n"
                                        "border : none ; \n"
                                        "}")
        self.bodymessage.setObjectName("bodymessage")
        self.verticalLayout_2.addWidget(self.bodymessage)
        self.horizontalWidget = QtWidgets.QWidget(self.verticalWidget_2)
        self.horizontalWidget.setStyleSheet("border : none ; ")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.greenbutton = QtWidgets.QPushButton(self.horizontalWidget)
        self.greenbutton.setMinimumSize(QtCore.QSize(148, 0))
        self.greenbutton.setStyleSheet("\n"
                                                "\n"
                                                "\n"
                                                "QPushButton{ \n"
                                                "background-color: #2f3939 ;\n"
                                                "border-radius: 5px;\n"
                                                "color : white ;\n"
                                                "border: none;\n"
                                                "font: 14pt \"BigNoodleTitling\";\n"
                                                "padding-top : 7px ;\n"
                                                "padding-bottom : 7px ;\n"
                                                "padding-right : 27px ;\n"
                                                "padding-left : 27px ;\n"
                                                " }\n"
                                                "QPushButton:hover{\n"
                                                "border: 3px solid white;\n"
                                                "padding : 4px ;\n"
                                                "}\n"
                                                "")
        self.greenbutton.setObjectName("greenbutton")
        self.horizontalLayout_2.addWidget(self.greenbutton)
        self.redbutton = QtWidgets.QPushButton(self.horizontalWidget)
        self.redbutton.setStyleSheet("QPushButton{ \n"
                                        "background-color: #C33C54 ;\n"
                                        "border-radius: 5px;\n"
                                        "color : white ;\n"
                                        "border: none;\n"
                                        "font: 14pt \"BigNoodleTitling\";\n"
                                        "padding-top : 7px ;\n"
                                        "padding-bottom : 7px ;\n"
                                        "padding-right : 27px ;\n"
                                        "padding-left : 27px ;\n"
                                        " }\n"
                                        "QPushButton:hover{\n"
                                        "border: 3px solid white;\n"
                                        "padding : 4px ;\n"
                                        "}\n"
                                        "")
        self.redbutton.setObjectName("redbutton")
        self.horizontalLayout_2.addWidget(self.redbutton)
        self.verticalLayout_2.addWidget(self.horizontalWidget, 0, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addWidget(self.verticalWidget_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)

        self.redbutton.setText('No')
        self.greenbutton.setText('Yes')
    def dialogue_costumersinfo(self):
        self.verticalWidget = QtWidgets.QWidget()
        self.verticalWidget.setStyleSheet("background-color : rgba(0,0,0,100) ; ")
        self.verticalWidget.setObjectName("verticalWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalWidget)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalWidget_2 = QtWidgets.QWidget(self.verticalWidget)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(400, 0))
        self.verticalWidget_2.setStyleSheet("QWidget{\n"
                                                "background-color : rgb(35,35,35)  ;\n"
                                                "border-radius: 5px;\n"
                                                "border: 6px solid #2d3838;\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "QLable{\n"
                                                "color : white ; \n"
                                                "font: 12pt \"Segoe UI\";\n"
                                                "\n"
                                                "}")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titeldialgue = QtWidgets.QLabel(self.verticalWidget_2)
        self.titeldialgue.setStyleSheet("\n"
                                                "\n"
                                                "QLabel{\n"
                                                "font: 16pt \"BigNoodleTitling\";\n"
                                                "color : white ;\n"
                                                "padding-left : 10px ;\n"
                                                "border : none ; \n"
                                                "\n"
                                                "}")
        self.titeldialgue.setObjectName("titeldialgue")
        self.verticalLayout_2.addWidget(self.titeldialgue, 0, QtCore.Qt.AlignRight)
        self.verticalWidget_3 = QtWidgets.QWidget(self.verticalWidget_2)
        self.verticalWidget_3.setStyleSheet("QWidget{\n"
                                                "\n"
                                                "background-color : #2d3838 ; \n"
                                                "border-radius: 5px;\n"
                                                "color : #858585;\n"
                                                "}")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_name = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name, 0, QtCore.Qt.AlignRight)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.moreinfo_4 = QtWidgets.QPushButton(self.verticalWidget_3)
        self.moreinfo_4.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_4.setText("")
        
        self.moreinfo_4.setIcon(Theme.QIcon_from_svg(self ,":/image/core/user-line.svg", '#aef3e7'))
        self.moreinfo_4.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_4.setObjectName("moreinfo_4")
        self.horizontalLayout.addWidget(self.moreinfo_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_phone = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_phone.setObjectName("label_phone")
        self.horizontalLayout_3.addWidget(self.label_phone, 0, QtCore.Qt.AlignRight)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.moreinfo_6 = QtWidgets.QPushButton(self.verticalWidget_3)
        self.moreinfo_6.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_6.setText("")
        self.moreinfo_6.setIcon(Theme.QIcon_from_svg(self ,":/image/technology/mobile-phone-line.svg", '#aef3e7'))
        self.moreinfo_6.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_6.setObjectName("moreinfo_6")
        self.horizontalLayout_3.addWidget(self.moreinfo_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_carcompany = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_carcompany.setObjectName("label_carcompany")
        self.horizontalLayout_4.addWidget(self.label_carcompany, 0, QtCore.Qt.AlignRight)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.moreinfo_7 = QtWidgets.QPushButton(self.verticalWidget_3)
        self.moreinfo_7.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_7.setText("")
        self.moreinfo_7.setIcon(Theme.QIcon_from_svg(self ,":/image/commerce/bank-line.svg", '#aef3e7'))
        self.moreinfo_7.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_7.setObjectName("moreinfo_7")
        self.horizontalLayout_4.addWidget(self.moreinfo_7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.label_carmodel = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_carmodel.setObjectName("label_carmodel")
        self.horizontalLayout_5.addWidget(self.label_carmodel, 0, QtCore.Qt.AlignRight)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.moreinfo_8 = QtWidgets.QPushButton(self.verticalWidget_3)
        self.moreinfo_8.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_8.setText("")
      
        self.moreinfo_8.setIcon(Theme.QIcon_from_svg(self ,":/image/essential/key-line.svg", '#aef3e7'))
        self.moreinfo_8.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_8.setObjectName("moreinfo_8")
        self.horizontalLayout_5.addWidget(self.moreinfo_8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.label_carcode = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_carcode.setObjectName("label_carcode")
        self.horizontalLayout_6.addWidget(self.label_carcode, 0, QtCore.Qt.AlignRight)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.moreinfo_9 = QtWidgets.QPushButton(self.verticalWidget_3)
        self.moreinfo_9.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_9.setText("")
        self.moreinfo_9.setIcon(Theme.QIcon_from_svg(self ,":/image/technology/bar-code-line.svg", '#aef3e7'))
        self.moreinfo_9.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_9.setObjectName("moreinfo_9")
        self.horizontalLayout_6.addWidget(self.moreinfo_9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.label_notes = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_notes.setObjectName("label_notes")
        self.horizontalLayout_7.addWidget(self.label_notes, 0, QtCore.Qt.AlignRight)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.moreinfo_5 = QtWidgets.QPushButton(self.verticalWidget_3)
        self.moreinfo_5.setStyleSheet("QPushButton{ \n"
                                "background-color : none;\n"
                                "border:none;\n"
                                "padding : 0px ;\n"
                                "}")
        self.moreinfo_5.setText("")
     
        self.moreinfo_5.setIcon(Theme.QIcon_from_svg(self ,":/image/essential/note-edit-line.svg", '#aef3e7'))
        self.moreinfo_5.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_5.setObjectName("moreinfo_5")
        self.horizontalLayout_7.addWidget(self.moreinfo_5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.verticalWidget_3)
        self.horizontalWidget = QtWidgets.QWidget(self.verticalWidget_2)
        self.horizontalWidget.setStyleSheet("border : none ; ")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.okaybutton = QtWidgets.QPushButton(self.horizontalWidget)
        self.okaybutton.setStyleSheet("QPushButton{ \n"
                                        "background-color: #C33C54 ;\n"
                                        "border-radius: 5px;\n"
                                        "color : white ;\n"
                                        "border: none;\n"
                                        "font: 14pt \"BigNoodleTitling\";\n"
                                        "padding-top : 7px ;\n"
                                        "padding-bottom : 7px ;\n"
                                        "padding-right : 27px ;\n"
                                        "padding-left : 27px ;\n"
                                        " }\n"
                                        "QPushButton:hover{\n"
                                        "border: 3px solid white;\n"
                                        "padding : 4px ;\n"
                                        "}\n"
                                        "")
        self.okaybutton.setObjectName("okaybutton")
        self.okaybutton.setText('okay')
        self.horizontalLayout_2.addWidget(self.okaybutton)
        self.verticalLayout_2.addWidget(self.horizontalWidget, 0, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addWidget(self.verticalWidget_2, 1, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 2, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 1, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 1, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem16, 0, 1, 1, 1)        
        
        self.okaybutton.setText('okay')


        self.titeldialgue.setText("Costumer\'s informations ")
    def dialogue_modify_costumer(self):
        self.verticalWidget_modify = QtWidgets.QWidget()
        self.verticalWidget_modify.setStyleSheet("background-color : rgba(0,0,0,100) ; ")
        self.verticalWidget_modify.setObjectName("verticalWidget_modify")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalWidget_modify)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalWidget_modify_2 = QtWidgets.QWidget(self.verticalWidget_modify)
        self.verticalWidget_modify_2.setMinimumSize(QtCore.QSize(400, 0))
        self.verticalWidget_modify_2.setStyleSheet("QWidget{\n"
                                                "background-color : rgb(35,35,35)  ;\n"
                                                "border-radius: 5px;\n"
                                                "border: 6px solid #2d3838;\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "QLable{\n"
                                                "color : white ; \n"
                                                "font: 12pt \"Segoe UI\";\n"
                                                "\n"
                                                "}")
        self.verticalWidget_modify_2.setObjectName("verticalWidget_modify_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_modify_2)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titeldialgue = QtWidgets.QLabel(self.verticalWidget_modify_2)
        self.titeldialgue.setStyleSheet("\n"
                                                "\n"
                                                "QLabel{\n"
                                                "font: 16pt \"BigNoodleTitling\";\n"
                                                "color : white ;\n"
                                                "padding-left : 10px ;\n"
                                                "border : none ; \n"
                                                "\n"
                                                "}")
        self.titeldialgue.setObjectName("titeldialgue")
        self.verticalLayout_2.addWidget(self.titeldialgue, 0, QtCore.Qt.AlignRight)
        self.verticalWidget_modify_3 = QtWidgets.QWidget(self.verticalWidget_modify_2)
        self.verticalWidget_modify_3.setStyleSheet("QWidget{\n"
                                                "\n"
                                                "background-color : #2d3838 ; \n"
                                                "border-radius: 5px;\n"
                                                "color : #858585;\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit {\n"
                                                "background-color: #0A1414 ;\n"
                                                "border-radius: 0px;\n"
                                                "color : #858585 ;\n"
                                                "border: 1px solid #2f3939;\n"
                                                "padding-right: 12px;\n"
                                                "padding-top : 7px ;\n"
                                                "padding-bottom : 7px ;\n"
                                                "font: 10pt \"Segoe UI\";\n"
                                                "}\n"
                                                "QLineEdit:hover {\n"
                                                "    border: 1px solid #858585 ;\n"
                                                "}\n"
                                                "QLineEdit:focus {\n"
                                                "    border: 1px solid  #858585;\n"
                                                "    color : white ;\n"
                                                "}")
        self.verticalWidget_modify_3.setObjectName("verticalWidget_modify_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget_modify_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_name = QtWidgets.QLineEdit(self.verticalWidget_modify_3)
        self.line_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_name.setObjectName("line_name")
        self.horizontalLayout.addWidget(self.line_name)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.moreinfo_4 = QtWidgets.QPushButton(self.verticalWidget_modify_3)
        self.moreinfo_4.setStyleSheet("QPushButton{ \n"
                                "background-color : none;\n"
                                "border:none;\n"
                                "padding : 0px ;\n"
                                "}")
        self.moreinfo_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/core/user-line.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moreinfo_4.setIcon(icon)
        self.moreinfo_4.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_4.setObjectName("moreinfo_4")
        self.horizontalLayout.addWidget(self.moreinfo_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_phone = QtWidgets.QLineEdit(self.verticalWidget_modify_3)
        self.line_phone.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_phone.setObjectName("line_phone")
        self.horizontalLayout_3.addWidget(self.line_phone)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.moreinfo_6 = QtWidgets.QPushButton(self.verticalWidget_modify_3)
        self.moreinfo_6.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/technology/mobile-phone-line.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moreinfo_6.setIcon(icon1)
        self.moreinfo_6.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_6.setObjectName("moreinfo_6")
        self.horizontalLayout_3.addWidget(self.moreinfo_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_carcompany = QtWidgets.QLineEdit(self.verticalWidget_modify_3)
        self.line_carcompany.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_carcompany.setObjectName("line_carcompany")
        self.horizontalLayout_4.addWidget(self.line_carcompany)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.moreinfo_7 = QtWidgets.QPushButton(self.verticalWidget_modify_3)
        self.moreinfo_7.setStyleSheet("QPushButton{ \n"
                                "background-color : none;\n"
                                "border:none;\n"
                                "padding : 0px ;\n"
                                "}")
        self.moreinfo_7.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/commerce/bank-line.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moreinfo_7.setIcon(icon2)
        self.moreinfo_7.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_7.setObjectName("moreinfo_7")
        self.horizontalLayout_4.addWidget(self.moreinfo_7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line_carmodel = QtWidgets.QLineEdit(self.verticalWidget_modify_3)
        self.line_carmodel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_carmodel.setObjectName("line_carmodel")
        self.horizontalLayout_5.addWidget(self.line_carmodel)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.moreinfo_8 = QtWidgets.QPushButton(self.verticalWidget_modify_3)
        self.moreinfo_8.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_8.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/essential/key-line.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moreinfo_8.setIcon(icon3)
        self.moreinfo_8.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_8.setObjectName("moreinfo_8")
        self.horizontalLayout_5.addWidget(self.moreinfo_8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line_carcode = QtWidgets.QLineEdit(self.verticalWidget_modify_3)
        self.line_carcode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_carcode.setObjectName("line_carcode")
        self.horizontalLayout_6.addWidget(self.line_carcode)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.moreinfo_9 = QtWidgets.QPushButton(self.verticalWidget_modify_3)
        self.moreinfo_9.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_9.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/image/technology/bar-code-line.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moreinfo_9.setIcon(icon4)
        self.moreinfo_9.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_9.setObjectName("moreinfo_9")
        self.horizontalLayout_6.addWidget(self.moreinfo_9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_notes = QtWidgets.QLineEdit(self.verticalWidget_modify_3)
        self.line_notes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_notes.setObjectName("line_notes")
        self.horizontalLayout_7.addWidget(self.line_notes)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.moreinfo_5 = QtWidgets.QPushButton(self.verticalWidget_modify_3)
        self.moreinfo_5.setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
        self.moreinfo_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image/essential/note-edit-line.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moreinfo_5.setIcon(icon5)
        self.moreinfo_5.setIconSize(QtCore.QSize(30, 30))
        self.moreinfo_5.setObjectName("moreinfo_5")
        self.horizontalLayout_7.addWidget(self.moreinfo_5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.verticalWidget_modify_3)
        self.horizontalWidget = QtWidgets.QWidget(self.verticalWidget_modify_2)
        self.horizontalWidget.setStyleSheet("border : none ; ")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.modify_button = QtWidgets.QPushButton(self.horizontalWidget)
        self.modify_button.setMinimumSize(QtCore.QSize(100, 0))
        self.modify_button.setStyleSheet("QPushButton{ \n"
                                        "background-color: #C33C54 ;\n"
                                        "border-radius: 5px;\n"
                                        "color : white ;\n"
                                        "border: none;\n"
                                        "font: 14pt \"BigNoodleTitling\";\n"
                                        "padding-top : 7px ;\n"
                                        "padding-bottom : 7px ;\n"
                                        "padding-right : 27px ;\n"
                                        "padding-left : 27px ;\n"
                                        " }\n"
                                        "QPushButton:hover{\n"
                                        "border: 3px solid white;\n"
                                        "padding : 4px ;\n"
                                        "}\n"
                                        "")
        self.modify_button.setObjectName("modify_button")
        self.horizontalLayout_2.addWidget(self.modify_button)
        self.cancel_button = QtWidgets.QPushButton(self.horizontalWidget)
        self.cancel_button.setMinimumSize(QtCore.QSize(100, 0))
        self.cancel_button.setStyleSheet("QPushButton{ \n"
                                        "background-color: #2d3838 ;\n"
                                        "border-radius: 5px;\n"
                                        "color : white ;\n"
                                        "border: none;\n"
                                        "font: 14pt \"BigNoodleTitling\";\n"
                                        "padding-top : 7px ;\n"
                                        "padding-bottom : 7px ;\n"
                                        "padding-right : 27px ;\n"
                                        "padding-left : 27px ;\n"
                                        " }\n"
                                        "QPushButton:hover{\n"
                                        "border: 3px solid white;\n"
                                        "padding : 4px ;\n"
                                        "}\n"
                                        "")
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout_2.addWidget(self.horizontalWidget, 0, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addWidget(self.verticalWidget_modify_2, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 0, 1, 1, 1)
        # text and place holder 
        self.titeldialgue.setText("Costumer\'s informations ")
        self.line_name.setPlaceholderText("Name")
        self.line_phone.setPlaceholderText("Phone number")
        self.line_carcompany.setPlaceholderText("Car company")
        self.line_carmodel.setPlaceholderText("Car model")
        self.line_carcode.setPlaceholderText("Car code")
        self.line_notes.setPlaceholderText("Notes")
        self.modify_button.setText("Modify")
        self.cancel_button.setText("Cancel")

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = MainWindow()
    sys.exit(app.exec_())







