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
            ('A&E SD', 'view/76672/A&E-(SD)', 'https://www.aetv.com/assets/images/aetv/generic-thumb.jpg'),
            ('ABC HD', 'view/46476/ABC-(HD)', 'https://wpuploads.appadvice.com/wp-content/uploads/2010/03/abcicon.jpg'),
            ('ABC SD', 'view/68969/ABC-(SD)', 'https://wpuploads.appadvice.com/wp-content/uploads/2010/03/abcicon.jpg'),
            ('AMC HD', 'view/46209/AMC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/AMC.png?raw=true'),
            ('Animal Planet HD', 'view/76413/Animal-Planet-(HD)', 'https://cdn1.thr.com/sites/default/files/imagecache/landscape_928x523/2013/01/animal_planet_logo.jpg'),
            ('Animal Planet SD', 'view/76673/Animal-Planet-(SD)', 'https://cdn1.thr.com/sites/default/files/imagecache/landscape_928x523/2013/01/animal_planet_logo.jpg'),
            ('BBC America HD', 'view/77193/BBC-America-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/BBC%20America.png?raw=true'),
            ('BET HD', 'view/50652/BET-(HD)', 'https://pmcdeadline2.files.wordpress.com/2017/11/bet-network.jpg?w=681&h=383&crop=1'),
            ('BET SD', 'view/72736/BET-(SD)', 'https://pmcdeadline2.files.wordpress.com/2017/11/bet-network.jpg?w=681&h=383&crop=1'),
            ('Boomerang HD', 'view/77024/Boomerang-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Boomerang.png?raw=true'),
            ('Boomerang SD', 'view/77197/Boomerang-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Boomerang.png?raw=true'),
            ('Bravo HD', 'view/52480/Bravo-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bravo.png?raw=true'),
            ('Cartoon Network HD', 'view/71632/Cartoon-Network-(HD)', 'https://trilobluo.files.wordpress.com/2019/07/maxresdefault.jpg?w=624'),
            ('Cartoon Network SD', 'view/76674/Cartoon-Network-(SD)', 'https://trilobluo.files.wordpress.com/2019/07/maxresdefault.jpg?w=624'),
            ('CBS SD', 'view/69956/CBS-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CBS.png?raw=true'),
            ('CBS HD', 'view/57976/CBS-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CBS.png?raw=true'),
            ('Cinemax HD', 'view/77172/Cinemax-(HD)', 'https://www.identityschoolofacting.com/wp-content/uploads/2018/04/cinemaxlogo.jpg'),
            ('CNBC HD', 'view/71981/CNBC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNBC.png?raw=true'),
            ('CNBC SD', 'view/76676/CNBC-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNBC.png?raw=true'),
            ('CNN HD', 'view/46461/CNN-(HD)', 'https://cdn.cnn.com/cnn/.e1mo/img/4.0/logos/CNN_logo_400x400.png'),
            ('CNN SD', 'view/68967/CNN-(SD)', 'https://cdn.cnn.com/cnn/.e1mo/img/4.0/logos/CNN_logo_400x400.png'),
            ('Comedy Central HD', 'view/71610/Comedy-Central-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Comedy%20Central.png?raw=true'),
            ('CW HD', 'view/52510/CW-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/The%20CW.png?raw=true'),
            ('CW SD', 'view/76678/CW-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/The%20CW.png?raw=true'),
            ('The CW Network HD', 'view/77122/CW-Network', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/The%20CW.png?raw=true'),
            ('Discovery HD', 'view/69112/Discovery-(HD)', 'https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Discovery_HD.svg/1200px-Discovery_HD.svg.png'),
            ('Discovery SD', 'view/69110/Discovery-(SD)', 'https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Discovery_HD.svg/1200px-Discovery_HD.svg.png'),
            ('Disney HD', 'view/38804/Disney-(HD)', 'https://i.pinimg.com/originals/64/31/14/643114ea438c7b019cbf8c88b2d2ba47.jpg'),
            ('Disney SD', 'view/76679/Disney-(SD)', 'https://i.pinimg.com/originals/64/31/14/643114ea438c7b019cbf8c88b2d2ba47.jpg'),
            ('Disney Jr HD', 'view/77206/Disney-Jr-(HD)', 'http://www.filmcontact.com/sites/files/articles/disney_2.jpg'),
            ('Disney Jr Central', 'view/76879/Disney-Junior-Central', 'http://www.filmcontact.com/sites/files/articles/disney_2.jpg'),
            ('Disney Jr East HD', 'view/76878/Disney-Junior-East-(HD)', 'http://www.filmcontact.com/sites/files/articles/disney_2.jpg'),
            ('Disney XD HD', 'view/76391/Disney-XD-(HD)', 'https://yt3.ggpht.com/a/AGF-l7933ZsvaGH27w6SNIX3u_yrvVMKpzWeqWSHMQ=s900-c-k-c0xffffffff-no-rj-mo'),
            ('ESPN HD', 'view/57977/ESPN-2-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('ESPN SD', 'view/69029/ESPN-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('ESPN 2 HD', 'view/57977/ESPN-2-(HD)', 'https://media.bizj.us/view/img/11166691/espn2-logo*750xx1200-675-0-263.jpg'),
            ('ESPN 2 SD', 'view/69028/ESPN-2-(SD)', 'https://media.bizj.us/view/img/11166691/espn2-logo*750xx1200-675-0-263.jpg'),
            ('Food Network HD', 'view/52506/Food-Network-(HD)', 'https://pmcvariety.files.wordpress.com/2016/01/food-network-logo.jpg?w=1000&h=563&crop=1'),
            ('Food Network SD', 'view/69023/Food-Network-(SD)', 'https://pmcvariety.files.wordpress.com/2016/01/food-network-logo.jpg?w=1000&h=563&crop=1'),
            ('Fox News HD', 'view/46465/Fox-News-(HD)', 'https://static.foxnews.com/static/orion/styles/img/fox-news/og/og-fox-news.png'),
            ('Fox Network HD', 'view/56002/Fox-Network-(HD)', 'http://static1.squarespace.com/static/54d10203e4b0d299700879e5/t/5b27f63c562fa70ec852cc1c/1529345600132/fox_network.gif?format=1500w'),
            ('Fox Movie Channel', 'view/38449/Fox-Movie-Channel', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRj-8O-xPgxgqkw3ujUMCWGmw0yh9I1V9UoEpEIlPncXaAAGtyC'),
            ('FX HD', 'view/74557/FX-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FX.png?raw=true'),
            ('FXX HD', 'view/76785/FXX-(Pacific)', 'https://pmcdeadline2.files.wordpress.com/2014/06/fxx_logogrid-e1565189089233.jpg?w=389&h=218'),
            ('FreeForm HD', 'view/76645/FreeForm-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Freeform.png?raw=true'),
            ('Hallmark HD', 'view/53856/Hallmark-(HD)', 'http://allvectorlogo.com/img/2016/07/hallmark-channel-logo.png'),
            ('HBO HD', 'view/36674/HBO-(HD)', 'https://www.hbo.com/content/dam/hbodata/brand/hbo-static-1920.jpg'),
            ('HBO 2 HD', 'view/76742/HBO-2-(HD)', 'https://i1.wp.com/www.freeurtv.com/wp-content/uploads/2016/08/HBO-2-Logo.jpg?resize=555%2C310'),
            ('HBO Comedy HD', 'view/38214/HBO-Comedy-movie', 'https://www.ilovesatellitetv.com/images/hbo-comedy.jpg'),
            ('History HD', 'view/39949/History-(HD)', 'https://pmcvariety.files.wordpress.com/2018/02/history-channel-logo.jpg?w=1000'),
            ('HGTV HD', 'view/52053/HGTV-(HD))', 'https://hgtvhome.sndimg.com/content/dam/images/hgtv/editorial/homepage/HGTV-default-search-image-2017-v1.jpg.rend.hgtvcom.616.462.suffix/1487358575482.jpeg'),
            ('Investigation Discovery HD', 'view/69111/ID---Investigation-Discovery-(HD)', 'http://cdn.realscreen.com/wp/wp-content/uploads/2018/10/Investigation-Discovery-ID.jpg?426102'),
            ('Investigation Discovery SD', 'view/76686/ID---Investigation-Discovery-(SD)', 'http://cdn.realscreen.com/wp/wp-content/uploads/2018/10/Investigation-Discovery-ID.jpg?426102'),
            ('Lifetime HD', 'view/57846/Lifetime-(HD)', 'https://www.mylifetime.com/assets/images/lifetime/generic-thumb.jpg'),
            ('Lifetime Movie Network HD', 'view/76394/Lifetime-Movie-Network-(HD)', 'https://pbs.twimg.com/profile_images/884890131513126913/ZmrZn7Y4_400x400.jpg'),
            ('NBC HD', 'view/57956/NBC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBC.png?raw=true'),
            ('NBC SD', 'view/69116/NBC-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBC.png?raw=true'),
            ('NBC NY', 'view/77074/NBC-4-NY', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBC.png?raw=true'),
            ('Nickelodeon HD', 'view/71112/Nickelodeon-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nickelodeon.png?raw=true'),
            ('Nickelodeon SD', 'view/76702/Nickelodeon-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nickelodeon.png?raw=true'),
            ('Nick Toons HD', 'view/77205/Nick-Toons-(HD)', 'http://images.mtvnn.com/707d38966f2513b4c5151da38980ec8d/original'),
            ('Nick Jr', 'view/76880/Nick-Jr.', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUKvWGmxVUKHR0Ri9klrWPiJ3XbN2WdeuRfduLIIaIEU5lR3pc'),
            ('NFL Network HD', 'view/NFL-Network-(HD)', 'https://www.nfl.com/static/content/public/static/scripts/network/assets/boxes/nfln_fbcard.jpg'),
            ('NFL Redzone HD', 'view/47847/NFL-Redzone-(HD)', 'http://p-img.movetv.com/cms/images/c42321dee7ac570b92a5680ce4efdc8275cf2443.jpg'),
            ('MSNBC HD', 'view/52505/MSNBC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MSNBC.png?raw=true'),
            ('MSNBC SD', 'view/76689/MSNBC-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MSNBC.png?raw=true'),
            ('OWN - Oprah Winfrey Network HD', 'view/53857/OWN---Oprah-Winfrey-Network-(HD)', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkcegPia0KkNRhB8g8I-pPcIZXF9hqCVD1-Ev-nj-8zjXH189h'),
            ('PBS Kids HD', 'view/76647/PBS-Kids', 'https://essexpubliclibrary.org/wp-content/uploads/2018/01/PBS_Kids_Dash.svg_.png'),
            ('Science HD', 'view/68871/Science-(HD)', 'https://i.vimeocdn.com/video/463315264_1280x720.jpg'),
            ('Showtime HD', 'view/44126/Showtime-(HD)', 'https://www.sho.com/site/image-bin/images/0_0_0/0_0_0_prm-ogsho_1280x640.jpg'),
            ('Starz HD', 'view/76705/StarZ-(SD)', 'https://images-na.ssl-images-amazon.com/images/I/81RgWpOGZLL._SY355_.png'),
            ('Starz SD', 'view/76705/StarZ-(SD)', 'https://images-na.ssl-images-amazon.com/images/I/81RgWpOGZLL._SY355_.png'),
            ('Syfy HD', 'view/46454/Syfy-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Syfy.png?raw=true'),
            ('Syfy SD', 'view/76694/Syfy-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Syfy.png?raw=true'),
            ('TBS HD', 'view/77066/TBS-(HD)', 'https://www.underconsideration.com/brandnew/archives/tbs_2015_logo_detail.png'),
            ('TBS SD', 'view/76695/TBS-(SD)', 'https://www.underconsideration.com/brandnew/archives/tbs_2015_logo_detail.png'),
            ('TNT HD', 'view/57973/TNT-(HD)', 'https://www.broadcastingcable.com/.image/t_share/MTU3MjM4MTk0MDkyMzg1NjA2/tnt_resized_bc.jpg'),
            ('TNT SD', 'view/69020/TNT-(SD)', 'https://www.broadcastingcable.com/.image/t_share/MTU3MjM4MTk0MDkyMzg1NjA2/tnt_resized_bc.jpg'),
            ('TLC HD', 'view/69109/TLC-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TLC.png?raw=true'),
            ('TLC SD', 'view/76671/TLC-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TLC.png?raw=true'),
            ('Travel channel HD', 'view/65833/Travel-channel-(HD)', 'http://thebrandusa.info/enews/wp-content/uploads/sites/12/2015/08/travel_channel_logo.jpg'),
            ('TruTV HD', 'view/52755/TruTV-(HD)', 'https://pmcvariety.files.wordpress.com/2014/07/trutv-logo.jpg?w=1000'),
            ('TV Land HD', 'view/49252/TVLand-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TV%20Land.png?raw=true'),
            ('TV Land SD', 'view/76697/TVland-(SD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TV%20Land.png?raw=true'),
            ('Universo HD', 'view/47844/Universo-(HD)', 'https://www.multichannel.com/.image/t_share/MTU0MDY0OTM5NjQ5NjA2NzM4/nbcuniversojpg.jpg'),
            ('Universal Kids HD', 'view/76713/Universal-Kids', 'http://www.animationxpress.com/wp-content/uploads/2019/06/Universal-Kids-logo.png'),
            ('USA Network HD', 'view/38768/USA-Network-(HD)', 'https://www.multichannel.com/.image/t_share/MTU0MDY0OTM5NjQ5NjA2NzM4/nbcuniversojpg.jpg'),
            ('VH1 HD', 'view/52988/VH1-(HD)', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/USA%20Network.png?raw=true'),
            ('-----24-7------', '', 'https://fonolo.com/wp-content/uploads/2016/03/A-Guide-to-247-Customer-Service.jpg'),
            ('Bleach', 'view/36820/Bleach-anime-full', 'https://upload.wikimedia.org/wikipedia/en/thumb/7/72/Bleachanime.png/220px-Bleachanime.png'),
            ('Detective Conan', 'view/38223/Detective-Conan-the-movies', 'https://vignette.wikia.nocookie.net/detectivconan/images/a/a2/Characters5.png/revision/latest?cb=20140428232345'),
            ('Dragon Ball', 'view/37044/Dragon-Ball', 'https://m.media-amazon.com/images/M/MV5BMjRlYTYyMDUtOGY5MC00MmFiLTljOTMtM2QzOWZjMWViN2FiL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR7,0,182,268_AL_.jpg'),
            ('Dragon Ball GT', 'view/53105/Dragon-Ball-GT', 'https://img.sharetv.com/shows/standard/dragon_ball_gt.jpg'),
            ('Dragon Ball Z', 'view/40156/Dragon-Balll-Z', 'https://m.media-amazon.com/images/M/MV5BMGMyOThiMGUtYmFmZi00YWM0LWJiM2QtZGMwM2Q2ODE4MzhhXkEyXkFqcGdeQXVyMjc2Nzg5OTQ@._V1_.jpg'),
            ('Friends', 'view/36673/Friends-show', 'https://www.shopyourtv.com/wp-content/uploads/2019/05/friends.jpg'),
            ('House MD', 'view/40783/House-MD', 'https://blog.cyrildason.com/wp-content/uploads/2016/11/House-MD.png'),
            ('King of Queens', 'view/38213/King-of-Queens', 'http://static.tvgcdn.net/feed/1/925/116356925.jpg'),
            ('Jackie Chan', 'view/37002/Jackie-Chan', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmYEhCqEtCQQoaydP_SyFekW2bcWuMM2TK66mxPilV5djQwS2b7Q'),
            ('Jackie Chan movies', 'view/36983/Jackie-Chan-movies', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmYEhCqEtCQQoaydP_SyFekW2bcWuMM2TK66mxPilV5djQwS2b7Q'),
            ('Naruto', 'view/37161/Naruto', 'https://a.wattpad.com/cover/100451910-288-k756864.jpg'),
            ('South Park', 'view/40155/South-Park', 'https://images2.minutemediacdn.com/image/upload/c_crop,h_358,w_640,x_0,y_49/f_auto,q_auto,w_1100/v1555003945/shape/mentalfloss/06804986093.png'),
            ('SuperHero movie channel', 'view/38366/SuperHero-movie-channel', 'https://qph.fs.quoracdn.net/main-qimg-24d02d403ce4a1947cac37f51003e620.webp'),
            ('That\'s 70 show', 'view/38217/That\'s-70-show', 'https://m.media-amazon.com/images/M/MV5BN2RkZGE0MjAtZGVkOS00MzVhLTg0OWItZTc4OGRjOTQ1ZTM4XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg'),
            ('The Office', 'view/40750/The-Office-(Show)', 'https://m.media-amazon.com/images/M/MV5BMTgzNjAzMDE0NF5BMl5BanBnXkFtZTcwNTEyMzM3OA@@._V1_.jpg')
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
