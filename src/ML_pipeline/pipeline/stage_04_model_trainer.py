from ML_pipeline.config.configuration import ConfigurationManager
from ML_pipeline.components.model_trainer import ModelTrainer
from ML_pipeline import logger

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train()
        except Exception as e:
            logger.info(e)
            raise(e)