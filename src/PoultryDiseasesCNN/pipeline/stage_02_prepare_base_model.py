from src.PoultryDiseasesCNN.config.configuration import ConfigurationManager
from src.PoultryDiseasesCNN.components.prepare_base_model import PrepareBaseModel
from src.PoultryDiseasesCNN.Poultry_Logger import setup_logger
logger=setup_logger()

STAGE_NAME = "Prepare Base Model stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.prepare_base_model_config = self.config.get_prepare_base_model_config()
        self.prepare_base_model = PrepareBaseModel(config=self.prepare_base_model_config)

    def main(self):
        self.prepare_base_model.get_base_model()
        self.prepare_base_model.update_base_model()

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e