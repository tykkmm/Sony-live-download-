import os

class Config(object):

    #TELEGRAM STUFF
    APP_ID = int(os.environ.get("29426486", ""))
    API_HASH = os.environ.get("d71ad4ec048ab41677a1a439b21ff0c9", "")
    BOT_TOKEN = os.environ.get("7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To", "")
