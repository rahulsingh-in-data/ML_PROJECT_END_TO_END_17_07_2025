from src.mlproject.constants import *
from src.mlproject.utils.common import read_yaml, create_directories, save_json
from src.mlproject import logger
from src.mlproject.entity.config_entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH):

        self.config = read_yaml(str(config_file_path))
        self.params = read_yaml(str(params_file_path))
        self.schema = read_yaml(str(schema_file_path))

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        """Returns Data Ingestion Configuration."""

        config = self.config.data_ingestion

        create_directories([config.root_dir, config.unzip_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=config.source_url,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema

        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )
        
        return data_validation_config


