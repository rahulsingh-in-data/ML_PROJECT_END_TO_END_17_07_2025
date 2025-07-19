from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_validation import DataValidation
from src.mlproject import logger


STAGE_NAME = "02_data_validation"
class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        print("Config keys:", config.config.keys())  # Debug: print config keys
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<") 
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e 