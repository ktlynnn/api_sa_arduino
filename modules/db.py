import firebase_admin

cred_obj = firebase_admin.credentials.Certificate("../env/sex.json")
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://bananadb-7cafe-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

