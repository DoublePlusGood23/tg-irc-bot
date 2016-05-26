#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
#    tg-irc-bot   A Bot to relay chat between Telegram and IRC.
#    Copyright (C) 2016  Ethan R. Jones
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import asyncio

import telepot
import telepot.async

class TgBot(telepot.async.Bot):
    """Telegram IRC Relay Bot"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._answerer = telepot.async.helper.Answerer(self)

    async def on_chat_message(self, msg):
        """Gets msg from telegram chat sends to an IRC"""
        content_type, chat_type, chat_id = telepot.glance(msg)
        print('Chat Message:', content_type, chat_type, chat_id)
        # TODO Change this to send IRC messages...
        msg = self.response(msg['text'])
        if msg is not None:
            await self.sendMessage(chat_id, msg)
        return

    def response(self, command):
        """Returns the proper response based on which command was said by the user"""
        if '/test' in command:
            return "Functioning Properly."
