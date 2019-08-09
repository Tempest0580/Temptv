# -*- coding: utf-8 -*-
# --[ USTVgo v1.0 ]--|--[ From JewBMX ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib
from resources.lib.modules import client
from resources.lib.modules import control


class ustvgo:
    def __init__(self):
        self.list = []
        self.base_main_link = 'http://ustvgo.tv/%s'
        self.base_icon_link = 'https://github.com/jewbmx/xml/blob/master/img/ustvgo.jpg?raw=true'

    def root(self):
        channels = [
            ('abc-live-streaming-free'),
            ('ae-networks-live-streaming-free'),
            ('amc-live'),
            ('animal-planet-live'),
            ('bbc-america-live'),
            ('bet'),
            ('boomerang'),
            ('bravo-channel-live-free'),
            ('cartoon-network-live-streaming-free'),
            ('cbs-live-streaming-free'),
            ('cmt'),
            ('cnbc-live-streaming-free'),
            ('cnn-live-streaming-free'),
            ('comedy-central-live-free'),
            ('destination-america'),
            ('discovery-channel-live'),
            ('disney-channel-live-streaming-free'),
            ('disneyjr'),
            ('disneyxd'),
            ('diy'),
            ('e'),
            ('espn2'),
            ('espn-live'),
            ('food-network-live-free'),
            ('fox-business-live-streaming-free'),
            ('fox-hd-live-streaming'),
            ('fox-news-live-streaming-free'),
            ('fox-sports-1'),
            ('fox-sports-2'),
            ('freeform-channel-live-free'),
            ('fx-channel-live'),
            ('fxm'),
            ('fxx'),
            ('golf-channel-live-free'),
            ('gsn'),
            ('hallmark-channel-live-streaming-free'),
            ('hallmark-movies-mysteries-live-streaming-free'),
            ('hbo'),
            ('hgtv-live-streaming-free'),
            ('history-channel-live'),
            ('hln'),
            ('investigation-discovery-live-streaming-free'),
            ('lifetime-channel-live'),
            ('lifetime-movies'),
            ('mlb-network'),
            ('motortrend'),
            ('msnbc-live-streaming-free'),
            ('mtv'),
            ('nat-geo-wild-live'),
            ('national-geographic-live'),
            ('nba-tv'),
            ('nbc-sports'),
            ('nbc'),
            ('nfl-network-live-free'),
            ('nickelodeon-live-streaming-free'),
            ('nicktoons'),
            ('own'),
            ('oxygen'),
            ('paramount-network'),
            ('pbs-live'),
            ('pop'),
            ('science'),
            ('showtime'),
            ('starz-channel-live'),
            ('sundance-tv'),
            ('syfy-channel-live'),
            ('tbs-channel-live-free'),
            ('tcm'),
            ('telemundo'),
            ('tennis-channel-live-free'),
            ('the-cw-live-streaming-free'),
            ('the-weather-channel-live-streaming-free'),
            ('tlc-live-free'),
            ('tnt'),
            ('travel-channel-live-free'),
            ('trutv'),
            ('tv-land-live-free'),
            ('univision'),
            ('usa-network-live'),
            ('vh1'),
            ('we-tv')
        ]
        for channel in channels:
            cleanChannel = channel.replace('-streaming', '').replace('-live', '').replace('-free', '')
            cleanChannel = cleanChannel.upper().replace('-', ' ')
            self.list.append({'name': cleanChannel, 'url': self.base_main_link % channel, 'image': self.base_icon_link, 'action': 'ustvgoPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url, title, icon):
        try:
            html = client.request(url)
            stream = re.compile("file: '(.+?)',", re.DOTALL).findall(html)[0]
            url = stream
            control.execute('PlayMedia(%s)' % url)
        except Exception:
            return

    def addDirectory(self, items, queue=False, isFolder=True):
        if items is None or len(items) is 0:
            control.idle()
            sys.exit()
        sysaddon = sys.argv[0]
        syshandle = int(sys.argv[1])
        addonFanart, addonThumb, artPath = control.addonFanart(), control.addonThumb(), control.artPath()
        for i in items:
            try:
                name = i['name']
                if i['image'].startswith('http'):
                    thumb = i['image']
                elif artPath is not None:
                    thumb = os.path.join(artPath, i['image'])
                else:
                    thumb = addonThumb
                item = control.item(label=name)
                if isFolder:
                    url = '%s?action=%s' % (sysaddon, i['action'])
                    try:
                        url += '&url=%s' % urllib.quote_plus(i['url'])
                    except Exception:
                        pass
                    item.setProperty('IsPlayable', 'false')
                else:
                    url = '%s?action=%s' % (sysaddon, i['action'])
                    try:
                        url += '&url=%s' % i['url']
                    except Exception:
                        pass
                    item.setProperty('IsPlayable', 'true')
                    item.setInfo("mediatype", "video")
                    item.setInfo("audio", '')
                item.setArt({'icon': thumb, 'thumb': thumb})
                if addonFanart is not None:
                    item.setProperty('Fanart_Image', addonFanart)
                control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)
            except Exception:
                pass
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)
