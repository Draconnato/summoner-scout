from dotenv import load_dotenv
import os

load_dotenv()

def validate_env_variable(var_name: str) -> str:
    """Validate that an environment variable is set and return its value."""
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"{var_name} environment variable is not set.")
    return value