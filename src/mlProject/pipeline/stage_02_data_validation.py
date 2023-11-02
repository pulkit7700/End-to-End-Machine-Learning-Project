from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValiadtion
from mlProject import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} started! <<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f" >>>>>>>>>>> Stage {STAGE_NAME} Completed! <<<<<<< \n\n x=======================================x")
    except Exception as e:
        raise e