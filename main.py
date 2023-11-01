from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} has Started! <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} has Completed <<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)


