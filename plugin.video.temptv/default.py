# -*- coding: UTF-8 -*-

import re, os, sys, urllib, urllib2, requests, socket, gzip
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import userlists
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


def MAIN():
    addDir('Entertainment', userlists.english, 2, AddonIcon)
    addDir('Movies', userlists.movies, 2, AddonIcon)
    addDir('Kids', userlists.kids, 2, AddonIcon)
    addDir('Sports', userlists.sports, 2, AddonIcon)
    addDir('News', userlists.news, 2, AddonIcon)
    addDir('Music', userlists.music, 2, AddonIcon)
    addDir('27/7', userlists.hour24, 2, AddonIcon)
    addDir('Pluto.TV', userlists.pluto, 2, AddonIcon)
    addDir('1 Click Movies', '', 7, AddonIcon)
    addDir('1 Click Shows', '', 11, AddonIcon)
    addDir('On Demand Movies', '', 12, AddonIcon)
    addDir('On Demand Shows', '', 13, AddonIcon)
    addDir('UK', userlists.uk, 2, AddonIcon)
    if adult == 'true':
        addDir('Lust', userlists.adult, 2, AddonIcon)
    addDir('MORELISTS', '', 5, AddonIcon)
    addDir('[B] Settings [/B]', 'url', 4, AddonIcon, Folder=False)
    addDir('Refresh', '', 6, AddonIcon, Folder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def VOD_MOVIES():
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def VOD_SHOWS():
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK_SHOWS():
    addDir('Smallville', userlists.smallville, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK_4k():
    addDir('2019', userlists.click_4k_2019, 2, AddonIcon)
    addDir('2018', userlists.click_4k_2018, 2, AddonIcon)
    addDir('1993', userlists.click_4k_1993, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK_1080():
    addDir('2019', userlists.click_1080p_2019, 2, AddonIcon)
    addDir('2018', userlists.click_1080p_2018, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK_720():
    addDir('2019', userlists.click_720_2019, 2, AddonIcon)
    addDir('2018', userlists.click_720_2018, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CLICK():
    addDir('4K', '', 8, AddonIcon)
    addDir('1080p', '', 9, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def MORELISTS():
    addDir('Testing', userlists.testing, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


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
    match = re.compile('#.+? tvg-logo="(.+?)" .+,(.+?)\n(.+?)\n').findall(html)
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
        elif '.m3u' in url:
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

