import requests
from auth import Auth
from utils.riot import is_valid_region


class Summoners:

    def __init__(self, puuid: str, region: str):
        self.puuid = puuid
        self.region = region.lower()
        self.__api_token = Auth.get_auth_token()

        is_valid_region(self.region)

    def fetch_summoner_by_puuid(self):
        """Fetch league summoner by PUUID."""
        url = f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{self.puuid}"
        headers = {"X-Riot-Token": self.__api_token}

        response = requests.get(url,headers=headers)
        response.raise_for_status()
        return response.json()