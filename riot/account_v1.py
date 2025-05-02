import requests
import os
import utils.dot_env
from auth import Auth 

class Account:

    def __init__(self, game_name: str, tag_line: str):
        self.game_name = game_name
        self.tag_line = tag_line
        self.__region_router = os.getenv("REGION_ROUTER")
        self.__api_token = Auth.get_auth_token()
        self.puuid = self.__get_puuid()

    def __get_puuid(self) -> None:
        request = requests.get(
            url=f"{self.__region_router}riot/account/v1/accounts/by-riot-id/{self.game_name}/{self.tag_line}",
            headers={"X-Riot-Token": self.__api_token}
        )
        request = request.json()
        return request.get("puuid")