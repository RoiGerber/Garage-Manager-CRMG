from os import get_terminal_size
from firebase import Firebase


firebaseConfig ={
    
}

firebase = Firebase(firebaseConfig)


def addrecord(allcostumers):
    db = firebase.database()
    try:
        db.child("users").set(allcostumers)
        return None
    except Exception as e : 
        return None

def get_one_record():
    db = firebase.database()
    try:
        allcostumers = db.child("users").get().val()
        return allcostumers
    except Exception as e : 
        return None



