from ml_verfahren.linear_regression import LinearRegression
from sanelib import Sanelib

linreg = Sanelib(LinearRegression())
linreg.train()
linreg.predict()
linreg.score()