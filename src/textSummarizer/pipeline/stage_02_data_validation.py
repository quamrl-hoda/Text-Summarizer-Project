from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataVaidation
from textSummarizer.logging import logger 

STAGE_NAME = "Data Validation Stage"
class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataVaidation(config=data_validation_config)
            validation_status = data_validation.validate_all_files()
            if validation_status:
                logger.info("All files are validated successfully.")
            else:
                logger.info("Data validation failed. Some files are missing or incorrect.")

        except Exception as e:
            logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
            raise e