# -*- coding: utf-8 -*-
# --[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib, json, urlparse
import xbmc, xbmcgui, xbmcplugin
import js2py
from resources.lib.modules import log_utils
from resources.lib.modules import client
from resources.lib.modules import control


class ustvgo:
    def __init__(self):
        self.list = []
        self.base_link = 'https://ustvgo.tv'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}
        self.icon = 'https://github.com/Tempest0580/xml/blob/master/icons/channels.png?raw=true'
        addon_dir = control.addonPath #xbmc.translatePath('special://home/addons/plugin.video.tempest')
        self.ustv_chennel = os.path.join(addon_dir, "resources", "lib", "indexers", "ustvgo_new.json")

    def root(self):
        def get_dict_per_name(list_of_dict, key_value):
            for item in list_of_dict:
                if item['name'] == key_value:
                    my_item = item
                    list_of_dict.remove(item)
                    break
            else:
                my_item = None
            return list_of_dict, my_item
        with open(self.ustv_chennel) as f:
            list_of_dict = json.load(f)
        urls = [self.base_link]
        for url in urls:
            url = client.request(url, headers=self.headers)
            url = client.parseDOM(url, 'div', attrs={'class': 'entry-content clearfix'})
            for url in url:
                url = re.findall('><a href="(.+?)">(.+?)</a>', url)
                for item in url:
                    ch_name = item[1].replace('</strong>', '').replace('<strong>', '').replace('#038;', '').replace('&amp;', '&').replace('Animal', 'Animal Planet').replace('CW', 'The CW').strip()
                    list_of_dict, ch_dict = get_dict_per_name(list_of_dict, ch_name)
                    if ch_dict:
                        ch_dict.update({'url': item[0]})
                        self.list.append(ch_dict)
                    else:
                        self.list.append({'name': ch_name, 'url': item[0], 'image': self.icon, 'action': 'ustvgoPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            link = client.request(url, headers=self.headers)
            link = str([i for i in re.findall("<iframe src='(.+?)'", link)][0].split("'")[0])
            if link.startswith('/'):
                link = urlparse.urljoin(self.base_link, link)
            log_utils.log('---2EMBED Testing - Exception: \n' + str(link))
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

