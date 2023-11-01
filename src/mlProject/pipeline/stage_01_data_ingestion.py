from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} has Started! <<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} has Completed <<<<<<<<<\n\nx===================x")
    except Exception as e:
        logger.exception(e)