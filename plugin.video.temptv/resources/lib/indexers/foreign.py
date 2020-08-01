# -*- coding: utf-8 -*-
# --[ From Tempest ]--

import re, os, sys, urllib, urlparse, requests
from resources.lib.modules import client
from resources.lib.modules import log_utils
from resources.lib.modules import control


class foreign:
    def __init__(self):
        self.list = []
        self.base_link = 'https://github.com/iptv-org/iptv'
        self.headers = {'User-Agent': client.agent()}

    def root(self):
        url = requests.get(self.base_link, headers=self.headers).content
        url = re.findall('alias=".+?" fallback-src="(.+?)".+?>\xc2\xa0(.+?)</td><td align="right">.+?</td><td align="left" '
                 'nowrap=""><code>(.+?)</code></td><td align="left">', url)
        for link in url:
            self.list.append({'name': link[1], 'url': link[2], 'image': link[0], 'action': 'foreignNext'})
        self.addDirectory(self.list)
        return self.list

    def roots(self, url):
        url = requests.get(url, headers=self.headers).content
        url = re.compile('#.+? tvg-logo="(.+?)" .+?",(.+?)\n(.+?)\n', re.MULTILINE|re.DOTALL).findall(url)
        for link in url:
            self.list.append({'name': link[1], 'url': link[2], 'image': link[0], 'action': 'foreignPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            control.execute('PlayMedia(%s)' % url)
        except:
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

