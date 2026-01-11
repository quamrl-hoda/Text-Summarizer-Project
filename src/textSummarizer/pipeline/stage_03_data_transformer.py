from textSummarizer.logging import logger
from textSummarizer.entity.config_entity import DataTransformationConfig
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformer import DataTransformation
from transformers import AutoTokenizer

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()