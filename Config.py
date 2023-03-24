import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5"")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6051627585:AAEnN2aOouXMSmv2tJq71jvLFJrQUSI1X2s")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJ8Bu8ApTIa0MNCCMrIQ1-grHJa3u1tVSYmonJ1mUd8eGWwy_yrUl0Y2Ss5Xi9bCsq_ki-Wm11KXPzxKn8J3NH-gb4Q1ZGrTpkYof6woQvLoqZz7aKDLyrc5Avh3ZPoLqJvB9oNbH-MxhMf0YUC29pVoxJQEt5QTKf-tKPTGUo006zNoyVSj86cR0VFYU5kPllj0vyZH0BfOezHmL632nk2amByK8AT0tdaREegnTBvF5Z3MXx-I43CaXHeu0y3YuIFsV0hMOZga2A5MHcBr4_n2gBhyxVxhaXhKMQX9XM14lfg65nr-MwVtOjfBBZvLd5Vn8_2fe7-549zati2vCmLide0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
