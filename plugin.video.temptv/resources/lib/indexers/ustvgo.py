# -*- coding: utf-8 -*-
# --[ USTVgo v1.4 ]--|--[ From JewBMX & Tempest ]--
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
            ('ABC', 'abc-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ABC.png?raw=true'),
            ('A&E', 'ae-networks-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/A&E.png?raw=true'),
            ('AMC', 'amc-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/AMC.png?raw=true'),
            ('Animal Planet', 'animal-planet-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Animalplanet.png?raw=true'),
            ('BBC America', 'bbc-america-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/BBC%20America.png?raw=true'),
            ('BET', 'bet', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bet.png?raw=true'),
            ('Boomerang', 'boomerang', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Boomerang.png?raw=true'),
            ('Bravo', 'bravo-channel-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bravo.png?raw=true'),
            ('Cartoon Network', 'cartoon-network-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Cartoon%20Network.png?raw=true'),
            ('CBS', 'cbs-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CBS.png?raw=true'),
            ('CMT', 'cmt', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CMT%20Films.png?raw=true'),
            ('CNBC', 'cnbc-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNBC.png?raw=true'),
            ('CNN', 'cnn-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNN.png?raw=true'),
            ('Comedy Central', 'comedy-central-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Comedy%20Central.png?raw=true'),
            ('Destination America', 'destination-america', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Destination_America_logo.svg/400px-Destination_America_logo.svg.png'),
            ('Discovery Channel', 'discovery-channel-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Discovery%20Channel.png?raw=true'),
            ('Disney Channel', 'disney-channel-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20Channel.png?raw=true'),
            ('Disney Jr', 'disneyjr', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20Junior.png?raw=true'),
            ('Disney XD', 'disneyxd', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20XD.png?raw=true'),
            ('DIY', 'diy', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/DIY.png?raw=true'),
            ('E', 'e', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/E!.png?raw=true'),
            ('ESPN', 'espn-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('ESPN 2', 'espn2', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('Food Network', 'food-network-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Food%20Network.png?raw=true'),
            ('Fox Business', 'fox-business-live-streaming-free', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Fox_Business.svg/420px-Fox_Business.svg.png'),
            ('Fox', 'fox-hd-live-streaming', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FOX.png?raw=true'),
            ('Fox News', 'fox-news-live-streaming-free', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/300px-Fox_News_Channel_logo.svg.png'),
            ('Fox Sports 1', 'fox-sports-1', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/2015_Fox_Sports_1_logo.svg/400px-2015_Fox_Sports_1_logo.svg.png'),
            ('Fox Sports 2', 'fox-sports-2', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/FS2_logo_2015.svg/400px-FS2_logo_2015.svg.png'),
            ('FreeForm', 'freeform-channel-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Freeform.png?raw=true'),
            ('FX', 'fx-channel-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FX.png?raw=true'),
            ('FXM', 'fxm', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/FXM_Logo.svg/400px-FXM_Logo.svg.png'),
            ('FXX', 'fxx', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FXX.png?raw=true'),
            ('Golf', 'golf-channel-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Golf.png?raw=true'),
            ('GSN', 'gsn', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Game%20Show%20Network.png?raw=true'),
            ('Halmark Channel', 'hallmark-channel-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Hallmark%20Channel.png?raw=true'),
            ('Halmark Movies & Mysteries', 'hallmark-movies-mysteries-live-streaming-free', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Hallmark_movies_mysteries.png/220px-Hallmark_movies_mysteries.png'),
            ('HBO', 'hbo', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/HBO.png?raw=true'),
            ('HGTV', 'hgtv-live-streaming-free', 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/HGTV_2010.svg/400px-HGTV_2010.svg.png'),
            ('History Channel', 'history-channel-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/History.png?raw=true'),
            ('HLN', 'hln', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/HLN_%28TV_network%29_2017_logo.svg/300px-HLN_%28TV_network%29_2017_logo.svg.png'),
            ('Investigation Discovery', 'investigation-discovery-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Investigation%20Discovery.png?raw=true'),
            ('lifetime Channel', 'lifetime-channel-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Lifetime.png?raw=true'),
            ('Lifetime Movies', 'lifetime-movies', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Lifetime%20Networks.png?raw=true'),
            ('MLB Network', 'mlb-network', 'https://upload.wikimedia.org/wikipedia/en/thumb/a/ac/MLBNetworkLogo.svg/280px-MLBNetworkLogo.svg.png'),
            ('MotorTrend', 'motortrend', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Motor_Trend.svg/400px-Motor_Trend.svg.png'),
            ('MSNBC', 'msnbc-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MSNBC.png?raw=true'),
            ('MTV', 'mtv', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MTV.png?raw=true'),
            ('NAT GEO WILD', 'nat-geo-wild-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nat%20Geo%20Wild.png?raw=true'),
            ('National Geographic', 'national-geographic-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/National%20Geographic.png?raw=true'),
            ('NBA TV', 'nba-tv', 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/NBA_TV.svg/300px-NBA_TV.svg.png'),
            ('NBC Sports', 'nbc-sports', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBCSN.png?raw=true'),
            ('NBC', 'nbc', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBC.png?raw=true'),
            ('NFL Network', 'nfl-network-live-free', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/NFL_Network_logo.svg/450px-NFL_Network_logo.svg.png'),
            ('Nickelodeon', 'nickelodeon-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nickelodeon.png?raw=true'),
            ('NickToons', 'nicktoons', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NickToons.png?raw=true'),
            ('OWN', 'own', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/OWN.png?raw=true'),
            ('Oxygen', 'oxygen', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Oxygen.png?raw=true'),
            ('Paramont Network', 'paramount-network', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Paramount%20Network.png?raw=true'),
            ('PBS', 'pbs-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/PBS.png?raw=true'),
            ('POP', 'pop', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Pop_Network_Logo.png/220px-Pop_Network_Logo.png'),
            ('Science', 'science', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Science%20Channel.png?raw=true'),
            ('Showtime', 'showtime', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Showtime.png?raw=true'),
            ('Starz', 'starz-channel-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Starz.png?raw=true'),
            ('Sundance', 'sundance-tv', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/SundanceTV.png?raw=true'),
            ('SYFY', 'syfy-channel-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Syfy.png?raw=true'),
            ('TBS', 'tbs-channel-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TBS.png?raw=true'),
            ('TCM', 'tcm', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Turner%20Classic%20Movies%20(TCM).png?raw=true'),
            ('Telemundo', 'telemundo', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Telemundo_Logo_2018-2.svg/440px-Telemundo_Logo_2018-2.svg.png'),
            ('Tennis Channel', 'tennis-channel-live-free', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Tennis_Channel_logo.svg/220px-Tennis_Channel_logo.svg.png'),
            ('The CW', 'the-cw-live-streaming-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/The%20CW.png?raw=true'),
            ('The Weather Channel', 'the-weather-channel-live-streaming-free', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/The_Weather_Channel_logo_2005-present.svg/300px-The_Weather_Channel_logo_2005-present.svg.png'),
            ('TLC', 'tlc-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TLC.png?raw=true'),
            ('TNT', 'tnt', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TNT.png?raw=true'),
            ('Travel Channel', 'travel-channel-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Travel%20Channel.png?raw=true'),
            ('TruTv', 'trutv', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/truTV.png?raw=true'),
            ('Tv Land', 'tv-land-live-free', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TV%20Land.png?raw=true'),
            ('Univision', 'univision', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Logo_Univision_2019.svg/400px-Logo_Univision_2019.svg.png'),
            ('USA Network', 'usa-network-live', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/USA%20Network.png?raw=true'),
            ('VH1', 'vh1', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/VH1.png?raw=true'),
            ('We Tv', 'we-tv', 'https://upload.wikimedia.org/wikipedia/en/thumb/d/db/We_TV_logo_2014.svg/440px-We_TV_logo_2014.svg.png')
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
