# -*- coding: utf-8 -*-
# --[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib, base64
from resources.lib.modules import client
from resources.lib.modules import control


class ustvgo:
    def __init__(self):
        self.list = []
        self.base_link = 'https://ustvgo.tv'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}

    def root(self):
        channels = [
            ('ABC', '/player.php?stream=ABC', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ABC.png?raw=true'),
            ('A&E', '/player.php?stream=AE', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/A&E.png?raw=true'),
            ('AMC', '/player.php?stream=AMC', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/AMC.png?raw=true'),
            ('Animal Planet', '/player.php?stream=ANIMAL', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Animalplanet.png?raw=true'),
            ('BBC America', '/player.php?stream=BBCAmerica', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/BBC%20America.png?raw=true'),
            ('BET', '/player.php?stream=BET', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bet.png?raw=true'),
            ('Boomerang', '/player.php?stream=Boomerang', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Boomerang.png?raw=true'),
            ('Bravo', '/player.php?stream=Bravo', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bravo.png?raw=true'),
            ('Cartoon Network', '/player.php?stream=CN', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Cartoon%20Network.png?raw=true'),
            ('CBS', '/player.php?stream=CBS', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CBS.png?raw=true'),
            ('Cinemax', '/player.php?stream=Cinemax', 'https://www.tvinsider.com/wp-content/uploads/2017/06/cinemaxlogo.jpg'),
            ('CMT', '/player.php?stream=CMT', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CMT%20Films.png?raw=true'),
            ('CNBC', '/player.php?stream=CNBC', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNBC.png?raw=true'),
            ('CNN', '/player.php?stream=CNN', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNN.png?raw=true'),
            ('Comedy Central', '/player.php?stream=Comedy', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Comedy%20Central.png?raw=true'),
            ('Destination America', '/player.php?stream=DA', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Destination_America_logo.svg/400px-Destination_America_logo.svg.png'),
            ('Discovery Channel', '/player.php?stream=Discovery', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Discovery%20Channel.png?raw=true'),
            ('Disney Channel', '/player.php?stream=Disney', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20Channel.png?raw=true'),
            ('Disney Jr', '/player.php?stream=DisneyJr', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20Junior.png?raw=true'),
            ('Disney XD', '/player.php?stream=DisneyXD', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20XD.png?raw=true'),
            ('DIY', '/player.php?stream=DIY', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/DIY.png?raw=true'),
            ('E!', '/player.php?stream=E', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/E!.png?raw=true'),
            ('ESPN', '/player.php?stream=ESPN', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('ESPN 2', '/player.php?stream=ESPN2', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('Food Network', '/player.php?stream=FoodNetwork', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Food%20Network.png?raw=true'),
            ('Fox', '/player.php?stream=FOX', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FOX.png?raw=true'),
            ('Fox Business', '/player.php?stream=FoxBusiness', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Fox_Business.svg/420px-Fox_Business.svg.png'),
            ('Fox News', '/player.php?stream=FoxNews', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/300px-Fox_News_Channel_logo.svg.png'),
            ('Fox Sports 1', '/player.php?stream=FS1', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/2015_Fox_Sports_1_logo.svg/400px-2015_Fox_Sports_1_logo.svg.png'),
            ('Fox Sports 2', '/player.php?stream=FS2', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/FS2_logo_2015.svg/400px-FS2_logo_2015.svg.png'),
            ('FreeForm', '/player.php?stream=Freeform', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Freeform.png?raw=true'),
            ('FX', '/player.php?stream=FX', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FX.png?raw=true'),
            ('FXM', '/player.php?stream=FXMovie', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/FXM_Logo.svg/400px-FXM_Logo.svg.png'),
            ('FXX', '/player.php?stream=FXX', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FXX.png?raw=true'),
            ('Golf', '/player.php?stream=GOLF', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Golf.png?raw=true'),
            ('GSN', '/player.php?stream=GSN', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Game%20Show%20Network.png?raw=true'),
            ('Halmark Channel', '/player.php?stream=Hallmark', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Hallmark%20Channel.png?raw=true'),
            ('Halmark Movies & Mysteries', '/player.php?stream=HMM', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Hallmark_movies_mysteries.png/220px-Hallmark_movies_mysteries.png'),
            ('HBO', '/player2.php?stream=HBO', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/HBO.png?raw=true'),
            ('HGTV', '/player.php?stream=HGTV', 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/HGTV_2010.svg/400px-HGTV_2010.svg.png'),
            ('History Channel', '/player.php?stream=History', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/History.png?raw=true'),
            ('HLN', '/player.php?stream=HLN', 'https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/HLN_%28TV_network%29_2017_logo.svg/300px-HLN_%28TV_network%29_2017_logo.svg.png'),
            ('Investigation Discovery', '/player.php?stream=ID', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Investigation%20Discovery.png?raw=true'),
            ('lifetime Channel', '/player.php?stream=Lifetime', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Lifetime.png?raw=true'),
            ('Lifetime Movies', '/player.php?stream=LifetimeM', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Lifetime%20Networks.png?raw=true'),
            ('MLB Network', '/player.php?stream=MLB', 'https://upload.wikimedia.org/wikipedia/en/thumb/a/ac/MLBNetworkLogo.svg/280px-MLBNetworkLogo.svg.png'),
            ('MotorTrend', '/player.php?stream=MotorTrend', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Motor_Trend.svg/400px-Motor_Trend.svg.png'),
            ('MSNBC', '/player.php?stream=MSNBC', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MSNBC.png?raw=true'),
            ('MTV', '/player.php?stream=MTV', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MTV.png?raw=true'),
            ('NAT GEO WILD', '/player.php?stream=NatGEOWild', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nat%20Geo%20Wild.png?raw=true'),
            ('National Geographic', '/player.php?stream=NatGEO', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/National%20Geographic.png?raw=true'),
            ('NBA TV', '/player.php?stream=NBA', 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/NBA_TV.svg/300px-NBA_TV.svg.png'),
            ('NBC', '/player.php?stream=NBC', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBC.png?raw=true'),
            ('NBC Sports', '/player.php?stream=NBCSN', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBCSN.png?raw=true'),
            ('NFL Network', '/player.php?stream=NFL', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/NFL_Network_logo.svg/450px-NFL_Network_logo.svg.png'),
            ('Nickelodeon', '/player.php?stream=Nickelodeon', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nickelodeon.png?raw=true'),
            ('NickToons', '/player.php?stream=Nicktoons', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NickToons.png?raw=true'),
            ('One America News Network', '/player.php?stream=OAN', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/17/OANN.jpg/230px-OANN.jpg'),
            ('OWN', '/player.php?stream=OWN', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/OWN.png?raw=true'),
            ('Oxygen', '/player.php?stream=Oxygen', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Oxygen.png?raw=true'),
            ('Paramont Network', '/player.php?stream=Paramount', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Paramount%20Network.png?raw=true'),
            ('PBS', '/player.php?stream=PBS', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/PBS.png?raw=true'),
            ('POP', '/player.php?stream=POP', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Pop_Network_Logo.png/220px-Pop_Network_Logo.png'),
            ('Science', '/player.php?stream=Science', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Science%20Channel.png?raw=true'),
            ('Showtime', '/player2.php?stream=Showtime', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Showtime.png?raw=true'),
            ('Starz', '/player.php?stream=StarZ', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Starz.png?raw=true'),
            ('Sundance', '/player.php?stream=SundanceTV', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/SundanceTV.png?raw=true'),
            ('SYFY', '/player.php?stream=SYFY', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Syfy.png?raw=true'),
            ('TBS', '/player.php?stream=TBS', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TBS.png?raw=true'),
            ('TCM', '/player.php?stream=TCM', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Turner%20Classic%20Movies%20(TCM).png?raw=true'),
            ('Telemundo', '/player.php?stream=Telemundo', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Telemundo_Logo_2018-2.svg/440px-Telemundo_Logo_2018-2.svg.png'),
            ('Tennis Channel', '/player.php?stream=Tennis', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Tennis_Channel_logo.svg/220px-Tennis_Channel_logo.svg.png'),
            ('The CW', '/player.php?stream=CW', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/The%20CW.png?raw=true'),
            ('TLC', '/player.php?stream=TLC', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TLC.png?raw=true'),
            ('TNT', '/player.php?stream=TNT', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TNT.png?raw=true'),
            ('Travel Channel', '/player.php?stream=Travel', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Travel%20Channel.png?raw=true'),
            ('TruTv', '/player.php?stream=TruTV', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/truTV.png?raw=true'),
            ('Tv Land', '/player.php?stream=TVLand', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TV%20Land.png?raw=true'),
            ('Univision', '/player.php?stream=Univision', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Logo_Univision_2019.svg/400px-Logo_Univision_2019.svg.png'),
            ('USA Network', '/player.php?stream=USANetwork', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/USA%20Network.png?raw=true'),
            ('VH1', '/player.php?stream=VH1', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/VH1.png?raw=true'),
            ('We Tv', '/player.php?stream=WETV', 'https://upload.wikimedia.org/wikipedia/en/thumb/d/db/We_TV_logo_2014.svg/440px-We_TV_logo_2014.svg.png'),
            ('WWE Network', '/player.php?stream=WWE', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/WWE_Network_logo.svg/300px-WWE_Network_logo.svg.png'),
            ('Yes Network', '/player.php?stream=YES', 'https://www.sportsvideo.org/new/wp-content/uploads/2017/02/yes_network.jpg')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base_link + channel[1], 'image': channel[2], 'action': 'ustvgoPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            link = client.request(url, headers=self.headers)
            link = re.compile("atob\('(.+?)'\);").findall(link)[0]
            link = base64.b64decode(link)
            link = '%s|User-Agent=%s&Referer=%s' % (link, client.agent(), self.base_link)
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
