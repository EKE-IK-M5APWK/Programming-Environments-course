import datetime
import json


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.data = []
        self.load()

        def load():
            with open(filename) as json_file:
                data = json.load(json_file)
                return data

        def save(data):
            with open(self.file, 'w') as outfile:
                json.dump(self.data, outfile)

        def add(value):
            self.data.append(value)

        @staticmethod
        def get_date():
            return str(datetime.datetime.now()).split(" ")[0]
