import os
from src.mlproject import logger
from src.mlproject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # Read the dataset
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = data.columns.tolist()

            # Extract expected schema columns from config
            expected_cols = list(self.config.all_schema["COLUMNS"].keys())

            # Validation: Are all expected columns present?
            missing_cols = [col for col in expected_cols if col not in all_cols]
            extra_cols = [col for col in all_cols if col not in expected_cols]

            validation_status = len(missing_cols) == 0 and len(extra_cols) == 0

            # Log details
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validation_status}\n")
                if missing_cols:
                    f.write(f"Missing Columns: {missing_cols}\n")
                if extra_cols:
                    f.write(f"Unexpected Columns: {extra_cols}\n")

            return validation_status
    
        except Exception as e:
            logger.exception(f"Exception occurred during data validation: {e}")
            raise e
