from utils.dot_env import validate_env_variable

class Auth:

    def get_auth_token() -> str:
        return validate_env_variable("API_KEY")