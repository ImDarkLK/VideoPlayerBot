"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

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
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "3047095"))
API_HASH = getenv("API_HASH", "994ffa4835a9c6fb1d697bdf283addbc")
BOT_TOKEN = getenv("BOT_TOKEN", "1921906120:AAHFBRG_ng0m7C8BA_eQ0JIeoafHnJsTbZA")
SESSION_STRING = getenv("SESSION_STRING", "BQABYNENwi2ffvuXs4crVQOX0Nk2JpYi_a1vGC8Gh0p0qV_AW0_tw8_Is1swz0cA53A_sLSVva1QJyVLUN2nDC_dSY1nU1Zy_OB0RZQBJWl56UcO-y1NyRp7PNqLDk-w7976r6z9CaoknGjv64bra6nthEYGJxoK2eymlBPGMeqcrCckoXOoBDdavQkhm0JlC0ju93h2hFXA6n07so_0L83pAYdhNCLP4gXBULCl_94tnwZ9qs8xvrc-ZdziIuM2QxcEJ515cTWl877qzoX73hVbearQL6ZxFFPs9rshCeu_snKdbd9EnznoZpuYnpxW1yVsWoDXNyrgN6pTFyMB52-GasWa_AA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ehi_podda_giveaways_chat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ehi_podda_official)
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LKMusicAssist)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "Hi උද්දික, Whats හැපනින් ?")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
