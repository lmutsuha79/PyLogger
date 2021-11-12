import pyrebase

confige = {
    "dataBaseURL": "https://pyloger-3295c-default-rtdb.firebaseio.com/",
    "apiKey": "AIzaSyD-duv4tfPZPSpVauI1vO7IT-ktDNwEnbM",
    "authDomain": "pyloger-3295c.firebaseapp.com",
    "projectId": "pyloger-3295c",
    "storageBucket": "pyloger-3295c.appspot.com",
    "messagingSenderId": "460935053967",
    "appId": "1:460935053967:web:1c90085505cb8bdaf126fa",
    "measurementId": "G-42BKXTZD3J"
}

fireBase = pyrebase.initalize_app(confige)
dataBase = fireBase.database()

data = {
    "age": 19,
    "name": "yasser",
    "isALive": True,
}
dataBase.push(data)