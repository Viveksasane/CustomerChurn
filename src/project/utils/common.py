import os
from box.exceptions import BoxValueError
import yaml
from src.project.logging import logger
import json
import pickle
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns
    
    Args:
        path_to_yaml (str) : path like input
    
    Raises :
        ValueError : if yaml file is empty
        e : empty file

    Returns :
        ConfigBox : ConfigBox type

    """
    try :
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"Yaml file :{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """Create list of directories
    Args :
          path_to_directories(list):list of path of directories
          ignore_log(bool,optional):ignore if multiple dirs is to be created.Defaults
    """
    for path in path_to_directories:
        os.makdirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at :{path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """Save json data
    Args:
     path(Path):path to json file
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at :{path}")


@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    """load json files data
    Args :
        path(Path):path to json file
        
    Returns: 
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content=json.load(f)
    
    logger.info(f"json file loaded successfully from :{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    with open(path, "wb") as f:
        pickle.dump(data, f)

    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the binary file.
    """
    with open(path, "rb") as f:
        content = pickle.load(f)

    logger.info(f"Binary file loaded from: {path}")

    return ConfigBox(content)