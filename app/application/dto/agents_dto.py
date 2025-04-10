from pydantic import BaseModel
from typing import Dict, Any


class ApplicationConfig(BaseModel):
    parameters: Dict[str, Any]


class ModelsConfig(BaseModel):
    application_1: ApplicationConfig
    application_2: ApplicationConfig


class Config(BaseModel):
    models: ModelsConfig
