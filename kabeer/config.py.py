class Config(object):
    API_HASH = os.getenv("API_HASH")
    API_ID = int(os.getenv("API_ID"))
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
