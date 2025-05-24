import firebase_admin
from datetime import datetime
from zoneinfo import ZoneInfo
from firebase_admin import db, credentials

_packed_data:list = []
_PACKET_LIMIT = 60 # Number of data points to collect before sending to Firebase

cred_obj = firebase_admin.credentials.Certificate("./env/sex.json")
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://bananadb-7cafe-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('test_data')

def read_data(temp, humidity):
    if len(_packed_data) == _PACKET_LIMIT:
        ref.push({
            f"{datetime.now().strftime('%H:%M:%S_%Y-%m-%d')}": _packed_data
        })
        _packed_data.clear()
        print("Data sent to Firebase and cleared from local storage.")
    else:
        _packed_data.append({
            'timestamp': datetime.now().strftime('%H:%M:%S_%Y-%m-%d'),
            'temperature': temp,
            'humidity': humidity
        })
    print(len(_packed_data), "data points collected.")