# -*- coding: UTF-8 -*-

import re, os, sys, urllib, urllib2, requests, socket, gzip
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import userlists
import shows
Addon = xbmcaddon.Addon
AddonInfo = Addon().getAddonInfo
AddonID = AddonInfo('id')
AddonIcon = AddonInfo('icon')
AddonFanArt = AddonInfo('fanart')
addon = xbmcaddon.Addon(id=AddonID)
profileDir = addon.getAddonInfo('profile')
profileDir = xbmc.translatePath(profileDir).decode("utf-8")
if not os.path.exists(profileDir):
    os.makedirs(profileDir)
cookiePath = os.path.join(profileDir, 'cookies.lwp')
addon_handle = int(sys.argv[1])
socket.setdefaulttimeout(10)
urlopen = urllib2.urlopen
Request = urllib2.Request
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent': USER_AGENT, 'Accept': '*/*', 'Connection': 'keep-alive'}
adult = addon.getSetting('Show_Adult')
dev = addon.getSetting('Dev')


def MAIN():
    addDir('Entertainment', userlists.english, 2, 'https://i2.wp.com/www.somersetcounty4h.org/wp-content/uploads/entertainment-icon.png?fit=567%2C567')
    addDir('Movies', userlists.movies, 2, 'https://d1nhio0ox7pgb.cloudfront.net/_img/o_collection_png/green_dark_grey/256x256/plain/movies.png')
    addDir('Kids', userlists.kids, 2, 'https://yt3.ggpht.com/a/AGF-l7-eRsuCOQ43Hj9WVVU1xGY2L6sgA8S1DZLM2w=s900-mo-c-c0xffffffff-rj-k-no')
    addDir('Sports', userlists.sports, 2, 'https://images.all-free-download.com/images/graphicthumb/free_sport_vector_pack_557881.jpg')
    addDir('News', userlists.news, 2, 'https://esemag.com/wp-content/uploads/2015/11/News-Items.jpg')
    addDir('Music', userlists.music, 2, 'https://c8.alamy.com/comp/PE2FM5/vector-cartoon-music-icon-in-comic-style-sound-note-sign-illustration-pictogram-melody-music-business-splash-effect-concept-PE2FM5.jpg')
    addDir('24/7', userlists.hour24, 2, 'https://depo8.com/wp-content/uploads/2014/07/24-7-icon.png')
    addDir('1 Click Movies', '', 7, 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/c72e2f68-1a1c-48a2-aa5f-edf7eaaf3548/d704h5l-8e40963d-18aa-4982-a412-5c0ef52f6acf.png')
    addDir('1 Click Shows', '', 11, 'http://chittagongit.com/images/tv-series-icon/tv-series-icon-15.jpg')
    addDir('In Theaters', userlists.theater, 2, 'http://mytnnews.com/wp-content/uploads/2012/06/now-in-theaters.jpg')
    addDir('Pluto TV', userlists.pluto, 2, 'https://images-na.ssl-images-amazon.com/images/I/519H2haYtzL._SY355_.png')
    #addDir('On Demand Movies', '', 12, AddonIcon)
    #addDir('On Demand Shows', '', 13, AddonIcon)
    addDir('Foreign Channels', '', 22, AddonIcon)
    if adult == 'true':
        addDir('Adult\'s Only', userlists.adult, 2, 'https://previews.123rf.com/images/123vector/123vector1403/123vector140300027/26460698-vector-illustration-of-red-adult-icon-on-white-background.jpg')
    if dev == 'true':
        addDir('Testing', '', 5, 'http://icons.iconarchive.com/icons/aaron-sinuhe/series-season-folder/256/extras-icon.png')
    addDir('[B] Settings [/B]', 'url', 4, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyhtqOw2iVU3-nBZMb1cWTDw_bsR4dkNtLvSkqQn3jsApD1A3', Folder=False)
    addDir('Refresh', '', 6, 'https://maxcdn.icons8.com/app/uploads/2016/11/refresh1.png', Folder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def VOD_MOVIES():
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def VOD_SHOWS():
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK_SHOWS():
    addDir('Ballers', '', 20, 'https://m.media-amazon.com/images/M/MV5BNTIzMDk3Mzc4Nl5BMl5BanBnXkFtZTgwODExNDAwNjM@._V1_.jpg')
    addDir('Family Guy', '', 15, 'https://m.media-amazon.com/images/M/MV5BODEwZjEzMjAtNjQxMy00Yjc4LWFlMDAtYjhjZTAxNDU3OTg3XkEyXkFqcGdeQXVyOTM2NTM4MjA@._V1_.jpg')
    addDir('House MD', '', 19, 'https://blog.cyrildason.com/wp-content/uploads/2016/11/House-MD.png')
    addDir('Izombie', '', 21, 'https://images-na.ssl-images-amazon.com/images/I/51msaPPK-sL._SY445_.jpg')
    addDir('Smallville', '', 14, 'https://m.media-amazon.com/images/M/MV5BYmNiNzlhOWItMDM5Mi00MGYzLWI1ZDYtNmI5NzI0MWFkMTIwXkEyXkFqcGdeQXVyNjU2NjA5NjM@._V1_.jpg')
    # addDir('Anger Managment', userlists.angermanagment, 2, 'https://i1.wp.com/hitenism.com/wp-content/uploads/Fotolia_61714948_L.jpg?ssl=1')
    addDir('Stargate SG1', '', 18, 'https://cdn1us.denofgeek.com/sites/denofgeekus/files/styles/main_wide/public/stargate_sg-1_cast.jpg?itok=EucgrKA3')
    addDir('Supernatural', '', 17, 'https://cdn1us.denofgeek.com/sites/denofgeekus/files/styles/main_wide/public/supernatural_season_12_poster.jpg?itok=ocBbj_o5')
    addDir('The Simpsons', '', 16, 'https://m.media-amazon.com/images/M/MV5BYjFkMTlkYWUtZWFhNy00M2FmLThiOTYtYTRiYjVlZWYxNmJkXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    # addDir('', '', 20, '')


def CLICK_4k():
    addDir('2019', userlists.click_4k_2019, 2, AddonIcon)
    addDir('2018', userlists.click_4k_2018, 2, AddonIcon)
    addDir('2017', userlists.click_4k_2017, 2, AddonIcon)
    addDir('2016', userlists.click_4k_2017, 2, AddonIcon)
    addDir('2015', userlists.click_4k_2017, 2, AddonIcon)
    addDir('2014', userlists.click_4k_2017, 2, AddonIcon)
    addDir('1995', userlists.click_4k_1995, 2, AddonIcon)
    addDir('1993', userlists.click_4k_1993, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK_1080():
    addDir('2019', userlists.click_1080p_2019, 2, AddonIcon)
    addDir('2018', userlists.click_1080p_2018, 2, AddonIcon)
    addDir('2017', userlists.click_1080p_2017, 2, AddonIcon)
    addDir('2016', userlists.click_1080p_2016, 2, AddonIcon)
    addDir('2015', userlists.click_1080p_2015, 2, AddonIcon)
    addDir('2013', userlists.click_1080p_2013, 2, AddonIcon)
    addDir('2012', userlists.click_1080p_2012, 2, AddonIcon)
    addDir('2011', userlists.click_1080p_2011, 2, AddonIcon)
    addDir('1991', userlists.click_1080p_1991, 2, AddonIcon)
    addDir('1982', userlists.click_1080p_1982, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK_720():
    addDir('2019', userlists.click_720_2019, 2, AddonIcon)
    addDir('2018', userlists.click_720_2018, 2, AddonIcon)
    addDir('2016', userlists.click_720_2016, 2, AddonIcon)
    addDir('2014', userlists.click_720_2014, 2, AddonIcon)
    addDir('2002', userlists.click_720_2002, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK():
    addDir('4K', '', 8, 'https://sitejerk.com/images/4k-png-14.png')
    addDir('1080p', '', 9, 'https://image.flaticon.com/icons/png/512/68/68922.png')
    addDir('720p', '', 10, 'https://image.flaticon.com/icons/png/512/974/974576.png')
    addDir('Kids Movies', userlists.kids_movies, 2, 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/90s-kids-movies-1553540981.jpg')
    addDir('3D Movies', userlists.iiid_movies, 2, 'https://cdn01.vulcanpost.com/wp-uploads/2014/09/3d_pardaphash.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def MORELISTS():
    addDir('Testing - Test for 24-48Hrs before adding to Main Lists', userlists.testing, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def FOREIGN():
    addDir('Afghanistan', userlists.Afghanistan, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Afghanistan.svg/2000px-Flag_of_Afghanistan.svg.png')
    addDir('Albania', userlists.Albania, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/2000px-Flag_of_Albania.svg.png')
    addDir('Algeria', userlists.Algeria, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Algeria.svg/2000px-Flag_of_Algeria.svg.png')
    addDir('Argentina', userlists.Argentina, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/2000px-Flag_of_Argentina.svg.png')
    addDir('Armenia', userlists.Armenia, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Flag_of_Armenia.svg/2000px-Flag_of_Armenia.svg.png')
    addDir('Australia', userlists.Australia, 2, 'https://upload.wikimedia.org/wikipedia/commons/8/88/Flag_of_Australia_%28converted%29.svg')
    addDir('Austria', userlists.Austria, 2, 'https://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_Austria.svg')
    addDir('Azerbaijan', userlists.Azerbaijan, 2, 'https://upload.wikimedia.org/wikipedia/commons/d/dd/Flag_of_Azerbaijan.svg')
    addDir('Bahrain', userlists.Bahrain, 2, 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Bahrain.svg')
    addDir('Bangladesh', userlists.Bangladesh, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag_of_Bangladesh.svg/2000px-Flag_of_Bangladesh.svg.png')
    addDir('Barbados', userlists.Barbados, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Flag_of_Barbados.svg/2000px-Flag_of_Barbados.svg.png')
    addDir('Belarus', userlists.Belarus, 2, 'https://upload.wikimedia.org/wikipedia/commons/8/85/Flag_of_Belarus.svg')
    addDir('Belgium', userlists.Belgium, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Belgium.svg/2000px-Flag_of_Belgium.svg.png')
    addDir('Bolivia', userlists.Bolivia, 2, 'https://upload.wikimedia.org/wikipedia/commons/d/de/Flag_of_Bolivia_%28state%29.svg')
    addDir('Bosnia and Herzegovina', userlists.Bosnia_and_Herzegovina, 2, 'https://upload.wikimedia.org/wikipedia/commons/b/bf/Flag_of_Bosnia_and_Herzegovina.svg')
    addDir('Brazil', userlists.Brazil, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/1280px-Flag_of_Brazil.svg.png')
    addDir('Bulgaria', userlists.Bulgaria, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Bulgaria.svg/2000px-Flag_of_Bulgaria.svg.png')
    addDir('Cambodia', userlists.Cambodia, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Flag_of_Cambodia_vertical.svg/2000px-Flag_of_Cambodia_vertical.svg.png')
    addDir('Canada', userlists.Canada, 2, 'https://upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Canada_%28Pantone%29.svg')
    addDir('Chile', userlists.Chile, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Flag_of_Chile.svg/2000px-Flag_of_Chile.svg.png')
    addDir('China', userlists.China, 2, 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_the_People%27s_Republic_of_China.svg')
    addDir('Colombia', userlists.Colombia, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/255px-Flag_of_Colombia.svg.png')
    addDir('Costa Rica', userlists.Costa_Rica, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Costa_Rica_%28state%29.svg/255px-Flag_of_Costa_Rica_%28state%29.svg.png')
    addDir('Germany', userlists.Germany, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/1280px-Flag_of_Germany.svg.png')
    addDir('India', userlists.India, 2, 'https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg')
    addDir('Indonesia', userlists.Indonesia, 2, 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg')
    addDir('Italy', userlists.Italia, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/255px-Flag_of_Italy.svg.png')
    addDir('Mexico', userlists.Mexico, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/2000px-Flag_of_Mexico.svg.png')
    addDir('Russia', userlists.Russia, 2, 'https://upload.wikimedia.org/wikipedia/en/archive/f/f3/20120812153730%21Flag_of_Russia.svg')
    addDir('Spain', userlists.Spain, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1280px-Flag_of_Spain.svg.png')
    addDir('United Kingdom', userlists.uk, 2, 'https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    # addDir('', '', 2, '')


def REFRESH():
    xbmc.executebuiltin('Container.Refresh')


def addDir(name, url, mode, iconimage, Folder=True):
    if url.startswith('plugin'):
        u = url
    else:
        u = (sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    liz.setArt({'fanart': AddonFanArt})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=Folder)
    return ok


def addPlayLink(name, url, mode, iconimage):
    u = (sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    # liz.setProperty('IsPlayable', 'true')
    liz.setInfo(type="Video", infoLabels={"Title": name})
    video_streaminfo = {'codec': 'h264'}
    liz.addStreamInfo('video', video_streaminfo)
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=False)
    return ok


def getHtml(url, referer=None, hdr=None, data=None):
    if not hdr:
        req = Request(url, data, headers)
    else:
        req = Request(url, data, hdr)
    if referer:
        req.add_header('Referer', referer)
    if data:
        req.add_header('Content-Length', len(data))
    response = urlopen(req, timeout=20)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        f.close()
    else:
        data = response.read()    
    response.close()
    return data


def parsem3u(html):
    match = re.compile('#.+? tvg-logo="(.+?)" .+?",(.+?)\n(.+?)\n').findall(html)
    count = 0
    for channelicon, name, url in match:
        url = url.replace('\r', '')
        addPlayLink(name, url, 3, channelicon)
        count += 1
    return count


def PAGE(url):
    html = getHtml(url)
    iptvlinks = re.compile("=(.+?)=(.+?)=", re.DOTALL | re.IGNORECASE).findall(html)
    for name, link in iptvlinks:
        addDir(name, link, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def LIST(url):
    try:
        m3u = getHtml(url)
        parsem3u(m3u)
    except:
        addDir('Nothing found', '', '', '', Folder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def PLAY(url, title):
    playmode = int(addon.getSetting('playmode'))
    iconimage = xbmc.getInfoImage("ListItem.Thumb")
    if playmode == 0:
        stype = ''
        if '.ts' in url:
            stype = 'TSDOWNLOADER'
        elif '.m3u' in url or '.m3u8' in url:
            stype = 'HLSRETRY'
        if stype:
            from F4mProxy import f4mProxyHelper
            f4mp = f4mProxyHelper()
            xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
            f4mp.playF4mLink(
                url, name, proxy=None, use_proxy_for_chunks=False, maxbitrate=0, simpleDownloader=False,
                auth=None, streamtype=stype,setResolved=False, swf=None, callbackpath="", callbackparam="",
                iconImage=iconimage)
            return
    listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    listitem.setInfo('video', {'Title': name})
    listitem.setProperty("IsPlayable", "true")
    xbmc.Player().play(url, listitem)


def OPENSETTINGS():
    addon.openSettings()
    xbmc.executebuiltin('Container.Refresh')


def getParams():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if params[len(params) - 1] == '/':
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param


params = getParams()
url = None
name = None
mode = None
img = None
try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    img = urllib.unquote_plus(params["img"])
except:
    pass


if mode is None or mode == 0:
    MAIN()
elif mode == 1:
    PAGE(url)
elif mode == 2:
    LIST(url)
elif mode == 3:
    PLAY(url, name)
elif mode == 4:
    OPENSETTINGS()
elif mode == 5:
    MORELISTS()
elif mode == 6:
    REFRESH()
elif mode == 7:
    CLICK()
elif mode == 8:
    CLICK_4k()
elif mode == 9:
    CLICK_1080()
elif mode == 10:
    CLICK_720()
elif mode == 11:
    CLICK_SHOWS()
elif mode == 12:
    VOD_MOVIES()
elif mode == 13:
    VOD_SHOWS()
elif mode == 14:
    shows.SMALLVILLE()
elif mode == 15:
    shows.FAMLIYGUY()
elif mode == 16:
    shows.SIMPSONS()
elif mode == 17:
    shows.SUPERNATURAL()
elif mode == 18:
    shows.STARGATE()
elif mode == 19:
    shows.HOUSE()
elif mode == 20:
    shows.BALLERS()
elif mode == 21:
    shows.IZOMBIE()
elif mode == 22:
    FOREIGN()
