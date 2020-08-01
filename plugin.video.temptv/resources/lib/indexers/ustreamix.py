# -*- coding: utf-8 -*-
# --[ From Tempest ]--

import re, os, sys, urllib, urlparse
import xbmc, xbmcgui, xbmcplugin
from resources.lib.modules import log_utils
from resources.lib.modules import control, client


class ustreamix:
    def __init__(self):
        self.list = []
        self.base_link = 'https://ustreamix.net'
        self.headers = {'User-Agent': client.agent()}
        self.icon = 'https://github.com/Tempest0580/xml/blob/master/icons/channels.png?raw=true'

    def root(self):
        url = 'https://ssl.ustreamix.com/index.html'
        url = client.request(url, headers=self.headers)
        url = re.findall('href="(.+?)" target="_blank">(.+?) <span', url)
        for item in url:
            self.list.append({'name': item[1], 'url': item[0], 'image': self.icon, 'action': 'ustreamixPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            from resources.lib.modules import client
            from resources.lib.modules import jsunpack
            from resources.lib.modules import log_utils
            unpacked = ''
            url_main = url
            url = client.request(url_main, headers=self.headers)
            url = re.compile('(eval\(function\(p,a,c,k,e,d\)\{.*)').findall(url)
            for url in url:
                if 'hls' in url and 'm3u8' in url:
                    uncode = jsunpack.unpack(url)
                    code = re.findall('host_tmg="(.+?)";var ustreamix_app=0;', uncode)[0]
                    code1 = re.findall('file_name="(.+?)";var', uncode)[0]
                    code2 = re.findall('jdtk="(.+?)";var', uncode)[0]
                    link = 'https://%s/%s?token=%s|User-Agent=%s&Referer=%s' % (code, code1, code2, client.agent(), url_main)
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
