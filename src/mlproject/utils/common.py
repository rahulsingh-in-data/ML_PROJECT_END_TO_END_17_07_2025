import os
from box.exceptions import BoxValueError
import yaml
from src.mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Dict, List, Union
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(file_path: str) -> ConfigBox:
    try:
        with open(file_path, "r") as file:
            content = yaml.safe_load(file)
            logger.info(f"Successfully read YAML file at {file_path}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Empty YAML structure in file: {file_path}")
    except Exception as e:
        logger.error(f"Error reading YAML file at {file_path}: {e}")
        raise e
    

def create_directories(paths: list, verbose: bool = True) -> None:
    """
    Creates directories for the given list of paths.

    Args:
        paths (list of Path): List of directory paths to create.
        verbose (bool): Whether to log and print the created paths.

    Returns:
        None
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")
            print(f"Directory created at: {path}")

@ensure_annotations
def save_json(file_path: str, data: dict) -> None:
    """
    Saves data to a JSON file.
    
    Args:
        file_path (str): Path to the JSON file.
        data (Any): Data to be saved.
    """
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
            logger.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving data to {file_path}: {e}")
        raise e
    
@ensure_annotations
def load_json(file_path: str) -> Any:
    """
    Loads data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file.
    
    Returns:
        Any: Data loaded from the JSON file.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            logger.info(f"Data successfully loaded from {file_path}")
            return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON from {file_path}: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        raise e
    
@ensure_annotations
def load_bin(path=str) -> Any:
    """
    Load a binary file using joblib.
    
    Args:
        path (str): Path to the binary file.
    
    Returns:
        Any: The loaded object.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded successfully from {path}")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        raise
    except Exception as e:
        logger.error(f"Error loading binary file from {path}: {e}")
        raise e
    
@ensure_annotations
def get_size(path: str) -> int:
    """
    Get the size of a file or directory.
    
    Args:
        path (str): Path to the file or directory.
    
    Returns:
        int: Size in bytes.
    """
    try:
        size = os.path.getsize(path)
        logger.info(f"Size of {path} is {size} bytes")
        return size
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        raise
    except Exception as e:
        logger.error(f"Error getting size of {path}: {e}")
        raise e
    

