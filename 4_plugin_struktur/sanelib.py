
class Sanelib():
    def __init__(self, verfahren):
        self.verfahren = verfahren

    def train(self):
        self.verfahren.train()

    def predict(self):
        self.verfahren.predict()

    def score(self):
        self.verfahren.score()
