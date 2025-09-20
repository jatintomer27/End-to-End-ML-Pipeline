from dataclasses import dataclass
from pathlib import Path

# This is called entity and this is the return type of the configuration function.

"""
@dataclass automatically generates __init__, __repr__, __eq__, and other boilerplate 
for you based on the class attributes. This makes config objects concise and readable.
"""

"""
The frozen=True argument makes instances immutable — after creation you cannot assign to their fields 
(attempting to do so raises FrozenInstanceError).
"""

@dataclass(frozen=True) 
class DataIngestionConfig:
    """
    Declares the class that holds configuration 
    values for the data ingestion step.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio : float
    target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str