import os
import ssl
from urllib.request import urlretrieve
import requests
import zipfile
from src.mlproject import logger
from src.mlproject.utils.common import get_size
from src.mlproject.entity.config_entity import DataIngestionConfig
from pathlib import Path

ssl._create_default_https_context = ssl._create_unverified_context


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config



    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_url, stream=True)
            if response.status_code == 200:
                with open(self.config.local_data_file, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                logger.info(f"Downloaded file: {self.config.local_data_file}")
            else:
                logger.error(f"Failed to download file: {self.config.source_url}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")


    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted files to {unzip_path}")

