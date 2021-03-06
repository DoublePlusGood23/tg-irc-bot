#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# ircecho.py
# Copyright (C) 2011 : Robert L Szkutak II - http://robertszkutak.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import sys
import socket
import string

class IrcBot():

    # connection config
    host = "localhost"
    port = 6667
    chan = "#bot"

    # user config
    nick = "tib"
    ident = "TgIrcBot"
    realname = "Telegram <-> IRC Bot"
    master = "dpg"

    readbuffer = ""

    s=socket.socket( )
    s.connect((host, port))

    s.send(bytes("NICK " + nick + "\r\n", "UTF-8"))
    s.send(bytes("USER "+ ident + " " + host + " bla :" + realname + "\r\n", "UTF-8"))
    s.send(bytes("JOIN " + chan + "\r\n", "UTF-8"));
    s.send(bytes("PRIVMSG " + master +" :Hello Master\r\n", "UTF-8"))

    while 1:
        readbuffer = readbuffer+s.recv(1024).decode("UTF-8")
        temp = str.split(readbuffer, "\n")
        readbuffer=temp.pop( )

        for line in temp:
            line = str.rstrip(line)
            line = str.split(line)

            if(line[0] == "PING"):
                s.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
            if(line[1] == "PRIVMSG"):
                sender = ""
                for char in line[0]:
                    if(char == "!"):
                        break
                    if(char != ":"):
                        sender += char
                size = len(line)
                i = 3
                message = ""
                while(i < size):
                    message += line[i] + " "
                    i = i + 1
                message.lstrip(":")
                s.send(bytes("PRIVMSG %s %s \r\n" % (sender, message), "UTF-8"))
        for index, i in enumerate(line):
            print(line)
