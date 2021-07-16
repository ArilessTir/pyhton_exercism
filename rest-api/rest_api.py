class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        return self.database

    def post(self, url, payload=None):
        pass
