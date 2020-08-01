# -*- coding: utf-8 -*-
# --[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib, urlparse, base64
import xbmc, xbmcgui, xbmcplugin
from resources.lib.modules import client, log_utils
from resources.lib.modules import log_utils
from resources.lib.modules import control
from resources.lib.modules import cfscrape

sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])
artPath = control.artPath()
addonFanart = control.addonFanart()
addonThumb = control.addonThumb()


class sports24:
    def __init__(self):
        self.list = []
        self.base_link = 'http://sports24.club/tv/'
        self.headers = {'User-Agent': client.agent()}
        self.icon = 'https://github.com/Tempest0580/xml/blob/master/icons/channels.png?raw=true'
        self.scraper = cfscrape.create_scraper()

    def root(self):
        url = self.scraper.get(self.base_link, headers=self.headers).content
        url = re.findall('<a class="btn btn-outline-primary fxbtn" title="(.+?)" href="(.+?)">.+?</a>', url)
        for item in url:
            self.list.append({'name': item[0], 'url': self.base_link + item[1], 'image': self.icon, 'action': 'sports24Play'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            stream = self.scraper.get(url, headers=self.headers).content
            streams = re.findall('var xurl = atob\(\'(.+?)\'\)', stream)
            for link in streams:
                link = base64.b64decode(link)
                link = "https:" + link if not link.startswith('http') else link
                link = '%s|User-Agent=%s&Referer=%s' % (link, client.agent(), self.base_link)
                control.execute('PlayMedia(%s)' % link)
        except:
            return

    def addDirectory(self, items, queue=False, isFolder=True, sortMethod=xbmcplugin.SORT_METHOD_LABEL):
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
        control.sortMethod(syshandle, sortMethod)
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)
