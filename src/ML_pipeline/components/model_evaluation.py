import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from ML_pipeline.config.configuration import ModelEvaluationConfig
from ML_pipeline.utils.common import save_json
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_absolute_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]

        predicted_qualities = model.predict(test_x)

        rmse, mae, r2 = self.eval_metrics(test_y,predicted_qualities)

        # Saving the metrics as local

        scores = {'rmse':rmse, 'mae':mae, 'r2':r2}
        save_json(path = Path(self.config.metric_file_name), data=scores)