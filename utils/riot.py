from utils.dot_env import validate_env_variable

def is_valid_region(region: str) -> bool:
    """Validate if the provided region is valid."""
    available_regions = {value.lower() for value in validate_env_variable("REGIONS").split(",")}
    if region.lower() not in available_regions:
        raise ValueError(f"Region {region} not valid.")
    return True