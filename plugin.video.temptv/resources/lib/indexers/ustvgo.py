# -*- coding: utf-8 -*-
# --[ USTVgo v1.3 ]--|--[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib
from resources.lib.modules import client
from resources.lib.modules import control


class ustvgo:
    def __init__(self):
        self.list = []
        self.base_link = 'http://ustvgo.tv/%s'

    def root(self):
        channels = [
            ('ABC', 'abc-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2018/10/abc-269x151.jpg'),
            ('A&E', 'ae-networks-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/AE.png'),
            ('AMC', 'amc-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/AMC-1.png'),
            ('Animal Planet', 'animal-planet-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/animal-planet.png'),
            ('BBC America', 'bbc-america-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/BBC.jpg'),
            ('BET', 'bet', 'http://ustvgo.tv/wp-content/uploads/2019/08/bet-269x151.png'),
            ('Boomerang', 'boomerang', 'http://ustvgo.tv/wp-content/uploads/2019/08/Boomerang.png'),
            ('Bravo', 'bravo-channel-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/bravo-269x151.png'),
            ('Cartoon Network', 'cartoon-network-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/cartoon-network.jpg'),
            ('CBS', 'cbs-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2018/10/CBS-1.png'),
            ('CMT', 'cmt', 'http://ustvgo.tv/wp-content/uploads/2019/08/cmt-1.png'),
            ('CNBC', 'cnbc-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2018/10/cnbc-1.jpg'),
            ('CNN', 'cnn-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2018/10/CNN-1.png'),
            ('Comedy Central', 'comedy-central-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/comedy-central-269x151.png'),
            ('Destination America', 'destination-america', 'http://ustvgo.tv/wp-content/uploads/2019/08/Destination_America.png'),
            ('Discovery Channel', 'discovery-channel-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/Discovery.png'),
            ('Disney Channel', 'disney-channel-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/disney-269x151.png'),
            ('Disney Jr', 'disneyjr', 'http://ustvgo.tv/wp-content/uploads/2019/08/disney-jr-768x432-1.png'),
            ('Disney XD', 'disneyxd', 'http://ustvgo.tv/wp-content/uploads/2019/08/disney-xd-768x432-1.png'),
            ('DIY', 'diy', 'http://ustvgo.tv/wp-content/uploads/2019/08/diy.png'),
            ('E', 'e', 'https://cordcutting.com/wp-content/uploads/2018/01/e-network-logo.png'),
            ('ESPN', 'espn-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/espn-269x151.png'),
            ('ESPN 2', 'espn2', 'http://ustvgo.tv/wp-content/uploads/2019/08/espn2-269x151.png'),
            ('Food Network', 'food-network-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/food-network-269x151.png'),
            ('Fox Business', 'fox-business-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2018/10/foxbusiness.jpg'),
            ('Fox', 'fox-hd-live-streaming', 'http://ustvgo.tv/wp-content/uploads/2018/10/FOX-1.png'),
            ('Fox News', 'fox-news-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2018/10/foxnews.jpg'),
            ('Fox Sports 1', 'fox-sports-1', 'http://ustvgo.tv/wp-content/uploads/2019/01/fs1-269x151.png'),
            ('Fox Sports 2', 'fox-sports-2', 'http://ustvgo.tv/wp-content/uploads/2019/01/fs2-269x151.png'),
            ('FreeForm', 'freeform-channel-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/freeform-269x151.png'),
            ('FX', 'fx-channel-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/fx-269x151.png'),
            ('FXM', 'fxm', 'http://ustvgo.tv/wp-content/uploads/2019/08/FXM.png'),
            ('FXX', 'fxx', 'http://ustvgo.tv/wp-content/uploads/2019/08/FXX.png'),
            ('Golf', 'golf-channel-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/golf-269x151.png'),
            ('GSN', 'gsn', 'http://ustvgo.tv/wp-content/uploads/2019/08/GSN.jpg'),
            ('Halmark Channel', 'hallmark-channel-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/hallmark-chanel-logo.jpg'),
            ('Halmark Movies & Mysteries', 'hallmark-movies-mysteries-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/HMM_logo_black-700x245.jpg'),
            ('HBO', 'hbo', 'http://ustvgo.tv/wp-content/uploads/2019/01/hbo-269x151.png'),
            ('HGTV', 'hgtv-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/HGTV-269x151.png'),
            ('History Channel', 'history-channel-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/History.png'),
            ('HLN', 'hln', 'http://ustvgo.tv/wp-content/uploads/2019/08/HLN.jpg'),
            ('Investigation Discovery', 'investigation-discovery-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/id-269x151.jpg'),
            ('lifetime Channel', 'lifetime-channel-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/Lifetime-269x151.png'),
            ('Lifetime Movies', 'lifetime-movies', 'http://ustvgo.tv/wp-content/uploads/2019/08/lifetimeM.jpeg'),
            ('MLB Network', 'mlb-network', 'http://ustvgo.tv/wp-content/uploads/2019/05/MLB.png'),
            ('MotorTrend', 'motortrend', 'http://ustvgo.tv/wp-content/uploads/2019/08/Motortrend-1.png'),
            ('MSNBC', 'msnbc-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2018/10/msnbc_logo-269x151.jpg'),
            ('MTV', 'mtv', 'http://ustvgo.tv/wp-content/uploads/2019/08/mtv.jpg'),
            ('NAT GEO WILD', 'nat-geo-wild-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/NatGeoWild.jpeg'),
            ('National Geographic', 'national-geographic-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/National-Geographic-269x151.png'),
            ('NBA TV', 'nba-tv', 'http://ustvgo.tv/wp-content/uploads/2019/01/nbatv-269x151.jpg'),
            ('NBC Sports', 'nbc-sports', 'http://ustvgo.tv/wp-content/uploads/2019/01/nbcsn-269x151.jpg'),
            ('NBC', 'nbc', 'http://ustvgo.tv/wp-content/uploads/2018/10/nbc-logo.jpg'),
            ('NFL Network', 'nfl-network-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/nfln-logo-dark.png'),
            ('Nickelodeon', 'nickelodeon-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/Nickelodeon_2009.png'),
            ('NickToons', 'nicktoons', 'http://ustvgo.tv/wp-content/uploads/2019/08/nicktoons.png'),
            ('OWN', 'own', 'http://ustvgo.tv/wp-content/uploads/2019/08/own.jpg'),
            ('Oxygen', 'oxygen', 'http://ustvgo.tv/wp-content/uploads/2019/08/Oxygen-1.png'),
            ('Paramont Network', 'paramount-network', 'http://ustvgo.tv/wp-content/uploads/2019/08/paramount.jpg'),
            ('PBS', 'pbs-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/PBS.jpg'),
            ('POP', 'pop', 'http://ustvgo.tv/wp-content/uploads/2019/08/Pop_Network-1.png'),
            ('Science', 'science', 'http://ustvgo.tv/wp-content/uploads/2019/08/Science.jpg'),
            ('Showtime', 'showtime', 'http://ustvgo.tv/wp-content/uploads/2019/01/Showtime-269x151.png'),
            ('Starz', 'starz-channel-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/StarZ-269x151.png'),
            ('Sundance', 'sundance-tv', 'http://ustvgo.tv/wp-content/uploads/2019/08/sundance-tv.jpg'),
            ('SYFY', 'syfy-channel-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/syfy-269x151.png'),
            ('TBS', 'tbs-channel-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/tbs-269x151.png'),
            ('TCM', 'tcm', 'http://ustvgo.tv/wp-content/uploads/2019/05/TCM.png'),
            ('Telemundo', 'telemundo', 'http://ustvgo.tv/wp-content/uploads/2019/08/Telemundo.png'),
            ('Tennis Channel', 'tennis-channel-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/TennisChannel.whiteBg.png'),
            ('The CW', 'the-cw-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/cw-269x151.png'),
            ('The Weather Channel', 'the-weather-channel-live-streaming-free', 'http://ustvgo.tv/wp-content/uploads/2018/10/Weather-Channel-269x151.png'),
            ('TLC', 'tlc-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/tlc-269x151.png'),
            ('TNT', 'tnt', 'http://ustvgo.tv/wp-content/uploads/2019/01/TNT.jpg'),
            ('Travel Channel', 'travel-channel-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/Travel-269x151.png'),
            ('TruTv', 'trutv', 'http://ustvgo.tv/wp-content/uploads/2019/08/TruTV-269x151.png'),
            ('Tv Land', 'tv-land-live-free', 'http://ustvgo.tv/wp-content/uploads/2019/01/TVLand-269x151.png'),
            ('Univision', 'univision', 'http://ustvgo.tv/wp-content/uploads/2019/08/univisionlogo.jpg'),
            ('USA Network', 'usa-network-live', 'http://ustvgo.tv/wp-content/uploads/2019/01/USA-Network-269x151.png'),
            ('VH1', 'vh1', 'http://ustvgo.tv/wp-content/uploads/2019/08/vh1.png'),
            ('We Tv', 'we-tv', 'http://ustvgo.tv/wp-content/uploads/2019/08/wetv.jpg')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base_link % channel[1], 'image': channel[2], 'action': 'ustvgoPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            stream = client.request(url)
            url = re.compile("file: '(.+?)',", re.DOTALL).findall(stream)[0]
            control.execute('PlayMedia(%s)' % url)
        except Exception:
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
