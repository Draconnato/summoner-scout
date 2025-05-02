import utils.dot_env
import os

class Auth:

    def get_auth_token() -> str:
        return os.getenv("API_KEY")
