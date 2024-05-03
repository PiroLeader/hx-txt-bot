import re, os, time
import datetime

class Config:
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '6807993246:AAFJF86XfZEoiBGXS1SOD0GBhpNo3EgBUVY')
    API_HASH = os.environ.get('API_HASH', '2034b81303744d1dd2c7ffc02e21cfe2')
    API_ID = int(os.environ.get('API_ID', '18429621'))
    OWNER_ID = int(os.environ.get('OWNER_ID', '5486913681')) #Admin UserId
    DB_URI = os.environ.get('DB_URI') #May Be In Future.
    
