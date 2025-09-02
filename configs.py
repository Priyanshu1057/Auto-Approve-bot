from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23685822"))
    API_HASH = getenv("API_HASH", "ff0572e13ff2f63a50f6dc707e0c4c9f")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "FilmyflixHD")
    CHID = int(getenv("CHID", "-1001648037641"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
