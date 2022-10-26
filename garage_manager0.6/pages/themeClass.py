from PyQt5 import QtGui
from App import *
from functools import partial

class Theme(MainWindow):

    def inint_ui(self):
        # change the color of the icons into from black to #858585
        self.ui.adduser.setIcon(Theme.QIcon_from_svg(self , ':/image/essential/add-line.svg','#aef3e7'))
        self.ui.users.setIcon(Theme.QIcon_from_svg(self ,":/image/core/user-line.svg", '#858585'))
        self.ui.sendsms.setIcon(Theme.QIcon_from_svg(self ,":/image/social/email-line.svg", '#858585'))
        # titel 
        self.ui.appname.setText("Garage Manager")
        # color the icons of the first page 
        self.ui.icon_name.setIcon(Theme.QIcon_from_svg(self , ':/image/core/user-line.svg','#aef3e7'))
        self.ui.icon_phone.setIcon(Theme.QIcon_from_svg(self , ':/image/technology/mobile-phone-line.svg','#aef3e7'))
        self.ui.icon_company.setIcon(Theme.QIcon_from_svg(self , ':/image/commerce/bank-line.svg','#aef3e7'))
        self.ui.icon_model.setIcon(Theme.QIcon_from_svg(self , ':/image/essential/key-line.svg','#aef3e7'))
        self.ui.icon_code.setIcon(Theme.QIcon_from_svg(self , ':/image/technology/bar-code-line.svg','#aef3e7'))
        self.ui.icon_notes.setIcon(Theme.QIcon_from_svg(self , ':/image/essential/note-edit-line.svg','#aef3e7'))
        # color the icons of  the second page 
        self.ui.icon_search.setIcon(Theme.QIcon_from_svg(self , ':/image/core/search-line.svg','#aef3e7'))
        self.ui.icon_filter.setIcon(Theme.QIcon_from_svg(self , ':/image/core/filter-grid-circle-line.svg','#aef3e7'))
        # color the icons of the third page 
        self.ui.icon_search_2.setIcon(Theme.QIcon_from_svg(self , ':/image/core/search-line.svg','#aef3e7'))
        self.ui.icon_filter_2.setIcon(Theme.QIcon_from_svg(self , ':/image/core/filter-grid-circle-line.svg','#aef3e7'))
        self.ui.icon_message.setIcon(Theme.QIcon_from_svg(self , ':/image/social/chat-bubble-outline-badged.svg','#aef3e7'))

    def actionbutton(self):
        pass

    def openpage(self , button):
        # change the color of the icons into from black to #858585
        self.ui.adduser.setIcon(Theme.QIcon_from_svg(self , ':/image/essential/add-line.svg','#858585'))
        self.ui.users.setIcon(Theme.QIcon_from_svg(self ,":/image/core/user-line.svg", '#858585'))
        self.ui.sendsms.setIcon(Theme.QIcon_from_svg(self ,":/image/social/email-line.svg", '#858585'))
        
        # open the pages and make the pressed button with this color ===> #aef3e7
        if button.objectName() == 'adduser' :
            self.ui.LESPAGES.setCurrentIndex(0)
            self.ui.adduser.setIcon(Theme.QIcon_from_svg(self , ':/image/essential/add-line.svg' , "#aef3e7"))
            
        elif button.objectName() == 'users':
            self.ui.LESPAGES.setCurrentIndex(1) 
            self.ui.users.setIcon(Theme.QIcon_from_svg(self , ':/image/core/user-solid.svg' , '#aef3e7'))
            
        elif button.objectName() == 'sendsms' :
            self.ui.LESPAGES.setCurrentIndex(2) 
            self.ui.sendsms.setIcon(Theme.QIcon_from_svg(self , ':/image/social/email-solid.svg' , '#aef3e7'))
           

    def QIcon_from_svg(self , svg_filepath, color):
        img = QPixmap(svg_filepath)
        qp = QPainter(img)
        qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
        qp.fillRect( img.rect(), QColor(color) )
        qp.end()
        return QIcon(img)
    
    
   
    
    

  
        








