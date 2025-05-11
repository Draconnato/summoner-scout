import requests
from auth import Auth
from utils.dot_env import validate_env_variable
from utils.riot import is_valid_region

class Entries:

    def __init__(self, puuid: str, region: str):
        self.puuid = puuid
        self.region = region.lower()
        self.__api_token = Auth.get_auth_token()

        is_valid_region(self.region)
        self.data = self.fetch_entry_by_puuid()

    def fetch_entry_by_puuid(self) -> list:
        """Fetch league entries by PUUID."""
        url = f"https://{self.region}.api.riotgames.com/lol/league/v4/entries/by-puuid/{self.puuid}"
        headers = {"X-Riot-Token": self.__api_token}

        response = requests.get(url,headers=headers)
        response.raise_for_status()
        return response.json()