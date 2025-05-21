from os import environ 

class Config:
    API_ID = environ.get("API_ID", "22020431")
    API_HASH = environ.get("API_HASH", "0a47ec13eb6606a886779037b6417673")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8045686492:AAGVmn1ZgX3V5D7iCOBJYSJqUUvO9nGUmLo") 
    BOT_SESSION = environ.get("BOT_SESSION", "fwdv22") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://nguyenkhactam5:q1231234@superbot.vmvzlsu.mongodb.net/?retryWrites=true&w=majority&appName=SuperBot")
    DATABASE_NAME = environ.get("DATABASE_NAME", "nguyenkhactam5")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7312317360').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
