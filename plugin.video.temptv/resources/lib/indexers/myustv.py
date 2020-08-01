# -*- coding: utf-8 -*-
# -Created By Tempest

import re, os, sys, urllib, base64
import xbmc, xbmcgui, xbmcplugin
from resources.lib.modules import client
from resources.lib.modules import control


class myustv:
    def __init__(self):
        self.list = []
        self.base_link = 'http://myustv.com'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}

    def root(self):
        urls = ['http://myustv.com//watch/category/united-states-usa-tv-channel',
                'http://myustv.com/watch/category/united-states-usa-tv-channel/page/2/',
                'http://myustv.com/watch/category/united-states-usa-tv-channel/page/3/',
                'http://myustv.com/watch/category/united-states-usa-tv-channel/page/4/',
                'http://myustv.com/watch/category/united-states-usa-tv-channel/page/5/',
                'http://myustv.com/watch/category/united-states-usa-tv-channel/page/6/',
                'http://myustv.com/watch/category/soccer-streams/']
        for url in urls:
            url = client.request(url, headers =self.headers)
            url = re.findall('<div class="td_module_1 td_module_wrap td-animation-stack">\s+<div class="td-module-image">\s+<div class="td-module-thumb"><a href="(.+?)" rel="bookmark" class="td-image-wrap" title="(.+?)"><img .+? src="(.+?)"', url)
            for item in url:
                self.list.append({'name': item[1].replace('#038;', ''), 'url': item[0], 'image': item[2], 'action': 'myustvPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            stream = client.request(url, headers=self.headers)
            stream = re.compile('var link= atob\("(.+?)"\);').findall(stream)[0]
            link = base64.b64decode(stream)
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
