from ML_pipeline.config.configuration import ConfigurationManager
from ML_pipeline.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config = model_evaluation_config)
            model_evaluation_config.save_results()
        except Exception as e:
            raise e