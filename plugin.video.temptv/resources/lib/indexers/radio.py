# -*- coding: utf-8 -*-
# -Created By Tempest

import re, os, sys, urllib
from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import cfscrape


class radio:
    def __init__(self):
        self.list = []
        self.base_link = 'http://streamwat.ch/radio'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}
        self.icon = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSykPFMcusbg1NRKDRFjMy4Drzd69L5eD6mpzJxg31xLj71L2Ed&usqp=CAU'
        self.scraper = cfscrape.create_scraper()

    def root(self):
        urls = [self.base_link]
        for url in urls:
            url = self.scraper.get(url, headers =self.headers).content
            url = re.findall('<li data-title="(.+?)" data-type="mp3" data-url="(.+?)"></li>', url)
            for item in url:
                self.list.append({'name': item[0], 'url': item[1], 'image': self.icon, 'action': 'radioPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            control.execute('ActivateWindow(busydialog)')
            control.execute('Dialog.Close(busydialog)')
            meta = {}
            for i in ['title', 'originaltitle', 'tvshowtitle', 'year', 'season', 'episode', 'genre', 'rating', 'votes', 'director', 'writer', 'plot', 'tagline']:
                try:
                    meta[i] = control.infoLabel('listitem.%s' % i)
                except:
                    pass
            meta = dict((k, v) for k, v in meta.iteritems() if not v == '')
            if 'title' not in meta:
                meta['title'] = control.infoLabel('listitem.label')
            icon = control.infoLabel('listitem.icon')
            self.name = meta['title']
            self.year = meta['year'] if 'year' in meta else '0'
            item = control.item(path=url, iconImage=icon, thumbnailImage=icon)
            item.setInfo(type='Video', infoLabels=control.metadataClean(meta))
            control.player.play(url, item)
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
