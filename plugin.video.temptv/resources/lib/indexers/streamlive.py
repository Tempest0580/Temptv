# -*- coding: utf-8 -*-
# --[ Streamlive v1.0 ]--|--[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib
from resources.lib.modules import client
from resources.lib.modules import control


class streamlive:
    def __init__(self):
        self.list = []
        self.base_link = 'https://www.streamlive.to/%s'

    def root(self):
        channels = [
            ('A&E HD', 'view/68952/A&E-(HD)', 'https://www.aetv.com/assets/images/aetv/generic-thumb.jpg'),
            ('ABC HD', 'view/46476/ABC-(HD)', 'https://wpuploads.appadvice.com/wp-content/uploads/2010/03/abcicon.jpg'),
            ('AMC HD', 'view/46209/AMC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/AMC.png?raw=true'),
            ('BET HD', 'view/50652/BET-(HD))', 'https://pmcdeadline2.files.wordpress.com/2017/11/bet-network.jpg?w=681&h=383&crop=1'),
            ('Bravo HD', 'view/52480/Bravo-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bravo.png?raw=true'),
            ('Cartoon Network HD', 'view/71632/Cartoon-Network-(HD)', 'https://trilobluo.files.wordpress.com/2019/07/maxresdefault.jpg?w=624'),
            ('CBS SD', 'view/69956/CBS-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CBS.png?raw=true'),
            ('CBS HD', 'view/57976/CBS-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CBS.png?raw=true'),
            ('Cinemax HD', 'view/77172/Cinemax-(HD)', 'https://www.identityschoolofacting.com/wp-content/uploads/2018/04/cinemaxlogo.jpg'),
            ('CNBC HD', 'view/71981/CNBC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNBC.png?raw=true'),
            ('CNN HD', 'view/46461/CNN-(HD)', 'https://cdn.cnn.com/cnn/.e1mo/img/4.0/logos/CNN_logo_400x400.png'),
            ('Comedy Central HD', 'view/71610/Comedy-Central-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Comedy%20Central.png?raw=true'),
            ('CW HD', 'view/52510/CW-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/The%20CW.png?raw=true'),
            ('The CW Network HD', 'view/77122/CW-Network', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/The%20CW.png?raw=true'),
            ('Discovery HD', 'view/69112/Discovery-(HD)', 'https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Discovery_HD.svg/1200px-Discovery_HD.svg.png'),
            ('Disney Jr HD', 'view/77206/Disney-Jr-(HD)', 'http://www.filmcontact.com/sites/files/articles/disney_2.jpg'),
            ('Disney Jr Central', 'view/76879/Disney-Junior-Central', 'http://www.filmcontact.com/sites/files/articles/disney_2.jpg'),
            ('Disney Jr East HD', 'view/76878/Disney-Junior-East-(HD)', 'http://www.filmcontact.com/sites/files/articles/disney_2.jpg'),
            ('Disney XD HD', 'view/76391/Disney-XD-(HD)', 'https://yt3.ggpht.com/a/AGF-l7933ZsvaGH27w6SNIX3u_yrvVMKpzWeqWSHMQ=s900-c-k-c0xffffffff-no-rj-mo'),
            ('ESPN 2 HD', 'view/57977/ESPN-2-(HD)', 'https://media.bizj.us/view/img/11166691/espn2-logo*750xx1200-675-0-263.jpg'),
            ('Food Network HD', 'view/52506/Food-Network-(HD)', 'https://food.fnr.sndimg.com/content/dam/images/food/editorial/blog/legacy/fn-dish/2013/1/fnd_FN-New-Logo_s4x3_lead.jpg.rend.hgtvcom.616.462.suffix/1505046804671.jpeg'),
            ('Fox News HD', 'view/46465/Fox-News-(HD)', 'https://static.foxnews.com/static/orion/styles/img/fox-news/og/og-fox-news.png'),
            ('Fox Network HD', 'view/56002/Fox-Network-(HD)', 'http://static1.squarespace.com/static/54d10203e4b0d299700879e5/t/5b27f63c562fa70ec852cc1c/1529345600132/fox_network.gif?format=1500w'),
            ('FX HD', 'view/74557/FX-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FX.png?raw=true'),
            ('FreeForm HD', 'view/76645/FreeForm-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Freeform.png?raw=true'),
            ('Hallmark HD', 'view/53856/Hallmark-(HD)', 'http://allvectorlogo.com/img/2016/07/hallmark-channel-logo.png'),
            ('HBO HD', 'view/36674/HBO-(HD)', 'https://www.hbo.com/content/dam/hbodata/brand/hbo-static-1920.jpg'),
            ('HBO 2 HD', 'view/76742/HBO-2-(HD)', 'https://i1.wp.com/www.freeurtv.com/wp-content/uploads/2016/08/HBO-2-Logo.jpg?resize=555%2C310'),
            ('HBO Comedy HD', 'view/38214/HBO-Comedy-movie', 'https://www.ilovesatellitetv.com/images/hbo-comedy.jpg'),
            ('History HD', 'view/39949/History-(HD)', 'https://pmcvariety.files.wordpress.com/2018/02/history-channel-logo.jpg?w=1000'),
            ('HGTV HD', 'view/52053/HGTV-(HD))', 'https://hgtvhome.sndimg.com/content/dam/images/hgtv/editorial/homepage/HGTV-default-search-image-2017-v1.jpg.rend.hgtvcom.616.462.suffix/1487358575482.jpeg'),
            ('House MD', 'view/40783/House-MD', 'https://blog.cyrildason.com/wp-content/uploads/2016/11/House-MD.png'),
            ('Lifetime HD', 'view/57846/Lifetime-(HD)', 'https://www.mylifetime.com/assets/images/lifetime/generic-thumb.jpg'),
            ('NBC HD', 'view/57956/NBC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBC.png?raw=true'),
            ('Nick Toons HD', 'view/77205/Nick-Toons-(HD)', 'http://images.mtvnn.com/707d38966f2513b4c5151da38980ec8d/original'),
            ('NFL Network HD', 'view/NFL-Network-(HD)', 'https://www.nfl.com/static/content/public/static/scripts/network/assets/boxes/nfln_fbcard.jpg'),
            ('NFL Redzone HD', 'view/47847/NFL-Redzone-(HD)', 'http://p-img.movetv.com/cms/images/c42321dee7ac570b92a5680ce4efdc8275cf2443.jpg'),
            ('OWN - Oprah Winfrey Network HD', 'view/53857/OWN---Oprah-Winfrey-Network-(HD)', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkcegPia0KkNRhB8g8I-pPcIZXF9hqCVD1-Ev-nj-8zjXH189h'),
            ('PBS Kids HD', 'view/76647/PBS-Kids', 'https://essexpubliclibrary.org/wp-content/uploads/2018/01/PBS_Kids_Dash.svg_.png'),
            ('Science HD', 'view/68871/Science-(HD)', 'https://i.vimeocdn.com/video/463315264_1280x720.jpg'),
            ('Showtime HD', 'view/44126/Showtime-(HD)', 'https://www.sho.com/site/image-bin/images/0_0_0/0_0_0_prm-ogsho_1280x640.jpg'),
            ('Starz HD', 'view/76705/StarZ-(SD)', 'https://images-na.ssl-images-amazon.com/images/I/81RgWpOGZLL._SY355_.png'),
            ('Starz SD', 'view/76705/StarZ-(SD)', 'https://images-na.ssl-images-amazon.com/images/I/81RgWpOGZLL._SY355_.png'),
            ('TNT', 'view/69020/TNT-(SD)', 'https://www.broadcastingcable.com/.image/t_share/MTU3MjM4MTk0MDkyMzg1NjA2/tnt_resized_bc.jpg'),
            ('TLC HD', 'view/69109/TLC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TLC.png?raw=true'),
            ('Travel channel HD', 'view/65833/Travel-channel-(HD)', 'http://thebrandusa.info/enews/wp-content/uploads/sites/12/2015/08/travel_channel_logo.jpg'),
            ('TV Land HD', 'view/49252/TVLand-(HD)', 'https://yt3.ggpht.com/a/AGF-l78zn_dZJ68pYkjCSobUxEX4cvd2QUtjzf65Iw=s900-c-k-c0xffffffff-no-rj-mo'),
            ('Universo HD', 'view/47844/Universo-(HD)', 'https://www.multichannel.com/.image/t_share/MTU0MDY0OTM5NjQ5NjA2NzM4/nbcuniversojpg.jpg'),
            ('USA Network HD', 'view/38768/USA-Network-(HD)', 'https://www.multichannel.com/.image/t_share/MTU0MDY0OTM5NjQ5NjA2NzM4/nbcuniversojpg.jpg'),
            ('VH1 HD', 'view/52988/VH1-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/USA%20Network.png?raw=true')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base_link % channel[1], 'image': channel[2], 'action': 'streamlivePlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            stream = client.request(url)
            url = re.compile('href="(https://nl2.streamlive.to/vlc/?.+?)"').findall(stream)[0]
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
