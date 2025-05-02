import requests
from utils.dot_env import validate_env_variable
from auth import Auth 

class Accounts:

    def __init__(self, game_name: str, tag_line: str):
        self.game_name = game_name
        self.tag_line = tag_line
        self.region_router = validate_env_variable("REGION_ROUTER")   
        self.__api_token = Auth.get_auth_token()
        self.puuid = self.__get_puuid()

    def __get_puuid(self) -> None:
        """Fetch the PUUID for the given game name and tag line."""
        url = f"{self.region_router}riot/account/v1/accounts/by-riot-id/{self.game_name}/{self.tag_line}"
        headers = {"X-Riot-Token": self.__api_token}

        response = requests.get(url,headers=headers)
        response.raise_for_status()
        
        data = response.json()
        puuid = data.get("puuid")

        if not puuid:
            raise ValueError("PUUID not found in the response.")
        
        return puuid