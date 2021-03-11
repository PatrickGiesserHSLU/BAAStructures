from util import db_connection
from linear_regression.train import LinearRegressionTrain

class LinearRegression():

    def __init__(self):
        self.params = "LinearRegression Params"
        self.options = "LinearRegression Options"
        self.connection = db_connection.DBConnection()
        self.model = LinearRegressionTrain()

    def set_options(self, options):
        self.options = options

    def get_model(self):
        return self.model

    def get_params(self):
        return self.params


