# -*- coding: utf-8 -*-
# --[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib, base64
import xbmc, xbmcgui, xbmcplugin
import js2py
from resources.lib.modules import client
from resources.lib.modules import control


class ustvgo:
    def __init__(self):
        self.list = []
        self.base_link = 'https://ustvgo.tv'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}
        self.icon = 'https://github.com/Tempest0580/xml/blob/master/icons/channels.png?raw=true'

    def root(self):
        urls = [self.base_link]
        for url in urls:
            url = client.request(url, headers =self.headers)
            url = re.findall('<li><strong><a href="(.+?)">(.+?)</a>', url)
            for item in url:
                self.list.append({'name': item[1].replace('#038;', ''), 'url': item[0], 'image': self.icon, 'action': 'ustvgoPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            link = client.request(url, headers=self.headers)
            link = str([i for i in re.findall("<iframe src='(.+?)'", link)][0].split("'")[0])
            link = client.request(link, headers=self.headers)
            try:
                code = link[link.find("encrypted"):]
                code = code[:code.find("</script>")]
                file_code = re.findall(r"file.+", code)[0]
                file_code = "var link = " + file_code[file_code.find(":") + 1: file_code.find(",")]
                code = code[:code.find("var player")]
                code = code + file_code
                crypto_min = self.base_link + "/Crypto/crypto.min.js"
                addional_code = client.request(crypto_min, headers=self.headers)
                code = addional_code + code
                context = js2py.EvalJs(enable_require=True)
                link = context.eval(code)
                link = link.replace("\r", "").replace("\n", "")
                link = '%s|User-Agent=%s&Referer=%s' % (link, client.agent(), self.base_link)
                control.execute('PlayMedia(%s)' % link)
            except:
                import xbmcgui
                dialog = xbmcgui.Dialog()
                dialog.notification('VPN', 'VPN Locked Or The Code Has Changed', xbmcgui.NOTIFICATION_INFO, 5000)
                return
        except Exception as e:
            xbmc.log(str(e), level=xbmc.LOGNOTICE)
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
