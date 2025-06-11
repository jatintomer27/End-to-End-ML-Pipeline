from dataclasses import dataclass
from pathlib import Path

# This is called entity and this is the return type of the configuration function.

@dataclass(frozen=True) # Why we are using data class and will it do.
class DataIngestionConfig:
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