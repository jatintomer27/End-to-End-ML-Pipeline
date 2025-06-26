# It is my endpoint 

from ML_pipeline import logger
from ML_pipeline.pipeline.stage_01_data_ingestion import  DataIngestionTrainingPipeline
from ML_pipeline.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from ML_pipeline.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from ML_pipeline.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from ML_pipeline.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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

STAGE_NAME = "Model Transformation Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
except Exception as e:
    logger.exception(e)
    raise e