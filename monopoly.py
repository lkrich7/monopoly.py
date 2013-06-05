#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

class Player:
    name = None
    money = 1500
    postion = None
    def __unicode__(self) :
        return self.name
    def __str__(self) :
        return unicode(self)

class PropertyLand:
    house_num = 0
    owner = None

in_encoding = sys.stdin.encoding
players = []

while (True) :
    print u'输入参赛人数[2-4]:'
    try :
        player_num = int(raw_input().decode(in_encoding))
        break
    except :
        pass

for x in range(0, player_num) :
    print u"输入 %d 号玩家名字：" % x
    name = raw_input().decode(in_encoding)
    print type(name)
    player = Player()
    player.name = name
    print type(player.name)
    players.append(player)

while (True) :
    print u'开始游戏吗？[y/n]'
    isStart = raw_input()
    if isStart == 'y' or isStart == 'n' :
        break

print u'======================='
for a in players :
    print player

a = PropertyLand()
print a.house_num
