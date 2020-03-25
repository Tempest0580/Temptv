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
        self.headers = {'User-Agent': client.agent()}

    def root(self):
        channels = [
            ('A&E', 'view/76672/A&E-(SD)', 'https://www.aetv.com/assets/images/aetv/generic-thumb.jpg'),
            ('ABC', 'view/68969/ABC-(SD)', 'https://wpuploads.appadvice.com/wp-content/uploads/2010/03/abcicon.jpg'),
            ('ABC HD', 'view/46476/ABC-(HD)', 'https://wpuploads.appadvice.com/wp-content/uploads/2010/03/abcicon.jpg'),
            ('AMC', 'view/76666/AMC-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/AMC.png?raw=true'),
            ('Animal Planet', 'view/76673/Animal-Planet-(SD)', 'https://cdn1.thr.com/sites/default/files/imagecache/landscape_928x523/2013/01/animal_planet_logo.jpg'),
            ('Big Ten Network BTN HD', 'view/76730/Big-Ten-Network-BTN-(HD)', 'https://btn.com/wp-content/uploads/2019/08/btn_logo_kit_page_4a.jpg?w=970&h=546&crop=1'),
            ('Cartoon Network', 'view/76674/Cartoon-Network-(SD)', 'https://trilobluo.files.wordpress.com/2019/07/maxresdefault.jpg?w=624'),
            ('CNN', 'view/68967/CNN-(SD)', 'https://cdn.cnn.com/cnn/.e1mo/img/4.0/logos/CNN_logo_400x400.png'),
            ('Disney HD', 'view/38804/Disney-(HD)', 'https://i.pinimg.com/originals/64/31/14/643114ea438c7b019cbf8c88b2d2ba47.jpg'),
            ('Disney', 'view/76679/Disney-(SD)', 'https://i.pinimg.com/originals/64/31/14/643114ea438c7b019cbf8c88b2d2ba47.jpg'),
            ('ESPN HD', 'view/57977/ESPN-2-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('ESPN 2', 'view/69028/ESPN-2-(SD)', 'https://media.bizj.us/view/img/11166691/espn2-logo*750xx1200-675-0-263.jpg'),
            ('ESPN Deportes HD', 'view/76738/ESPN-Deportes-(HD)', 'https://espnpressroom.com/us/files/2016/03/RS1129_ESPN_Deportes_CLR_Pos-scr-1-850x610.jpg'),
            ('ESPN U HD', 'view/76663/ESPN-U-(HD)', 'http://p-img.movetv.com/cms/images/a5e621a17fba73a2dd3f8c0304168aebc9253dd4.jpg'),
            ('Food Network', 'view/69023/Food-Network-(SD)', 'https://pmcvariety.files.wordpress.com/2016/01/food-network-logo.jpg?w=1000&h=563&crop=1'),
            ('Food Network NY HD', 'view/77023/Fox-Network-NY-(HD)', 'https://images.foxtv.com/www.fox5ny.com/img/724/407/default-image.png?ve=1&tl=1'),
            ('Fox News', 'view/68968/Fox-News-(SD)', 'https://static.foxnews.com/static/orion/styles/img/fox-news/og/og-fox-news.png'),
            ('Fox Network HD', 'view/56002/Fox-Network-(HD)', 'http://static1.squarespace.com/static/54d10203e4b0d299700879e5/t/5b27f63c562fa70ec852cc1c/1529345600132/fox_network.gif?format=1500w'),
            ('Fox Movie Channel', 'view/38449/Fox-Movie-Channel', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRj-8O-xPgxgqkw3ujUMCWGmw0yh9I1V9UoEpEIlPncXaAAGtyC'),
            ('Fox Sports 2', 'view/76681/Fox-Sports-2-(SD)', 'https://i.pinimg.com/originals/2f/c6/c8/2fc6c8b8cef098c7c325bc507b595795.jpg'),
            ('Fox Business', 'view/76680/Fox-Business-(SD)', 'https://talkingbiznews.com/wp-content/uploads/2011/09/fox-business-logo.jpg'),
            ('FXM', 'view/79283/FXM', 'https://pbs.twimg.com/profile_images/378800000290446785/bbcee77125173fe3b41b836f5749ca2c_400x400.jpeg'),
            ('Hallmark', 'view/76683/Hallmark-(SD)', 'http://allvectorlogo.com/img/2016/07/hallmark-channel-logo.png'),
            ('HBO', 'view/69021/HBO-(SD)', 'https://www.hbo.com/content/dam/hbodata/brand/hbo-static-1920.jpg'),
            ('NBC Sport Network', 'view/71137/NBC-Sport-Network-(SD)', 'https://thecomeback.com/awfulannouncing/wp-content/uploads/sites/94/2014/01/nbcsnblack.jpg'),
            ('MLB Network', 'view/76688/MLB-Network-(SD)', 'https://www.f5.com/content/dam/f5-com/page-assets-en/home-en/customers/case-studies/logo-mlb-network.png'),
            ('MTV - Music Television SD', 'view/69037/MTV---Music-Television-(SD)', 'https://i.pinimg.com/originals/7f/00/b4/7f00b470cf30f87fa616281abe46dbb2.jpg'),
            ('Nickelodeon HD', 'view/71112/Nickelodeon-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nickelodeon.png?raw=true'),
            ('Nickelodeon', 'view/76702/Nickelodeon-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nickelodeon.png?raw=true'),
            ('NFL Network', 'vview/72886/NFL-Network-(SD)', 'https://www.nfl.com/static/content/public/static/scripts/network/assets/boxes/nfln_fbcard.jpg'),
            ('MSNBC', 'view/76689/MSNBC-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MSNBC.png?raw=true'),
            ('OWN - Oprah Winfrey Network', 'view/76670/OWN-Oprah-Winfrey-Network-(SD)', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkcegPia0KkNRhB8g8I-pPcIZXF9hqCVD1-Ev-nj-8zjXH189h'),
            ('Science', 'view/76693/Science-(SD)', 'https://i.vimeocdn.com/video/463315264_1280x720.jpg'),
            ('Showtime', 'view/69036/Showtime-(SD)', 'https://www.sho.com/site/image-bin/images/0_0_0/0_0_0_prm-ogsho_1280x640.jpg'),
            ('Starz', 'view/76705/StarZ-(SD)', 'https://images-na.ssl-images-amazon.com/images/I/81RgWpOGZLL._SY355_.png'),
            ('TNT', 'view/69020/TNT-(SD)', 'https://www.broadcastingcable.com/.image/t_share/MTU3MjM4MTk0MDkyMzg1NjA2/tnt_resized_bc.jpg'),
            ('Travel channel', 'view/69019/Travel-chanel-(SD)', 'http://thebrandusa.info/enews/wp-content/uploads/sites/12/2015/08/travel_channel_logo.jpg'),
            ('TruTV', 'view/73009/TruTV-(SD)', 'https://pmcvariety.files.wordpress.com/2014/07/trutv-logo.jpg?w=1000'),
            ('USA Network', 'view/73018/USA-Network-(SD)', 'https://www.cultjer.com/img/ug_photo/2016_06/65873520160628092848.jpg'),
            ('VH1', 'view/76699/VH1-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/USA%20Network.png?raw=true'),
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base_link % channel[1], 'image': channel[2], 'action': 'streamlivePlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            stream = client.request(url, headers=self.headers)
            result = re.compile("return([[\a-zA-Z]+]).join").findall(stream)
            for result in result:
                result = result.strip('([]').replace('\/', '/').replace(',', '').replace('"', '')
                result = 'https:' + result
                link = result + self.code(url) + self.code2(url)
                link = '%s|Referer=%s' % (link, url)
                control.execute('PlayMedia(%s)' % link)
        except Exception:
            return

    def code(self, url):
        try:
            stream = client.request(url, headers=self.headers)
            result2 = re.compile("\+ (.+?).join").findall(stream)[0]
            result3 = re.findall("var (.+?) = \[(.+?)\];", stream)
            for link, code in result3:
                if result2 in link:
                    code = code.replace(',','').replace('"', '')
                    return code
        except:
            return

    def code2(self, url):
        try:
            stream = client.request(url, headers=self.headers)
            result4 = re.compile("id=(.+?)>(.+?)</span").findall(stream)
            result5 = re.findall('\+ document.getElementById(.+?).innerHTML', stream)[0]
            result5 = result5.strip('("")')
            for link, code2 in result4:
                if 'success' in link: continue
                if result5 in link:
                    return code2
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
