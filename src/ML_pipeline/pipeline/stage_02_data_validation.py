from ML_pipeline.config.configuration import ConfigurationManager
from ML_pipeline.entity.config_entity import DataValidationConfig
from ML_pipeline.components.data_validation import DataValidation
from ML_pipeline import logger

# Create the pipeline

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config(DataValidationConfig)
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            logger.info(e)
            raise e