from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Data Ingestion Configuration Data Class."""
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """Data Validation Configuration Data Class."""
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

