# -*- coding: utf-8 -*-

import re
import time



def onServerInfo(server, info):
    if not info.isPlayer:
        return

    player = info.player
    command, blocktype, radius_s = parsed_info(info.content)
    radius = int(radius_s)

    if command != '!!platform':
        return

    if blocktype == '':
        blocktype = 'iron_block'

    if not blocktype.startswith('minecraft:'):
        blocktype += 'minecraft:'

    if radius <= 0 or radius > 255:
        server.tell(player, 'Error in radius input; default 5')
        radius = 5

    fillblock(server, player, blocktype, radius)


def parsed_info(content):
    c = content.decode('utf-8')
    tokens = c.split()
    length = len(tokens)

    command = tokens[0]
    blocktype = tokens[1] if length >= 2 else None
    edge = tokens[2] if length >= 3 else None
    return command, blocktype, edge


def fillblock(server, player, blocktype, radius):
    to_send = 'execute ' + player + ' fill ~-' + str(radius) + ' ~ ~-' + str(radius) + ' ~' + str(radius) + ' ~ ~' + str(radius) + ' ' + blocktype
    server.execute(to_send)
