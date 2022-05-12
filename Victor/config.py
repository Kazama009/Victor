class Config(object):
    LOGGER = True
    APP_ID = 12345 # Get from telegram.org
    API_HASH = "" # Get from telegram.org


class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True