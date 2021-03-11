import config

class DBConnection:

    def __init__(self):
        self.host = config.DB_HOST
        self.user = config.DB_USER
        self.pw = config.DB_PW
        self.name = config.DB_NAME
        self.port = config.DB_PORT

        self.connection = "Connection"

    def connect(self):
        self.connection = "Connection"

    def disconnect(self):
        self.connection = None

    def query(self):
        pass