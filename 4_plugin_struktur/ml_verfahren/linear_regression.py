from util import db_connection

class LinearRegression():

    def __init__(self):
        self.params = "LinearRegression Params"
        self.options = "LinearRegression Options"
        self.connection = db_connection.DBConnection()

    def set_options(self, options):
        self.options = options

    def train(self):
        print("LinearRegression Train")

    def predict(self):
        print("LinearRegression Predict")

    def get_params(self):
        return self.params

    def score(self):
        print("LinearRegression Score")