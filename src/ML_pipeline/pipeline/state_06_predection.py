import joblib
import numpy as np
import pandas as pd
from pathlib import Path

# To predect the quality of the wine from the user entered data

class PredectionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/data_trainer/model.joblib'))

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction

