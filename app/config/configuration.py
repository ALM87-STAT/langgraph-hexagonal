import json
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
import yaml
import os

from app.application.dto.agents_dto import Config


class ConfigLoader:

    def __init__(
        self,
        config_path: str | Path = "./assets/models.yml",
        config_server_path: str | Path = "./assets/mcp-servers-config.json",
    ):
        self.config_path = Path(config_path)
        self.config_server_path = Path(config_server_path)
        self.config = self._load_config()
        self.mcp_config = self._load_mcp_config()
        load_dotenv()

    def _load_mcp_config(self) -> Dict[str, Any]:
        if not self.config_server_path.exists():
            raise FileNotFoundError(
                f"MCP config file not found: {self.config_server_path}"
            )

        try:
            with open(self.config_server_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in MCP config: {e}", e.doc, e.pos)

    def _load_config(self) -> Config:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, "r") as f:
            config_dict = yaml.safe_load(f)

        # Resolve environment variables
        config_dict = self._resolve_env_vars(config_dict)

        # Validate and create config object
        return Config(**config_dict)

    def _resolve_env_vars(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively resolves environment variables in config values."""
        resolved_config = {}
        for key, value in config.items():
            if isinstance(value, dict):
                resolved_config[key] = self._resolve_env_vars(value)
            elif (
                isinstance(value, str)
                and value.startswith("${")
                and value.endswith("}")
            ):
                env_var = value[2:-1]
                resolved_config[key] = os.environ.get(env_var, value)
            else:
                resolved_config[key] = value
        return resolved_config

    @property
    def get_config(self) -> Config:
        return self.config

    @property
    def get_mcp_config(self) -> Dict[str, Any]:
        return self.mcp_config


# Usage example
if __name__ == "__main__":
    config_loader = ConfigLoader()
    config = config_loader.get_config
    print(f"Loaded configuration for environment: {config.environment}")
