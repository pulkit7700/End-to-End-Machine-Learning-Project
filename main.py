from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} has Started! <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} has Completed <<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} has Started! <<<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} has Completed <<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<< \n\n x=====================================x")
except Exception as e:
    logger.exception(e)

