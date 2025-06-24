import os
import pandas as pd
from ML_pipeline.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import joblib


class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column],axis=1)
        train_y = train_data[[self.config.target_column]]

        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]

        el = ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio,random_state=1)
        el.fit(train_x,train_y)

        joblib.dump(el, os.path.join(self.config.root_dir,self.config.model_name))