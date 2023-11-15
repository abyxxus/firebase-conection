from firebase import firebase
from datetime import date

fb = firebase.FirebaseApplication("https://alcancia-hard-umb-default-rtdb.firebaseio.com/",None)

def put_data(data):
    global fb
    datos = {
		"time" : date.today(),
		"total": data
	}
    
    rt = fb.post('/alcancia',data)
    
put_data(128)