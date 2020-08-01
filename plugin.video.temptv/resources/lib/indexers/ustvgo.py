# -*- coding: utf-8 -*-
# --[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib, base64
import xbmc, xbmcgui, xbmcplugin
from resources.lib.modules import client
from resources.lib.modules import control


class ustvgo:
    def __init__(self):
        self.list = []
        self.base_link = 'https://ustvgo.tv'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}
        self.icon = 'https://github.com/Tempest0580/xml/blob/master/icons/channels.png?raw=true'

    def root(self):
        urls = ['https://ustvgo.tv/category/entertainment/',
                'https://ustvgo.tv/category/entertainment/page/2/',
                'https://ustvgo.tv/category/entertainment/page/3/',
                'https://ustvgo.tv/category/news/',
                'https://ustvgo.tv/category/sports/',
                'https://ustvgo.tv/category/kids/']
        for url in urls:
            url = client.request(url, headers =self.headers)
            url = re.findall('class="featured-image"> <a href="(.+?)" title="(.+?)"><img width=".+?" height=".+?" src=".+?" class=".+?" alt="" data-lazy-src="(.+?)" /><noscript><img width="269" height="151" src=".+?"', url)
            for item in url:
                self.list.append({'name': item[1].replace('#038;', ''), 'url': item[0], 'image': self.icon, 'action': 'ustvgoPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            link = client.request(url, headers=self.headers)
            link = re.compile("<iframe src='(.+?)'").findall(link)[0]
            link = '%s%s' % (self.base_link, link)
            link = client.request(link, headers=self.headers)
            link = re.compile("atob\('(.+?)'\);").findall(link)[0]
            link = base64.b64decode(link)
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
