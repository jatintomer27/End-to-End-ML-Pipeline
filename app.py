# It is my web application 

from ML_pipeline import logger
from ML_pipeline.pipeline.stage_01_data_ingestion import  DataIngestionTrainingPipeline
from ML_pipeline.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

# We have directly imported from the ML_pipeline 
# because we have aleady installed ML_pipeline as my local package in the setup.py file. (SRC_REPO)

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e