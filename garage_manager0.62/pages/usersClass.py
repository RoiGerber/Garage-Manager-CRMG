from os import stat
from typing import Text
from App import *
from functools import partial
from pages.themeClass import *
from operator import index, itemgetter
from pages.sendsmsmClass import *
import json 
from datetime import datetime

class Users(MainWindow):

    def inint_ui(self):
        # we get nbr of costumers 
        self.costumers_count = len(self.allcostumer)
        # upload all the costumers in the UI 
        Users.ShowAllCostumers(self , True)
        
    def actionbutton(self):
        self.ui.users.clicked.connect(partial(Theme.openpage , self , self.ui.users))
        # filter combobox listener (this methode will run when ever u change the value of combobox (name , date ))
        self.ui.filtersort.currentIndexChanged.connect(partial(Users.ShowAllCostumers , self  , False))
        self.ui.lineEdit_search.textChanged.connect(partial(Users.ShowAllCostumers , self  , False))

    def ShowAllCostumers(self , statu ):
        # clear the current list 
        Users.ClearList(self  , statu)
        # get the filter option (by name , by date )
        filterd_costumers = Users.filter_costumers(self)
        # sort the list of costumers 
        for i , costumer in enumerate(filterd_costumers) : 
            id = str(i) 
            globals()['self.ui.onesubitem'+'%s' % id] = QtWidgets.QWidget(self.ui.page2)
            globals()['self.ui.onesubitem'+'%s' % id].setStyleSheet("QWidget{\n"
                                            "background-color : #2f3939  ;\n"
                                            "border-radius: 8px;\n"
                                            "}")
            globals()['self.ui.onesubitem'+'%s' % id].setObjectName("onesubitem"+id )
            
            globals()['self.ui.horizontalLayout_5'+'%s' % id] = QtWidgets.QHBoxLayout(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.horizontalLayout_5'+'%s' % id].setObjectName("horizontalLayout_5"+id)
            # modify costumers button ###########################################################################################################
            globals()['self.ui.modifyCostumer'+'%s' % id] = QtWidgets.QPushButton(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.modifyCostumer'+'%s' % id].setStyleSheet("QPushButton{ \n"
                                            "background-color : none;\n"
                                            "border:none;\n"
                                            "padding : 0px ;\n"
                                            "}")
            globals()['self.ui.modifyCostumer'+'%s' % id].setIcon(Theme.QIcon_from_svg(self ,":/image/essential/edit-solid.svg", '#aef3e7'))
            globals()['self.ui.modifyCostumer'+'%s' % id].setIconSize(QtCore.QSize(30, 30))
            globals()['self.ui.modifyCostumer'+'%s' % id].setObjectName("modifyCostumer"+id)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.modifyCostumer'+'%s' % id])

            # delete costumers button ###########################################################################################################
            globals()['self.ui.DeleteCostumer'+'%s' % id] = QtWidgets.QPushButton(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.DeleteCostumer'+'%s' % id].setStyleSheet("QPushButton{ \n"
                                            "background-color : none;\n"
                                            "border:none;\n"
                                            "padding : 0px ;\n"
                                            "}")
            globals()['self.ui.DeleteCostumer'+'%s' % id].setIcon(Theme.QIcon_from_svg(self ,":/image/essential/trash-solid.svg", '#aef3e7'))
            globals()['self.ui.DeleteCostumer'+'%s' % id].setIconSize(QtCore.QSize(30, 30))
            globals()['self.ui.DeleteCostumer'+'%s' % id].setObjectName("DeleteCostumer"+id)
            globals()['self.ui.horizontalLayout_5'+'%s' % id].addWidget(globals()['self.ui.DeleteCostumer'+'%s' % id])
            # more info button ###########################################################################################################
            globals()['self.ui.MoreInfo'+'%s' % id] = QtWidgets.QPushButton(globals()['self.ui.onesubitem'+'%s' % id])
            globals()['self.ui.MoreInfo'+'%s' % id].setStyleSheet("QPushButton{ \n"
                                            "background-color : none;\n"
                                            "border:none;\n"
                                            "padding : 0px ;\n"
                                            "}")
            globals()['self.ui.MoreInfo'+'%s' % id].setIcon(Theme.QIcon_from_svg(self ,":/image/core/info-standard-line.svg", '#aef3e7'))
            globals()['self.ui.MoreInfo'+'%s' % id].setIconSize(QtCore.QSize(30, 30))
            globals()['self.ui.MoreInfo'+'%s' % id].setObjectName("MoreInfo"+id)
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
            
           
            self.ui.verticalLayout_2.addWidget(globals()['self.ui.onesubitem'+'%s' % id])
            # get all the informations about this (i th ) costumer 
            globals()['self.ui.UserName'+'%s' % id].setText(costumer['name'])
            globals()['self.ui.DateText'+'%s' % id].setText(costumer['date'])
            globals()['self.ui.companyText'+'%s' % id].setText(costumer['car_company'])
            globals()['self.ui.carmodel'+'%s' % id].setText(costumer['car_model'])
            # show more details about the costumer 
            globals()['self.ui.MoreInfo'+'%s' % id].clicked.connect(partial(Users.details_costumer , self  , costumer))
            # delete costumer 
            globals()['self.ui.DeleteCostumer'+'%s' % id].clicked.connect(partial(Users.deleteCostumer_MESSAGE , self ,costumer['phone_number']))
            # modify costumer 
            globals()['self.ui.modifyCostumer'+'%s' % id].clicked.connect(partial(Users.mofifyCostumer , self ,costumer))
            

        # update the count of constumer
        self.costumers_count = len(filterd_costumers)
        # add vertical space 
        self.S4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_2.addItem(self.S4)


    def details_costumer(self , costumer ) : 
        name  = costumer['name']
        phone_number = costumer['phone_number']
        car_company = costumer['car_company']
        car_model = costumer['car_model']
        car_code = costumer['car_code']
        notes = costumer['notes']
        self.dialogue_costumersinfo()
        self.layoutSTACK.addWidget(self.ui.widget_main)
        self.layoutSTACK.addWidget(self.verticalWidget)
        self.widgetSTACK = QtWidgets.QWidget()
        self.widgetSTACK.setLayout(self.layoutSTACK)
        self.setCentralWidget(self.widgetSTACK)
        # fill all the infos in the dialogue pop up 
        self.label_name.setText(name)
        self.label_phone.setText(phone_number)
        self.label_carcompany.setText(car_company)
        self.label_carmodel.setText(car_model)
        self.label_carcode.setText(car_code)
        self.label_notes.setText(notes)
        self.okaybutton.clicked.connect(partial(Users.close_dialogue_costumers , self ) )

    

    def ClearList(self , statu ):
        if not statu:
            for i in range(self.costumers_count) : 
                id = str(i)
                globals()['self.ui.onesubitem'+'%s' % id].deleteLater()
                globals()['self.ui.horizontalLayout_5'+'%s' % id].deleteLater()
                globals()['self.ui.UserIcon'+'%s' % id].deleteLater()
                globals()['self.ui.UserName'+'%s' % id].deleteLater()
                globals()['self.ui.DateIcon'+'%s' % id].deleteLater()
                globals()['self.ui.DateText'+'%s' % id].deleteLater()
                globals()['self.ui.MoreInfo'+'%s' % id].deleteLater()
            self.ui.verticalLayout_2.removeItem(self.S4)


    def filter_costumers(self): 
        filter_sort = self.ui.filtersort.currentIndex()
        new_tab = []
        searchby = ""

        if self.ui.searchcombobox.currentIndex() == 0 :
            searchby = "name"
        elif self.ui.searchcombobox.currentIndex() == 1 :
            searchby = "car_company"
        else : 
            searchby = "car_model"
        for costumer in self.allcostumer :
            if costumer[searchby].upper().startswith(self.ui.lineEdit_search.text().upper()) : 
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
    

    def close_dialogue_costumers(self) : 
        self.layoutSTACK.removeWidget(self.verticalWidget)
    
    

    # dialogue message 
    def deleteCostumer_MESSAGE(self , phone ):
        Users.dialogue_message(self ,  'Confirmation' , 'Do u want to save this costumer !' , 1 , phone)

    def deleteCostumer(self , phone_number ): 
        index_to_delete = -1
        for index , costumer in enumerate(self.allcostumer) : 
            if costumer['phone_number'] == phone_number : 
                index_to_delete = index 
        
        if index_to_delete >= 0 : 
            self.allcostumer.pop(index_to_delete)
            # update the json file and the data base 
            # save this in json file 
            a_file = open("database_costumers.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            json_object['users'] = self.allcostumer
            a_file = open("database_costumers.json", "w")
            json.dump(json_object, a_file , indent= 4 )
            a_file.close()

            # update the UI in the users page 
            Users.ShowAllCostumers(self , False)
            # update the UI in the Send message page 
            Sendsms.deepCopy(self)
            Sendsms.ShowAllCostumers(self , False)
            # close the dialogue 
            Users.close_dialogue(self)
    
    

    def dialogue_message(self , titel ,  body_message , statu , phone_number) : 
            # add darken layer
            self.dialogue()
            if phone_number != 'just_message':
                self.layoutSTACK.addWidget(self.ui.widget_main)
            self.layoutSTACK.addWidget(self.verticalWidget)
            self.widgetSTACK = QtWidgets.QWidget()
            self.widgetSTACK.setLayout(self.layoutSTACK)
            self.setCentralWidget(self.widgetSTACK)
            self.bodymessage.setText(body_message)
            self.titeldialgue.setText(titel)
            self.redbutton.clicked.connect(partial(Users.close_dialogue , self ))
            # 1 == conformation (yes or No ) , 2 == information (one button 'okay ')
            if statu == 1 : 
                self.greenbutton.clicked.connect(partial(Users.deleteCostumer , self  , phone_number))
            else : 
                self.greenbutton.hide()
                self.redbutton.setText('Okay')
    

    # close the dialogue 
    def close_dialogue(self): 
        self.layoutSTACK.removeWidget(self.verticalWidget)

    def mofifyCostumer(self , costumer):
        self.dialogue_modify_costumer()
        self.layoutSTACK.addWidget(self.ui.widget_main)
        self.layoutSTACK.addWidget(self.verticalWidget_modify)
        self.widgetSTACK = QtWidgets.QWidget()
        self.widgetSTACK.setLayout(self.layoutSTACK)
        self.setCentralWidget(self.widgetSTACK)

        # fill the info of the costumer 

        self.line_name.setText(costumer['name'])  
        self.line_phone.setText(costumer['phone_number']) 
        self.line_carcompany.setText(costumer['car_company'])
        self.line_carmodel.setText(costumer['car_model'])
        self.line_carcode.setText(costumer['car_code'])
        self.line_notes.setText(costumer['notes'])


        self.cancel_button.clicked.connect(partial(Users.close_dialogue_modify  , self  ))
        self.modify_button.clicked.connect(partial(Users.applyModification , self ,costumer['phone_number'] ))
        
    
    def close_dialogue_modify(self): 
        self.layoutSTACK.removeWidget(self.verticalWidget_modify)

    def applyModification(self , old_phone):
        # get all informations about the costumer
        name = self.line_name.text()
        phone_number = self.line_phone.text()
        car_company = self.line_carcompany.text()
        car_model= self.line_carmodel.text()
        car_code = self.line_carcode.text()
        notes = self.line_notes.text()
        # find the user index 
        index_user = -1
        new_exists = True
        for index , costumer in enumerate(self.allcostumer):
            if costumer['phone_number'] == old_phone : 
                index_user = index
                break
        for index , costumer in enumerate(self.allcostumer):
            print(index , phone_number , old_phone ,costumer['phone_number'])
            if costumer['phone_number'] == phone_number and phone_number != old_phone:
                new_exists = False
                break

        if new_exists : 
            if name != '' and phone_number != '' and car_company != '' and car_model != '' and car_code != '' and notes != '' : 
                # here we do our query to save this costumer in json file 
                one_costumer = {
                    "name" :name , 
                    "phone_number" : phone_number , 
                    "car_company" :car_company , 
                    "car_model" :car_model , 
                    "car_code" :car_code , 
                    "notes" :notes , 
                    "date" : datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                }
                self.allcostumer[index_user]=one_costumer
                # save this in json file 
                a_file = open("database_costumers.json", "r")
                json_object = json.load(a_file)
                a_file.close()
                json_object['users'] = self.allcostumer
                a_file = open("database_costumers.json", "w")
                json.dump(json_object, a_file , indent= 4 )
                a_file.close()
                Users.close_dialogue_modify(self)
                Users.dialogue_message(self ,'Attention' , 'User has been successfully changed ' , 2 , "just_message")

                # update the UI in the users page 
                Users.ShowAllCostumers(self , False)
                # update the UI in the Send message page 
                Sendsms.deepCopy(self)
                Sendsms.ShowAllCostumers(self , False)
            else:
                Users.dialogue_message(self ,'Attention' , 'Please entre all the information about the costumer !' , 2 , "just_message")
        else:
            Users.dialogue_message(self ,'Attention' , 'This number has been alredy entred !' , 2 , "just_message")


    

    
            