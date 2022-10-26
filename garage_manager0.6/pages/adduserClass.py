from PyQt5 import QtWidgets
from App import *
from functools import partial
from pages.themeClass import *
import json
import os.path
from datetime  import datetime
from pages.usersClass import *
from pages.sendsmsmClass import *


class Adduser(MainWindow):
    def inint_ui(self):
        # test if the database file json exists 
        if os.path.isfile('database_costumers.json'):
            # File exist
            # we get all the costumers 
            with open('database_costumers.json', 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)
            self.allcostumer = json_object['users']
        else:
            # File not exist"
            # we create a new database json file 
            dictionary ={
                "users" : []
            }
            with open("database_costumers.json", "w") as outfile:
                json.dump(dictionary, outfile)
    def actionbutton(self):
        self.ui.adduser.clicked.connect(partial(Theme.openpage , self , self.ui.adduser))
        # add costumer listener 
        self.ui.button_addcostumer.clicked.connect(partial(Adduser.adduser , self ))


    def adduser(self): 
        Adduser.dialogue_message(self ,'Confirmation' , 'Do u want to save this costumer !' , 1 )

    # close the dialogue 
    def close_dialogue(self): 
        self.layoutSTACK.removeWidget(self.verticalWidget)
    
    # confirm adding new costumer
    def confirmAdding(self):
        # close the dialogue 
        self.layoutSTACK.removeWidget(self.verticalWidget)
        # get all informations about the costumer
        name = self.ui.line_name.text()
        phone_number = self.ui.line_phone.text()
        car_company = self.ui.line_carcompany.text()
        car_model= self.ui.line_carmodel.text()
        car_code = self.ui.line_carcode.text()
        notes = self.ui.line_notes.text()


        if Adduser.find_phone_number(self , phone_number) : 
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
                self.allcostumer.append(one_costumer)
                # save this in json file 
                a_file = open("database_costumers.json", "r")
                json_object = json.load(a_file)
                a_file.close()
                json_object['users'] = self.allcostumer
                a_file = open("database_costumers.json", "w")
                json.dump(json_object, a_file , indent= 4 )
                a_file.close()
                # clear edit lines 
                self.ui.line_name.setText('')
                self.ui.line_phone.setText('')
                self.ui.line_carcompany.setText('')
                self.ui.line_carmodel.setText('')
                self.ui.line_carcode.setText('')
                self.ui.line_notes.setText('')
                # upload the json file to firebase 
                Adduser.dialogue_message(self ,'Attention' , 'Costumer has been successfully added !' , 2 )
                # update the UI in the users page 
                Users.ShowAllCostumers(self , False)
                # update the UI in the Send message page 
                Sendsms.deepCopy(self)
                Sendsms.ShowAllCostumers(self , False)
            else: 
                Adduser.dialogue_message(self ,'Attention' , 'Please entre all the information about the costumer !' , 2 )
        else: 
            Adduser.dialogue_message(self ,'Attention' , 'This number has been alredy entred !' , 2 )
            self.ui.line_phone.setText('')
    

    def find_phone_number(self , phone_number):
        for index , costumer in enumerate(self.allcostumer):
            if costumer['phone_number'] == phone_number : 
                return False
        
        return True

        
    
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
            self.redbutton.clicked.connect(partial(Adduser.close_dialogue , self ))
            # 1 == conformation (yes or No ) , 2 == information (one button 'okay ')
            if statu == 1 : 
                self.greenbutton.clicked.connect(partial(Adduser.confirmAdding , self ))
            else : 
                self.greenbutton.hide()
                self.redbutton.setText('Okay')

    

    

            
       