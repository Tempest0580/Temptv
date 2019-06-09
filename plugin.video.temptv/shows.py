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


def SMALLVILLE():
    addDir('Season 1', userlists.smallville1, 2, "https://images-na.ssl-images-amazon.com/images/I/91kIbWInR0L._SY445_.jpg")
    addDir('Season 2', userlists.smallville2, 2, "https://www.jbhifi.com.au/FileLibrary/ProductResources/Images/17021-L-LO.jpg")
    #addDir('Season 3', userlists.smallville3, 2, AddonIcon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def FAMLIYGUY():
    addDir('Season 1', userlists.familyguy1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Family_Guy_Season1.png/220px-Family_Guy_Season1.png')
    addDir('Season 2', userlists.familyguy2, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Family_Guy_Season1.png/220px-Family_Guy_Season1.png')
    addDir('Season 12', userlists.familyguy12, 2, 'https://images-na.ssl-images-amazon.com/images/I/51cczA8ANuL._SY445_.jpg')
    addDir('Season 13', userlists.familyguy13, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/FG-season_13_coverart.jpeg/220px-FG-season_13_coverart.jpeg')
    addDir('Season 17', userlists.familyguy17, 2, 'https://cdn.watch-series.co/cover/family-guy-season-17.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SIMPSONS():
    addDir('Season 30', userlists.simpsons30, 2, 'http://www.indiewire.com/wp-content/uploads/2017/07/simpsons_s29_miniposter_2017.jpg?w=663')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))




