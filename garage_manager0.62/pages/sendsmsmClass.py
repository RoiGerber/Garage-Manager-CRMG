from typing import Set
from App import *
from functools import partial
from pages.themeClass import *
import json
from operator import index, itemgetter
from twilio.rest import Client 
import time


def Twillio_sender(phone_number,the_SMS):
         
        account_sid = 'AC263e4e2e9f84f386799250e71d4e35d6' 
        auth_token = 'a77c2790a9c716bcf4da9479af9470aa' 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create(  
                                      messaging_service_sid='MG9f7ba3c5f8687aff78cd30e361fb3b57',
                                      from_ = "AsGlass",
                                      body=the_SMS,      
                                      to='+972'+str(phone_number[1:]) 
                                  ) 
        time.sleep(0.1) 
        print(message.sid)


class Sendsms(MainWindow):
    def inint_ui(self):
        # nbr of costumers selected 
        self.selected_costumers = 0 
        # deep copy for the allcostumers table 
        Sendsms.deepCopy(self)
        # we get nbr of costumers 
        self.costumers_count_2 = len(self.deepcopyCostumers)
        # upload all the costumers in the UI 
        Sendsms.ShowAllCostumers(self , True)
        
    def actionbutton(self):
        self.ui.sendsms.clicked.connect(partial(Theme.openpage , self , self.ui.sendsms))
        # filter combobox listener (this methode will run when ever u change the value of combobox (name , date ))
        self.ui.filtersort_2.currentIndexChanged.connect(partial(Sendsms.ShowAllCostumers , self  , False))
        self.ui.lineEdit_search_2.textChanged.connect(partial(Sendsms.ShowAllCostumers , self  , False))
        # send message button listener 
        self.ui.sendmessagebutton.clicked.connect(partial(Sendsms.dialogue_message , self ,'Confirmation' , 'Do u want to a message !' , 1 ))
        # check all the filtered costumers
        self.ui.select_all.clicked.connect(partial(Sendsms.selectAll , self ))
    

    def deepCopy(self): 
        self.deepcopyCostumers = []
        for index , costumer in enumerate(self.allcostumer) : 
            self.deepcopyCostumers.append({
                "name" : costumer['name'] , 
                "phone_number" : costumer['phone_number'] , 
                "car_company" :  costumer['car_company'] , 
                "car_model" :  costumer['car_model'] , 
                "car_code" : costumer['car_code'],
                "notes" :  costumer['notes'] , 
                "date" : costumer['date'] ,
                "check" : False ,
                "index" : index 
            })


    def ShowAllCostumers(self , statu ):
        # clear the current list 
        Sendsms.ClearList(self  , statu)
        # get the filter option (by name , by date )
        filterd_costumers = Sendsms.filter_costumers(self)
        # sort the list of costumers 
        for i , costumer in enumerate(filterd_costumers) : 
            id = str(i)+'sendmessage_page'
            globals()['self.ui.onesubitem'+'%s' % id] = QtWidgets.QWidget(self.ui.page2)
            globals()['self.ui.onesubitem'+'%s' % id].setStyleSheet("QWidget{\n"
                                            "background-color : #2f3939  ;\n"
                                            "border-radius: 8px;\n"
                                            "}")
            globals()['self.ui.onesubitem'+'%s' % id].setObjectName("onesubitem"+id )
            
            globals()['self.ui.horizontalLayout_5'+'%s' % id] = QtWidgets.QHBoxLayout(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.horizontalLayout_5'+'%s' % id].setObjectName("horizontalLayout_5"+id)
            # check box  ###########################################################################################################
            globals()['self.ui.MoreInfo'+'%s' % id] = QtWidgets.QCheckBox(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.MoreInfo'+'%s' % id].setObjectName("MoreInfo"+id)
            globals()['self.ui.MoreInfo'+'%s' % id].setChecked(costumer['check'])
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.MoreInfo'+'%s' % id])
            # car model  text #################################################################################################################
            spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addItem(spacerItem6)
            globals()['self.ui.carmodel'+'%s' % id] = QtWidgets.QLabel(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.carmodel'+'%s' % id].setStyleSheet("color : #858585 ; ")
            globals()['self.ui.carmodel'+'%s' % id].setObjectName("carmodel"+id)
            globals()['self.ui.carmodel'+'%s' % id].setMinimumSize(QtCore.QSize(100, 0))
            globals()['self.ui.carmodel'+'%s' % id].setMaximumSize(QtCore.QSize(100, 16777215))
            globals()['self.ui.carmodel'+'%s' % id].setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.carmodel'+'%s' % id])
          
            # car model  icon ################################################################################################################
            globals()['self.ui.carmodelicon'+'%s' % id] = QtWidgets.QPushButton(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.carmodelicon'+'%s' % id].setStyleSheet("QPushButton{ \n"
                                            "background-color : none;\n"
                                            "border:none;\n"
                                            "padding : 0px ;\n"
                                            "}")
            globals()['self.ui.carmodelicon'+'%s' % id].setIcon(Theme.QIcon_from_svg(self , ':/image/essential/key-line.svg','#aef3e7'))
            globals()['self.ui.carmodelicon'+'%s' % id].setIconSize(QtCore.QSize(30, 30))
            globals()['self.ui.carmodelicon'+'%s' % id].setObjectName("carmodelicon"+id)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.carmodelicon'+'%s' % id])
            # car company  text #################################################################################################################
            spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addItem(spacerItem6)
            globals()['self.ui.companyText'+'%s' % id] = QtWidgets.QLabel(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.companyText'+'%s' % id].setStyleSheet("color : #858585 ; ")
            globals()['self.ui.companyText'+'%s' % id].setObjectName("companyText"+id)
            globals()['self.ui.companyText'+'%s' % id].setMinimumSize(QtCore.QSize(100, 0))
            globals()['self.ui.companyText'+'%s' % id].setMaximumSize(QtCore.QSize(100, 16777215))
            globals()['self.ui.companyText'+'%s' % id].setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.companyText'+'%s' % id])
          
            # car company  icon ################################################################################################################
            globals()['self.ui.Companyicon'+'%s' % id] = QtWidgets.QPushButton(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.Companyicon'+'%s' % id].setStyleSheet("QPushButton{ \n"
                                            "background-color : none;\n"
                                            "border:none;\n"
                                            "padding : 0px ;\n"
                                            "}")
            globals()['self.ui.Companyicon'+'%s' % id].setIcon(Theme.QIcon_from_svg(self , ':/image/commerce/bank-line.svg','#aef3e7'))
            globals()['self.ui.Companyicon'+'%s' % id].setIconSize(QtCore.QSize(30, 30))
            globals()['self.ui.Companyicon'+'%s' % id].setObjectName("Companyicon"+id)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.Companyicon'+'%s' % id])
            # Date text #################################################################################################################
            spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addItem(spacerItem6)
            globals()['self.ui.DateText'+'%s' % id] = QtWidgets.QLabel(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.DateText'+'%s' % id].setStyleSheet("color : #858585 ; ")
            globals()['self.ui.DateText'+'%s' % id].setObjectName("DateText"+id)
            globals()['self.ui.DateText'+'%s' % id].setMinimumSize(QtCore.QSize(120, 0))
            globals()['self.ui.DateText'+'%s' % id].setMaximumSize(QtCore.QSize(120, 16777215))
            globals()['self.ui.DateText'+'%s' % id].setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.DateText'+'%s' % id])
            # Date icon ################################################################################################################
            globals()['self.ui.DateIcon'+'%s' % id] = QtWidgets.QPushButton(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.DateIcon'+'%s' % id].setStyleSheet("QPushButton{ \n"
                                            "background-color : none;\n"
                                            "border:none;\n"
                                            "padding : 0px ;\n"
                                            "}")
            globals()['self.ui.DateIcon'+'%s' % id].setIcon(Theme.QIcon_from_svg(self ,":/image/social/date-outline-badged.svg", '#aef3e7'))
            globals()['self.ui.DateIcon'+'%s' % id].setIconSize(QtCore.QSize(30, 30))
            globals()['self.ui.DateIcon'+'%s' % id].setObjectName("DateIcon"+id)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.DateIcon'+'%s' % id])

            # User Name text  #########################################################################################################
            spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addItem(spacerItem5)
            globals()['self.ui.UserName'+'%s' % id] = QtWidgets.QLabel(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.UserName'+'%s' % id].setMinimumSize(QtCore.QSize(120, 0))
            globals()['self.ui.UserName'+'%s' % id].setMaximumSize(QtCore.QSize(120, 16777215))
            globals()['self.ui.UserName'+'%s' % id].setStyleSheet("color : #858585 ; ")
            globals()['self.ui.UserName'+'%s' % id].setObjectName("UserName"+id)
            globals()['self.ui.UserName'+'%s' % id].setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.UserName'+'%s' % id])

            # User icon ############################################################################################################
            globals()['self.ui.UserIcon'+'%s' % id] = QtWidgets.QPushButton(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.UserIcon'+'%s' % id].setStyleSheet("QPushButton{ \n"
                                        "background-color : none;\n"
                                        "border:none;\n"
                                        "padding : 0px ;\n"
                                        "}")
            globals()['self.ui.UserIcon'+'%s' % id].setIcon(Theme.QIcon_from_svg(self ,":/image/core/user-line.svg", '#aef3e7'))
            globals()['self.ui.UserIcon'+'%s' % id].setIconSize(QtCore.QSize(30, 30))
            globals()['self.ui.UserIcon'+'%s' % id].setObjectName("UserIcon"+id)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.UserIcon'+'%s' % id])
            
           
            self.ui.verticalLayout_4.addWidget(globals()['self.ui.onesubitem'+'%s' % id])
            # get all the informations about this (i th ) costumer 
            globals()['self.ui.UserName'+'%s' % id].setText(costumer['name'])
            globals()['self.ui.DateText'+'%s' % id].setText(costumer['date'])
            globals()['self.ui.companyText'+'%s' % id].setText(costumer['car_company'])
            globals()['self.ui.carmodel'+'%s' % id].setText(costumer['car_model'])
            # show more details about the costumer 
            globals()['self.ui.MoreInfo'+'%s' % id].clicked.connect(partial(Sendsms.details_costumer , self  , costumer))
            

        # update the count of constumer
        self.costumers_count_2 = len(filterd_costumers)
        # add vertical space 
        self.S5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_4.addItem(self.S5)


    def details_costumer(self , costumer ) : 
        name  = costumer['name']
        phone_number = costumer['phone_number']
        car_company = costumer['car_company']
        car_model = costumer['car_model']
        car_code = costumer['car_code']
        notes = costumer['notes']
        index = costumer['index'] 
        check = costumer['check']
    
        if check : 
            self.deepcopyCostumers[index]['check'] = False
            self.selected_costumers -= 1 
        else : 
            
            self.deepcopyCostumers[index]['check'] = True
            self.selected_costumers += 1 
            
        self.ui.costumersselected.setText(str(self.selected_costumers)+'  Costumers selected ')

    

    def ClearList(self , statu ):
        if not statu:
            for i in range(self.costumers_count_2) : 
                id = str(i)+'sendmessage_page'
                globals()['self.ui.onesubitem'+'%s' % id].deleteLater()
                globals()['self.ui.horizontalLayout_5'+'%s' % id].deleteLater()
                globals()['self.ui.UserIcon'+'%s' % id].deleteLater()
                globals()['self.ui.UserName'+'%s' % id].deleteLater()
                globals()['self.ui.DateIcon'+'%s' % id].deleteLater()
                globals()['self.ui.DateText'+'%s' % id].deleteLater()
                globals()['self.ui.MoreInfo'+'%s' % id].deleteLater()
            self.ui.verticalLayout_4.removeItem(self.S5)


    def filter_costumers(self): 
        filter_sort = self.ui.filtersort_2.currentIndex()
        new_tab = []
        searchby = ""

        if self.ui.searchcombobox_2.currentIndex() == 0 :
            searchby = "name"
        elif self.ui.searchcombobox_2.currentIndex() == 1 :
            searchby = "car_company"
        else : 
            searchby = "car_model"
        for costumer in self.deepcopyCostumers :
            if costumer[searchby].upper().startswith(self.ui.lineEdit_search_2.text().upper()) : 
                new_tab.append(costumer)

        if filter_sort == 0 : 
            # sort by name a --- z
            filterd_costumers  = sorted(new_tab, key=itemgetter('name')) 
        elif filter_sort == 1 :
            # sort by name z --- a 
            filterd_costumers = sorted(new_tab, key=itemgetter('name'), reverse=True)
        elif filter_sort == 2 :
            # sort by date earliest
            filterd_costumers  = sorted(new_tab, key=itemgetter('date')) 
        else :
            # sort by date latest
            filterd_costumers = sorted(new_tab, key=itemgetter('date'), reverse=True)
        return filterd_costumers
    



    # dialogue message 
    def dialogue_message(self , titel ,  body_message , statu) : 
        # add darken layer
        self.dialogue()
        self.layoutSTACK.addWidget(self.ui.widget_main)
        self.layoutSTACK.addWidget(self.verticalWidget)
        self.widgetSTACK = QtWidgets.QWidget()
        self.widgetSTACK.setLayout(self.layoutSTACK)
        self.setCentralWidget(self.widgetSTACK)
        self.bodymessage.setText(body_message)
        self.titeldialgue.setText(titel)
        self.redbutton.clicked.connect(partial(Sendsms.close_dialogue , self ))
        # 1 == conformation (yes or No ) , 2 == information (one button 'okay ')
        if statu == 1 : 
            self.greenbutton.clicked.connect(partial(Sendsms.sendmessage , self ))
        else : 
            self.greenbutton.hide()
            self.redbutton.setText('Okay')

    def sendmessage(self):
        print(self.selected_costumers)
        if self.selected_costumers > 0 : 
            if self.ui.lineEdit_message.text() != "":
                for index , costumer in enumerate(self.deepcopyCostumers) : 
                    if costumer['check'] : 
                        costumer_name = costumer['name']
                        costumer_phone = costumer['phone_number'] 
                        the_SMS = self.ui.lineEdit_message.text()
                        print('send message to', costumer_name, 'in this number' , costumer_phone)
                        # u can place here your code to send SMS u have the name of the costumer 
                        # and the phone number as well as the message itself 

                        try:
                            Twillio_sender(costumer_phone,the_SMS)
                            
                        except:
                            pass
                        """
                             PLACE SMS CODE HERE 
                        """


                        # uncheck the selected costumer 
                        self.deepcopyCostumers[index]['check'] = False

                        
                # close the dialogue
                Sendsms.close_dialogue(self)
                # success message 
                Sendsms.dialogue_message(self ,"Attention" , 'The message has been sent successfully  !' , 2)
                # clear the line message 
                self.ui.lineEdit_message.setText('')
                # update the UI 
                Sendsms.ShowAllCostumers(self , False)
            else : 
                Sendsms.close_dialogue(self)
                Sendsms.dialogue_message(self ,"Attention" , 'Please entre the meassage to send  !' , 2)
        else : 
            Sendsms.close_dialogue(self)
            Sendsms.dialogue_message(self ,"Attention" , 'Please select at least one costumer !' , 2)
        
    def close_dialogue(self) : 
        self.layoutSTACK.removeWidget(self.verticalWidget)
    
    # select all 
    def selectAll(self): 
        filterd_costumers = Sendsms.filter_costumers(self)
        # sort the list of costumers *
        selected = False
        if self.ui.select_all.isChecked():
            selected = True
            self.ui.costumersselected.setText(str(len(filterd_costumers))+' Costumers selected ')
            self.selected_costumers = len(filterd_costumers)
        else : 
            self.ui.costumersselected.setText('0 Costumers selected ')
            selected = False
            self.selected_costumers = 0
       
        for i , costumer in enumerate(filterd_costumers) :
            id = str(i)+'sendmessage_page'
            globals()['self.ui.MoreInfo'+'%s' % id].setChecked(selected)
            index = costumer['index'] 
            if self.ui.select_all.isChecked():
                self.deepcopyCostumers[index]['check'] = True
            else : 
                self.deepcopyCostumers[index]['check'] = False
