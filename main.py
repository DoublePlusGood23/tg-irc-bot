#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
#    tg-irc-bot   A Bot to relay chat between Telegram and IRC.
#    Copyright (C) 2016  Ethan R. Jones
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import asyncio
import telepot
import telepot.async
import tg_bot

# get Telegram token from env var.
api_key = os.getenv('API_KEY')

irc_serv = os.getenv('IRC_SERV')



bot = tg_bot.TgBot(api_key)
loop = asyncio.get_event_loop()

loop.create_task(bot.message_loop())
print('Listening ...')

loop.run_forever()
