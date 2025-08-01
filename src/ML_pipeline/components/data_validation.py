from ML_pipeline.entity.config_entity import DataValidationConfig
from ML_pipeline import logger
import pandas as pd

# Update the Component

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)
            all_schema = self.config.all_schema.keys()
            for column in all_columns:
                if column not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            logger(e)
            raise e
