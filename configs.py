from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23685822"))
    API_HASH = getenv("API_HASH", "ff0572e13ff2f63a50f6dc707e0c4c9f")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "FilmyflixHD")
    CHID = int(getenv("CHID", "-1001648037641"))
    SUDO = list(map(int, getenv("6725874739 1018033649").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://priyanshukumawat90_db_user:HtZWFwZpyQgNmdtv@cluster0.gmchzjb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
