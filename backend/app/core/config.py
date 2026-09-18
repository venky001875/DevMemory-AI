import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application configuration settings.

    You can extend this class with environment variables or defaults as needed.
    """
    app_name: str = "DevMemory AI Backend"
    version: str = "0.1.0"
    # Add more configuration variables here

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
        env_file_encoding = "utf-8"

# Export a single Settings instance for easy import throughout the project
settings = Settings()
