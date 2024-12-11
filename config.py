"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "27956216")
        self.API_HASH: str = os.environ.get("API_HASH", "7e79fca1cf1c9974dd623753fd5d2102")
        self.SESSION: str = os.environ.get("SESSION", "BQGqk_gAqQ8NCicSRJ40wIHI0gp_0gIdpGtHU3HIVsTF-NI4nz6td518qZqhDDE5pwm9QAIBRshfFuc3UjApnT5Hx80yle2ouTFASXO4uDMCWwsI1FdclekDf21D_-9wA_ex_uGXcbJriPF3-aGejTJPes0MwpbiVbDthhCpaMDJSjpnABH6y2sz8Sv-ldaB3f4itdvEteXA8rsOyh6lXzBoMbwqBjt68NPCPxgFZJim2NshdxvEOHKtsnUxAmVmGQgyJo1oCVrWFA_VzfYcV00KP1cLlVQjbpxABstg4Hex1Vwpnh1I0pm_zmzxheVsjBm5tJV98EKkVwOxYe-OJrcd1oCuOwAAAAHJJpY5AA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "7356074420:AAHnSu5Cx2r8CyJDY51Zo03g-1mi5Vtap0M")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "/").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", "27154e86e4e04c909ad65020dc190fef")
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", "97f9882ce54e47a49d27eab94d580075")


config = Config()
