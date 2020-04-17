# -*- coding: utf-8 -*-
# --[ Tempest ]--

import re, os, sys, urllib
from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import cfscrape


class zynetv:
    def __init__(self):
        self.list = []
        self.base_link = 'https://zynetv.net'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}

    def root(self):
        channels = [
            ('5 Star', 'https://zynetv.net/onefilm/5star.m3u8', 'https://zynetv.net/wp-content/uploads/5star.png'),
            ('5 Usa', 'https://zynetv.net/onefilm/5usa.m3u8', 'https://zynetv.net/wp-content/uploads/5usa.png'),
            ('ABC 5', 'https://zynetv.net/fastlink/abc.m3u8', 'https://wcvbcreative.com/2014logos/WCVB_v.jpg'),
            ('ABC', 'https://zynetv.net/wiz0x50xcler/abc.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ABC.png?raw=true'),
            ('A&E', 'https://zynetv.net/wiz0x50xcler/ae.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/A&E.png?raw=true'),
            ('AMC', 'https://zynetv.net/wiz0x50xcler/amc.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/AMC.png?raw=true'),
            ('Animal Planet', 'https://zynetv.net/wiz0x50xcler/ap.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Animalplanet.png?raw=true'),
            ('BBC America', 'https://zynetv.net/wiz0x50xcler/bbcam.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/BBC%20America.png?raw=true'),
            ('BBC Four', 'https://zynetv.net/onefilm/bbc4.m3u8', 'https://zynetv.net/wp-content/uploads/bbc4.png'),
            ('BBC One', 'https://zynetv.net/onefilm/bbc1.m3u8', 'https://zynetv.net/wp-content/uploads/bbc1.png'),
            ('BBC Two', 'https://zynetv.net/onefilm/bbc2.m3u8', 'https://zynetv.net/wp-content/uploads/bbc2.png'),
            ('BET', 'https://zynetv.net/wiz0x50xcler/bet.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bet.png?raw=true'),
            ('Boomerang', 'https://zynetv.net/wiz0x50xcler/boomerang.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Boomerang.png?raw=true'),
            ('Bravo', 'https://zynetv.net/wiz0x50xcler/bravo.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bravo.png?raw=true'),
            ('Cartoon Network', 'https://zynetv.net/wiz0x50xcler/cn.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Cartoon%20Network.png?raw=true'),
            ('CBS', 'https://zynetv.net/wiz0x50xcler/cbs.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CBS.png?raw=true'),
            ('CBS Drama', 'https://zynetv.net/onefilm/cbsdrama.m3u8', 'https://zynetv.net/wp-content/uploads/cbs-drama.png'),
            ('CMT', 'https://zynetv.net/wiz0x50xcler/cmt.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CMT%20Films.png?raw=true'),
            ('CNBC', 'https://zynetv.net/wiz0x50xcler/cnbc.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNBC.png?raw=true'),
            ('CNN', 'https://zynetv.net/wiz0x50xcler/cnn.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNN.png?raw=true'),
            ('Comedy Central', 'https://zynetv.net/wiz0x50xcler/cc.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Comedy%20Central.png?raw=true'),
            ('Destination America', 'https://zynetv.net/wiz0x50xcler/desam.phtml', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Destination_America_logo.svg/400px-Destination_America_logo.svg.png'),
            ('Discovery Channel', 'https://zynetv.net/wiz0x50xcler/dc.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Discovery%20Channel.png?raw=true'),
            ('Disney Channel', 'https://zynetv.net/wiz0x50xcler/disney.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20Channel.png?raw=true'),
            ('Disney Jr', 'https://zynetv.net/wiz0x50xcler/disneyjr.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20Junior.png?raw=true'),
            ('Disney XD', 'https://zynetv.net/wiz0x50xcler/disney-xd.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20XD.png?raw=true'),
            ('DIY', 'https://zynetv.net/wiz0x50xcler/diy.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/DIY.png?raw=true'),
            ('E!', 'https://zynetv.net/wiz0x50xcler/e.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/E!.png?raw=true'),
            ('ESPN', 'https://zynetv.net/wiz0x50xcler/espn.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('ESPN 2', 'https://zynetv.net/wiz0x50xcler/espn2.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('Food Network', 'https://zynetv.net/wiz0x50xcler/foodnet.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Food%20Network.png?raw=true'),
            ('Fox', 'https://zynetv.net/wiz0x50xcler/fox.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FOX.png?raw=true'),
            ('Fox Business', 'https://zynetv.net/wiz0x50xcler/fbn.phtml', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Fox_Business.svg/420px-Fox_Business.svg.png'),
            ('Fox News', 'https://zynetv.net/wiz0x50xcler/foxnews.phtml', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/300px-Fox_News_Channel_logo.svg.png'),
            ('Fox Sports 1', 'https://zynetv.net/wiz0x50xcler/fs1.phtml', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/2015_Fox_Sports_1_logo.svg/400px-2015_Fox_Sports_1_logo.svg.png'),
            ('Fox Sports 2', 'https://zynetv.net/wiz0x50xcler/fs2.phtml', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/FS2_logo_2015.svg/400px-FS2_logo_2015.svg.png'),
            ('FreeForm', 'https://zynetv.net/wiz0x50xcler/freeform.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Freeform.png?raw=true'),
            ('FX', 'https://zynetv.net/wiz0x50xcler/fx.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FX.png?raw=true'),
            ('FXM', 'https://zynetv.net/wiz0x50xcler/fxm.phtml', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/FXM_Logo.svg/400px-FXM_Logo.svg.png'),
            ('Halmark Channel', 'https://zynetv.net/wiz0x50xcler/hallmark.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Hallmark%20Channel.png?raw=true'),
            ('HBO', 'https://zynetv.net/wiz0x50xcler/hbo.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/HBO.png?raw=true'),
            ('HGTV', 'https://zynetv.net/wiz0x50xcler/hgtv.phtml', 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/HGTV_2010.svg/400px-HGTV_2010.svg.png'),
            ('History Channel', 'https://zynetv.net/wiz0x50xcler/history.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/History.png?raw=true'),
            ('History 2', 'https://zyne13020.herokuapp.com/http://livecdnh1.tvanywhere.ae:80/hls/h2/04.m3u8', 'https://zynetv.net/wp-content/uploads/h2.png'),
            ('HLN', 'https://zynetv.net/wiz0x50xcler/hln.phtml', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/HLN_%28TV_network%29_2017_logo.svg/300px-HLN_%28TV_network%29_2017_logo.svg.png'),
            ('Investigation Discovery', 'https://zynetv.net/wiz0x50xcler/id.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Investigation%20Discovery.png?raw=true'),
            ('lifetime Channel', 'https://zynetv.net/wiz0x50xcler/lifetime.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Lifetime.png?raw=true'),
            ('Lifetime Movies', 'https://zynetv.net/wiz0x50xcler/lmn.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Lifetime%20Networks.png?raw=true'),
            ('MSNBC', 'https://zynetv.net/wiz0x50xcler/msnbc.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MSNBC.png?raw=true'),
            ('MTV', 'https://zynetv.net/wiz0x50xcler/mtv.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MTV.png?raw=true'),
            ('NAT GEO WILD', 'https://zynetv.net/wiz0x50xcler/natwild.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nat%20Geo%20Wild.png?raw=true'),
            ('National Geographic', 'https://zynetv.net/wiz0x50xcler/natgeo.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/National%20Geographic.png?raw=true'),
            ('NBA TV', 'https://zynetv.net/wiz0x50xcler/nbatv.phtml', 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/NBA_TV.svg/300px-NBA_TV.svg.png'),
            ('NBC', 'https://zynetv.net/wiz0x50xcler/nbc.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBC.png?raw=true'),
            ('NFL Network', 'https://zynetv.net/wiz0x50xcler/nfl.phtml', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/NFL_Network_logo.svg/450px-NFL_Network_logo.svg.png'),
            ('Nickelodeon', 'https://zynetv.net/wiz0x50xcler/nick.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nickelodeon.png?raw=true'),
            ('NickToons', 'https://zynetv.net/wiz0x50xcler/nicktoons.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NickToons.png?raw=true'),
            ('One America News Network', 'https://zynetv.net/wiz0x50xcler/oan.phtml', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/17/OANN.jpg/230px-OANN.jpg'),
            ('Oxygen', 'https://zynetv.net/wiz0x50xcler/oxygen.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Oxygen.png?raw=true'),
            ('Paramont Network', 'https://zynetv.net/wiz0x50xcler/paramount.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Paramount%20Network.png?raw=true'),
            ('PBS', 'https://zynetv.net/wiz0x50xcler/pbs.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/PBS.png?raw=true'),
            ('Science', 'https://zynetv.net/wiz0x50xcler/science.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Science%20Channel.png?raw=true'),
            ('Showtime', 'https://zynetv.net/wiz0x50xcler/showtime.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Showtime.png?raw=true'),
            ('Starz', 'https://zynetv.net/wiz0x50xcler/starz.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Starz.png?raw=true'),
            ('Sundance', 'https://zynetv.net/wiz0x50xcler/sundance.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/SundanceTV.png?raw=true'),
            ('SYFY', 'https://zynetv.net/wiz0x50xcler/syfy.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Syfy.png?raw=true'),
            ('TBS', 'https://zynetv.net/wiz0x50xcler/tbs.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TBS.png?raw=true'),
            ('The CW', 'https://zynetv.net/wiz0x50xcler/thecw.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/The%20CW.png?raw=true'),
            ('TLC', 'https://zynetv.net/wiz0x50xcler/tlc.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TLC.png?raw=true'),
            ('TNT', 'https://zynetv.net/wiz0x50xcler/tnt.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TNT.png?raw=true'),
            ('Travel Channel', 'https://zynetv.net/wiz0x50xcler/travel.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Travel%20Channel.png?raw=true'),
            ('TruTv', 'https://zynetv.net/wiz0x50xcler/trutv.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/truTV.png?raw=true'),
            ('USA Network', 'https://zynetv.net/wiz0x50xcler/usa.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/USA%20Network.png?raw=true'),
            ('VH1', 'https://zynetv.net/wiz0x50xcler/vh1.phtml', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/VH1.png?raw=true'),
            ('WWE Network', 'https://zynetv.net/wiz0x50xcler/wwe.phtml', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/WWE_Network_logo.svg/300px-WWE_Network_logo.svg.png')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': channel[1], 'image': channel[2], 'action': 'zynetvPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            if 'm3u8' in url:
                link = '%s|User-Agent=%s&Referer=%s' % (url, client.agent(), url)
                control.execute('PlayMedia(%s)' % link)
            else:
                stream = cfscrape.get(url, headers=self.headers).content
                streams = re.findall('return\(\[(.+?)\].join.+? (.+?).join.+? document.getElementById\("(.+?)"\).innerHTML',
                                     stream)
                for item in streams:
                    url2 = re.findall('var (.+?) = \[(.+?)\]', stream, re.DOTALL)
                    for code in url2:
                        if item[1].replace('+ ', '') in code[0]:
                            url3 = re.findall('id=(.+?)>(.+?)</span><span', stream, re.DOTALL)
                            for code2 in url3:
                                if item[2] in code2[0]:
                                    link = item[0].replace(',', '').replace('"', '').replace('\\', '').replace('+', '') + code[1].replace(',', '').replace('"', '') + code2[1]
                                    link = '%s|User-Agent=%s' % (link, client.agent())
                                    control.execute('PlayMedia(%s)' % link)
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
