from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 685446593  # my telegram ID
    OWNER_USERNAME = "fabricioo"  # my telegram username
    API_KEY = "730699562:AAFjF4ioNYf5PJaQX3fH_Iu-2MY4teNxuD0"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'https://vittarmodd.herokuapp.com/'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = False
    SUDO_USERS = [168975623, 685446593]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
