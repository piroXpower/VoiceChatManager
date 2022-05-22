import os


class Config(object):
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    API_ID = int(os.environ.get("API_ID", ""))

    API_HASH = os.environ.get("API_HASH", "")

    LOG_CHAT = os.environ.get("CHAT", "international_hindi_chatting")
