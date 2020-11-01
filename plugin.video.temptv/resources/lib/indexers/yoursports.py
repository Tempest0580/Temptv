# -*- coding: utf-8 -*-
# --[ YourSports v1.0 ]--|--[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib, base64
import xbmc, xbmcgui, xbmcplugin
from resources.lib.modules import client
from resources.lib.modules import control


class yoursports:
    def __init__(self):
        self.list = []
        self.base_link = 'http://yoursports.stream'
        self.link = 'http://yoursports.stream/ing/'
        self.headers = {'User-Agent': client.agent()}
        self.icon = 'https://github.com/Tempest0580/xml/blob/master/icons/channels.png?raw=true'

    def root(self):
        urls = ['http://yoursports.stream/games.js?x=']
        for url in urls:
            url = client.request(url, headers =self.headers)
            url = url.split('scope.tv=[')[1]
            url = re.findall("chan:'(.+?)',url:'(.+?)'", url)
            url = [(i[0], self.link + i[1]) for i in url]
            for item in url:
                self.list.append({'name': item[0], 'url': item[1], 'image': self.icon, 'action': 'yoursportsPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            stream = client.request(url, headers=self.headers)
            link = re.compile("rbnhd = '(.+?)'").findall(stream)[0]
            link = base64.b64decode(link)
            if link.startswith('/'):
                link = self.base_link + link
            link = '%s|User-Agent=%s&Referer=%s' % (link, client.agent(), url)
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
