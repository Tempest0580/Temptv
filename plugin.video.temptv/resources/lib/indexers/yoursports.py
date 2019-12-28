# -*- coding: utf-8 -*-
# --[ YourSports v1.0 ]--|--[ From JewBMX & Tempest ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib, base64
from resources.lib.modules import client
from resources.lib.modules import control


class yoursports:
    def __init__(self):
        self.list = []
        self.base_link = 'http://yoursports.stream'
        self.uAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        self.headers = {'User-Agent': self.uAgent, 'Referer': self.base_link}

    def root(self):
        channels = [
            ('ACC NETWORK', '/ing/acc', 'https://cdn1.thecomeback.com/wp-content/uploads/sites/94/2016/07/acc_network.png'),
            ('AD SPORTS 1', '/ing/adsport1', 'http://www.1arablive.com/livetv/assets/images/1547480380.png'),
            ('AD SPORTS 2', '/ing/adsport2', 'http://iq.heytv.org/wp-content/uploads/2019/03/abu_dhabi_sports2.jpg'),
            ('ALLSPORTS BRAZIL', '/ing/allsports', 'https://pbs.twimg.com/profile_images/3690961964/ff37e12cddfacc82ce8db02fe00ff476.jpeg'),
            ('ARAGÓN DEPORTE', '/ing/tvx2?ch=aragondep', 'https://pbs.twimg.com/profile_images/1042751187991388160/lOzXBeJ3_400x400.jpg'),
            ('ASTRAKHAN SPORTS', '/ing/tvx2?ch=astrasport', 'https://www.freevector.com/uploads/vector/preview/11361/FreeVector-Volgar-Gazprom-Astrakhan.jpg'),
            ('ATG SPORT', '/ing/atgsport', 'https://mark.trademarkia.com/logo-images/aktiebolaget-trav-och-galopp/atg-sport-88139845.jpg'),
            ('BAHRAIN SPORTS', '/ing/bahrainsports', 'https://www.albawaba.com/sites/default/files/styles/default/public/im/Sport/bahrain_sport_day.png?itok=6abbxakq'),
            ('BETIS TV', '/ing/betistv', 'http://www.dealood.com/content/uploads/images/July2019/031a89fb932fc4501cfc67691ccb6f31[1]-large.jpeg'),
            ('BIG TEN NETWORK (US IP)', '/ing/btn', 'https://pbs.twimg.com/profile_images/992425758940368901/_XC0bfRl_400x400.jpg'),
            ('BOLIVIA DEPORTES', '/ing/boliviadeportes', 'https://4.bp.blogspot.com/-8Iiiwq237lA/WY4ngvRY3bI/AAAAAAAAFGw/YHhyZlgIrB8NK3nG6KQcAhkJtXPtTYB8QCLcBGAs/s1600/Canal-Bolivia-TV-Deportes.jpg'),
            ('CBS SPORTS HQ', '/ing/cdss', 'http://content.sportslogos.net/news/2015/11/cbs-sports-new-logo.jpg'),
            ('CCX SPORTS', '/ing/ccxsports', 'https://pbs.twimg.com/profile_images/809859306954723328/ldxBUVVT.jpg'),
            ('CDO DEPORTES', '/ing/cdodeportes', 'https://1.bp.blogspot.com/-VqTF4cSp34k/XCuUsIL3lgI/AAAAAAAACSQ/nAkBo6c_OhoZXCuIoo9vOwbqu6ycYrrGACLcBGAs/w640/cdo-tv.jpg'),
            ('COMBAT GO (US IP)', '/ing/po?ch=combatgo', 'https://static-cdn.jtvnw.net/jtv_user_pictures/39fa914d-0f72-418b-8966-f672d6b103e7-profile_image-300x300.png'),
            ('DUBAI RACING', '/ing/dubairacing', 'https://pbs.twimg.com/profile_images/993899145990729730/wifDLmuI_400x400.jpg'),
            ('ELEVEN SPORTS', '/ing/c?ch=eleven', 'https://upload.wikimedia.org/wikipedia/commons/4/49/Eleven_Sports.png'),
            ('ESPN', '/ing/espn', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('ESPN 2', '/ing/espn2', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ESPN.png?raw=true'),
            ('ESPN DEPORTES', '/ing/espndep', 'https://espnpressroom.com/us/files/2016/03/RS1129_ESPN_Deportes_CLR_Pos-scr-1-850x610.jpg'),
            ('ESPN LONGHORN', '/ing/lhn', 'https://texassports.com/images/2013/7/29/longhorn-network-1000x540.jpg?width=1128&height=635&mode=crop'),
            ('ESPN NEWS', '/ing/espnnews', 'https://upload.wikimedia.org/wikipedia/commons/3/31/Espnnews.png'),
            ('ESPN U', '/ing/espnu', 'http://p-img.movetv.com/cms/images/a5e621a17fba73a2dd3f8c0304168aebc9253dd4.jpg'),
            ('FC BAYERN TV', '/ing/tvx2?ch=fcbayern', 'https://mir-s3-cdn-cf.behance.net/projects/max_808/ff680059072721.Y3JvcCwxODM2LDE0MzcsMzU4LDA.jpg'),
            ('FIGHT TIME', '/ing/tvx2?ch=fighttime', 'https://image.winudf.com/v2/image/ZXMud2lmaWJhbGVhcmVzLmZpZ2h0dGltZV9zY3JlZW5fMF91eHdzZ3FmZA/screen-0.jpg?fakeurl=1&type=.jpg'),
            ('Fox Sports 1 (US IP)', '/ing/fs1', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/2015_Fox_Sports_1_logo.svg/400px-2015_Fox_Sports_1_logo.svg.png'),
            ('Fox Sports 2 (US IP)', '/ing/fs2', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/FS2_logo_2015.svg/400px-FS2_logo_2015.svg.png'),
            ('FOX SPORTS DEPORTES', '/ing/fsdeportes', 'https://www.pngkey.com/png/detail/297-2976406_fox-deportes-fox-sports-australia-logo.png'),
            ('FOX SPORTS NEWS', '/ing/fsnews', 'http://store-images.s-microsoft.com/image/apps.64293.9007199267003755.bfdca1b8-de6f-4813-a156-c79a99c7ef99.5aaea734-f974-4c58-a6a7-a9c726e668c9'),
            ('FUBO SPORTS NETWORK', '/ing/fubosports', 'https://pmcvariety.files.wordpress.com/2019/06/fubo-sports-network-logo-dark.jpg?w=1000&h=563&crop=1'),
            ('GOL TV', '/ing/goltv', 'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/0018/1156/brand.gif?itok=D3YVqhZv'),
            ('GOLF CHANNEL', '/ing/golf', 'https://www.golfchannel.com/sites/default/files/new_golf_channel_logo_304.jpg'),
            ('HUNT TV', '/ing/hunt', 'https://image.roku.com/developer_channels/prod/fd7432e5c8bd6ecc41ce279e009393baa2515bcb4e5d819c6e9770a16b4dce6b.png'),
            ('JORDAN SPORTS TV', '/ing/jordansport', 'https://i.pinimg.com/originals/b9/0f/cf/b90fcf3e80f61ead382bd2106d933d4b.jpg'),
            ('KTV SPORTS: KUWAIT', '/ing/ktvsports', 'https://content.osn.com/bob/745x419/KTS.jpg'),
            ('LACROSSE NETWORK', '/ing/c?ch=lacrosse', 'https://yt3.ggpht.com/a/AGF-l79fL2RBHZvBXAOOSegaVhZNytK6ESlCWBf4=s900-c-k-c0xffffffff-no-rj-mo'),
            ('MLB Network', '/ing/mlbn', 'https://upload.wikimedia.org/wikipedia/en/thumb/a/ac/MLBNetworkLogo.svg/280px-MLBNetworkLogo.svg.png'),
            ('MY SPORTS 1', '/ing/mysports', 'https://i1.wp.com/www.broadbandtvnews.com/wp-content/uploads/2018/08/MySports-One.jpg?resize=900%2C362&ssl=1'),
            ('NBCS BAY (US IP)', '/ing/nbcbay', 'https://www.nbcsports.com/bayarea/sites/csnbayarea/files/nbc-sports-ba-logo.jpg'),
            ('NBCS BOS (US IP)', '/ing/nbcne', 'https://pbs.twimg.com/profile_images/930117519729405963/5p6FvPDM_400x400.jpg'),
            ('NBCS CA (US IP)', '/ing/nbcca', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcvi-H5W0S35TfU5PCsVPSyYe1DtCchsHcjLTrWuYWSbcAebMx&s'),
            ('NBCS NW (US IP)', '/ing/nbcnw', 'https://pbs.twimg.com/profile_images/929758074012778496/hWSKZmVV.jpg'),
            ('NESN (US IP)', '/ing/nesn', 'https://nesn.com/wp-content/uploads/2019/10/webp.net-resizeimage.jpg'),
            ('NESN PLUS (US IP)', '/ing/nesnplus', 'https://nesn.com/wp-content/uploads/2013/03/nesnplus-white.png'),
            ('OLYMPIC Channel', '/ing/olympic', 'https://images-na.ssl-images-amazon.com/images/I/517OUKvP9kL._SX450_.png'),
            ('OLYMPIC Channel 2', '/ing/olympic2', 'https://images-na.ssl-images-amazon.com/images/I/517OUKvP9kL._SX450_.png'),
            ('OLYMPIC Channel 3', '/ing/olympic3', 'https://images-na.ssl-images-amazon.com/images/I/517OUKvP9kL._SX450_.png'),
            ('OLYMPIC Channel 4', '/ing/olympic3', 'https://images-na.ssl-images-amazon.com/images/I/517OUKvP9kL._SX450_.png'),
            ('OLYMPIC Channel 4', '/ing/olympic4', 'https://images-na.ssl-images-amazon.com/images/I/517OUKvP9kL._SX450_.png'),
            ('OLYMPIC Channel 5', '/ing/olympic5', 'https://images-na.ssl-images-amazon.com/images/I/517OUKvP9kL._SX450_.png'),
            ('OLYMPIC Channel 6', '/ing/olympic6', 'https://images-na.ssl-images-amazon.com/images/I/517OUKvP9kL._SX450_.png'),
            ('OMAN SPORTS', '/ing/omansports', 'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/0003/8031/brand.gif?itok=4Y7BHIC0'),
            ('ONE GOLF', '/ing/tvx2?ch=onegolf', 'http://onegolftv.com/wp-content/uploads/2018/08/onegolf-HD-oneline-01b.jpg'),
            ('PAC-12 PLUS', '/ing/tvx2?ch=pac12plus', 'https://pbs.twimg.com/profile_images/784137001633132545/e-Muo-mT.jpg'),
            ('RACING.COM', '/player.php?stream=NatGEO', 'https://www.mckentracing.com.au/assets/images/kent/link/9.png?b=190411144'),
            ('REAL MADRID TV', '/ing/realmadridtv', 'https://www.realmadrid.com/StaticFiles/RealMadridResponsive/images/static/realmadridtv.jpg'),
            ('RED BULL TV', '/ing/redbull', 'https://www.red24management.com/wp-content/uploads/2016/10/Becky-Ives-Red-Bull-TV.jpg'),
            ('RTV SPORT: SAN MARINO', '/ing/rtvsport', 'https://www.sanmarinortv.sm/assets/frontend/img/logo-1200-630.png?v26'),
            ('SEC NETWORK', '/ing/sec', 'https://www.multichannel.com/.image/t_share/MTU0MDY0OTQ4Nzc2NzQwNjAz/sec-network-logojpg.jpg'),
            ('SHARJAH SPORT', '/ing/sharjahsport', 'https://i.pinimg.com/736x/e8/ee/54/e8ee5423590f763acf97bf1d33564510.jpg'),
            ('SPORT 1 | LT', '/ing/tvx2?ch=sport1', 'https://mobilbranche.de/wp-content/uploads/2016/06/Sport1.jpg'),
            ('SPORT TVL', '/ing/tvx2?ch=sporttvl', 'https://pbs.twimg.com/profile_images/717091382930907136/H6FFxZqV_400x400.jpg'),
            ('SPORTACENTRS | LV', '/ing/sportacentrs', 'http://i.tiesraides.lv/1200x0s/pictures/2018-05-10/2018-05-10_2010_10_12_sportacentrs_logo_jpg.jpg'),
            ('STADIUM SPORTS', '/ing/stadium', 'https://s23455.pcdn.co/wp-content/uploads/2018/08/stadium-logo-640.jpeg'),
            ('SWISS SPORT TV', '/ing/tvx2?ch=swisssport', 'https://www.lg-obersee.ch/files/1_Oberseemeeting/Swiss-sport.tv.jpg'),
            ('TELEROMAGNA SPORT', '/ing/teleromagna', 'http://www.logotypes101.com/logos/443/EFC2A76D44994B5CA76D72FECF6A7325/logotrcolori.png'),
            ('Tennis Channel', '/ing/tennis', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Tennis_Channel_logo.svg/220px-Tennis_Channel_logo.svg.png'),
            ('TENNIS CHANNEL: THE T', '/ing/thet', 'https://www.multichannel.com/.image/t_share/MTU0MDYzODk5MTkxMjg4OTE0/tennis-channel-logo-400x300jpg.jpg'),
            ('TENNIS PLUS 1', '/ing/tennisplus?g=1', 'https://mark.trademarkia.com/logo-images/the-tennis-channel/t-tennis-channel-plus-86418209.jpg'),
            ('TENNIS PLUS 2', '/ing/tennisplus?g=2', 'https://mark.trademarkia.com/logo-images/the-tennis-channel/t-tennis-channel-plus-86418209.jpg'),
            ('TILESPORT GREECE', '/ing/tilesport', 'https://i.ytimg.com/vi/1zfBm0bw5NQ/maxresdefault.jpg'),
            ('TJK TV', '/ing/tjktv', 'https://i.pinimg.com/474x/36/5d/a8/365da80d63c27951d62265523500f921.jpg'),
            ('TRACE SPORTS STARS', '/ing/tvx2?ch=tracesports', 'https://i.ytimg.com/vi/E6Mz782vW9Q/maxresdefault.jpg'),
            ('TV PLAY SPORTS', '/ing/tvx2?ch=tvplaysport', 'https://www.cgates.lt/wp-content/uploads/2017/10/logo-tvplay-sports.png'),
            ('TÜRKMEN SPORTS', '/ing/turkmensports', 'https://i.ytimg.com/vi/wr-C4gFczLo/hqdefault.jpg'),
            ('XCORP TV', '/ing/xcorps', 'https://images.all-free-download.com/images/graphiclarge/x_corp_143718.jpg'),
            ('ABC', '/ing/abc', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/ABC.png?raw=true'),
            ('ABC NEWS', '/ing/abcnews', 'https://i.imgur.com/V8eTp2V.png'),
            ('AL JAZEERA', '/ing/aljazeera', 'http://www.egypttoday.com/images/larg/13842.jpg'),
            ('ATLANTA TV', '/ing/atlanta', 'https://fontmeme.com/images/ATLANTA-SET-IN-CABERNET-FONT.png'),
            ('BBC America', '/ing/tvx2?ch=bbc', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/BBC%20America.png?raw=true'),
            ('BET', '/ing/bet', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Bet.png?raw=true'),
            ('Boomerang ASIA', '/ing/bloomAsia', 'https://pbs.twimg.com/profile_images/778129630284902401/gXjFkqGM.jpg'),
            ('Boomerang AUSTRALIA', '/ing/bloomAus', 'https://pbs.twimg.com/profile_images/768354336103600128/AktQ5A17.jpg'),
            ('Boomerang EUROPE', '/ing/bloomEur', 'https://live-tv-channels.org/pt-data/uploads/logo/us-bloomberg-tv-europe.jpg'),
            ('Boomerang USA', '/ing/bloomUsa', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Boomerang.png?raw=true'),
            ('My TV BUFFALO', '/ing/buffalo', 'https://upload.wikimedia.org/wikipedia/en/d/d0/Wnyo_mntv.PNG'),
            ('BUZZR', '/ing/buzzr', 'https://i.vimeocdn.com/video/556352061.webp?mw=1000&mh=562&q=70'),
            ('Cartoon Network', '/ing/tvx2?ch=cartoonnet', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Cartoon%20Network.png?raw=true'),
            ('CBS', '/ing/cbs', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CBS.png?raw=true'),
            ('CBS NEWS', '/ing/cbsn', 'https://religionnews.com/wp-content/uploads/2019/04/webRNS-CBS_News_logo1-040519.jpg'),
            ('CHEDDAR', '/ing/cheddar', 'https://www.multichannel.com/.image/t_share/MTU1MDE1MDczNjU0NDQ5Mjcw/cheddar-logo-16x9.png'),
            ('CHEDDAR BIG NEWS', '/ing/cheddarnews', 'https://talkingbiznews.com/wp-content/uploads/2018/04/Screen-Shot-2018-04-17-at-5.38.40-PM-300x272.png'),
            ('Classic Arts', '/ing/tvx2?ch=classicarts', 'https://pbs.twimg.com/profile_images/708574672888135680/reNxGF3z_400x400.jpg'),
            ('CMC', '/ing/cmc', 'http://www.vector-logo.net/logo_preview/ai/c/CMC_LOGO.png'),
            ('CMT', '/ing/cmt', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CMT%20Films.png?raw=true'),
            ('CNBC', '/ping/cnbc', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNBC.png?raw=true'),
            ('CNN', '/ing/cnnnews', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/CNN.png?raw=true'),
            ('Comedy Central', '/ing/comedycentral', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Comedy%20Central.png?raw=true'),
            ('CON TV', '/ing/contv', 'https://pbs.twimg.com/profile_images/1044272252072521728/IWUQk2nK_400x400.jpg'),
            ('CSPAN', '/ing/cspan1', 'https://www.underconsideration.com/brandnew/archives/c_span_logo.png'),
            ('CSPAN 2', '/ing/cspan2', 'http://allvectorlogo.com/img/2016/07/c-span-2-logo.png'),
            ('CSPAN 3', '/ing/cspan3', 'http://oklivetv.com/wp-content/uploads/media/6c7ca884ba0edeabbb7dcf7b264ac8e2.jpeg'),
            ('Disney Channel', '/ing/tvx2?ch=disneychannel', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Disney%20Channel.png?raw=true'),
            ('Documentaries', '/ing/documentary', 'https://images-platform.99static.com/fQD1-6iYPBe3x1rzBnNHZUutz54=/500x500/top/smart/99designs-contests-attachments/24/24032/attachment_24032543'),
            ('Docurama', '/ing/docurama', 'https://www.juancarlosvazquez.com/wp-content/uploads/2016/12/50_Logos-22.jpg'),
            ('DW News', '/ing/dwnews', 'http://db.radioline.fr/pictures/radio_05461441af82e70f5c4bf24dd3961b18/logo200.jpg?size=200'),
            ('FailArmy', '/ing/tvx2?ch=failarmy', 'https://vignette.wikia.nocookie.net/logopedia/images/c/c8/FailArmy_logo_.jpg/revision/latest/scale-to-width-down/340?cb=20150126211049'),
            ('Film Detective', '/ing/filmdetective', 'https://nscreenmedia.com/wp-content/uploads/The-Film-Detective-logo.png'),
            ('Fox', '/ing/fox', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FOX.png?raw=true'),
            ('Fox Business', '/ing/foxbusiness', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Fox_Business.svg/420px-Fox_Business.svg.png'),
            ('Fox News', '/ing/foxnews', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/300px-Fox_News_Channel_logo.svg.png'),
            ('FX', '/ing/fx', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FX.png?raw=true'),
            ('FXX', '/ing/fxx', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/FXX.png?raw=true'),
            ('Garage TV', '/ing/garagetv', 'https://www.pngkey.com/png/detail/139-1393003_el-garage-tv-garage-tv-logo.png'),
            ('History 2', '/ing/history2', 'https://assets.change.org/photos/3/nl/bo/KNnLbOykNAOPeaR-400x400-noPad.jpg?1527644200'),
            ('House Channel', '/ing/HORnews', 'http://hcfama.org/sites/default/files/state_house_banner_1.png'),
            ('InfoWars', '/ing/infowars', 'http://www.infowarsshop.com/assets/images/infowarssquaresticker2.jpg'),
            ('David Knight', '/ing/infowardk', 'https://avatars.brighteon.com/d7cf4433-f647-409f-8529-caaaf63f0475'),
            ('Law And Crime', '/ing/lawandcrime', 'https://image.xumo.com/v1/channels/channel/9999320/248x140.png?type=channelTile'),
            ('MSNBC', '/ing/msnbcnews', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MSNBC.png?raw=true'),
            ('MTV', '/ing/mtv', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/MTV.png?raw=true'),
            ('MTV Hts', '/ing/tvx2?ch=mtvhits', 'https://pbs.twimg.com/profile_images/1813177034/mtv-hits_400x400.gif'),
            ('Nat Geo People', '/ing/natgeopeople', 'https://i0.wp.com/unifistreamyx.info/wp-content/uploads/2015/07/NatGeo_People_logo-628x353.gif'),
            ('Nat Geo Wild', '/ing/natgeowild', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Nat%20Geo%20Wild.png?raw=true'),
            ('National Geographic', '/ing/natgeo', 'https://blog.nationalgeographic.org/wp-content/uploads/2019/08/NG_Logo-1140x450.jpg'),
            ('Nature Vision', '/ing/po?ch=naturevision', 'https://www.ses.com/sites/default/files/styles/card/public/2018-01/Nature%20Vision%20Logo_1.png?itok=LGdA3q_m'),
            ('NBC', '/ing/nbc', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/NBC.png?raw=true'),
            ('News Net', '/ing/newsnet', 'https://yournewsnet.com/wp-content/uploads/2017/12/Newsnet-sm-1.jpg'),
            ('NewsMax Tv', '/ing/newsmax', 'https://www.multichannel.com/.image/t_share/MTU0MDYzODE1OTgwOTUxMjkx/newsmax-logojpg.jpg'),
            ('NEWSY', '/ing/newsy', 'https://www.multichannel.com/.image/t_share/MTYzOTI5MDY4NjI5MTQxMzI5/newsy-logo.jpg'),
            ('Paramont Network', '/ing/paramount', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/Paramount%20Network.png?raw=true'),
            ('PBS Kids', '/ing/pbskids', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/PBS%20Kids.png?raw=true'),
            ('PBS Kids 2', '/ing/pbskids2', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/PBS%20Kids.png?raw=true'),
            ('PeopleTV', '/ing/po?ch=peopletv', 'https://www.multichannel.com/.image/t_share/MTU0MDYzODE4MTI3MDU4Njgz/peopletv-logojpg.jpg'),
            ('Rai Movie', '/ing/raimovie', 'https://assets.change.org/photos/5/ma/it/jEmaIThYleWiRzS-400x225-noPad.jpg?1555167327'),
            ('RetroTV', '/ing/retrotv', 'https://cdn5.vectorstock.com/i/1000x1000/56/64/retro-tv-logo-design-flat-icon-vector-8035664.jpg'),
            ('RT AMERICA', '/ing/rtusanews', 'https://pbs.twimg.com/profile_images/1167911174/logo_RTamerica_white.jpg'),
            ('SCREAMFEST', '/ing/screamfest', 'https://i0.wp.com/thehorrorsyndicate.com/wp-content/uploads/2016/10/FEA-3.png?fit=610%2C345'),
            ('SKY NEWS', '/ing/skynews', 'https://news.sky.com/resources/sky-news-logo.png?v=1?bypass-service-worker'),
            ('The Shopping Channel', '/ing/qvc', 'http://dawnchubai.com/wordpress/wp-content/uploads/2017/04/TSC_Logo_Primary_SM_RGB-21.jpg'),
            ('TRAVEL RU HD', '/ing/travelhd', 'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/072019/rtghd_black.png?JCDSZI8rtT8MeNPq19TuLcTri027PfFI&itok=hvTZhW7Q'),
            ('Tv Land', '/ing/tvland', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/TV%20Land.png?raw=true'),
            ('VH1', '/ing/tvx2?ch=vh1', 'https://github.com/jewbmx/resource.images.studios.white/blob/master/resources/VH1.png?raw=true'),
            ('Viasat Explorer', '/ing/tvx2?ch=vexplorer', 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Viasat_Explore_Logo.jpg'),
            ('Viasat History', '/ing/tvx2?ch=vhistory', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Viasat_History_Logo.jpg/1200px-Viasat_History_Logo.jpg'),
            ('Viasat Nature', '/ing/tvx2?ch=vnature', 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Viasat_Nature_Logo.jpg'),
            ('Washington Post Live', '/ing/tvx2?ch=wpnews', 'https://pbs.twimg.com/profile_images/785948379041918977/2-arwrVt.jpg'),
            ('Weather Nation', '/ing/weathernation', 'https://is4-ssl.mzstatic.com/image/thumb/Purple123/v4/4f/ae/54/4fae5431-6273-6d15-930f-a216d1d1f02c/AppIcon-0-1x_U007emarketing-0-0-85-220-0-7.png/1200x630wa.png'),
            ('WGN9', '/ing/wgn', 'https://tribwgntv.files.wordpress.com/2019/01/wgnnewlogo.jpg?quality=85&strip=all'),
            ('WHDH 7 BOSTON', '/ing/cwboston', 'https://i.ytimg.com/vi/gejwOB2luO8/hqdefault.jpg')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base_link + channel[1], 'image': channel[2], 'action': 'yoursportsPlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            stream = client.request(url)
            try:
                link = re.compile('var mustave = atob\((.+?)\)').findall(stream)[0]
            except:
                link = re.compile('<iframe frameborder=0 height=100% width=100% src="(.+?php)"', re.DOTALL).findall(stream)[0]
                link = client.request(link)
                link = re.compile('var mustave = atob\((.+?)\)').findall(link)[0]
            link = base64.b64decode(link)
            if link.startswith('/'):
                link = self.base_link + link
            link = '%s|User-Agent=%s&Referer=%s' % (link, self.uAgent, url)
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
