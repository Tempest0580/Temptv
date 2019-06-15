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
    addDir('Season 3', userlists.familyguy3, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/4/46/FamilyGuy_season_1.png/220px-FamilyGuy_season_1.png')
    addDir('Season 4', userlists.familyguy4, 2, 'https://images-na.ssl-images-amazon.com/images/I/817xqXaw3bL._SY445_.jpg')
    addDir('Season 5', userlists.familyguy5, 2, 'https://images-na.ssl-images-amazon.com/images/I/81iB1SamyOL._SY445_.jpg')
    addDir('Season 6', userlists.familyguy6, 2, 'https://images-na.ssl-images-amazon.com/images/I/81oLqnxDtyL._SY445_.jpg')
    addDir('Season 7', userlists.familyguy7, 2, 'https://upload.wikimedia.org/wikipedia/en/6/66/Family_Guy_Vol7.jpg')
    addDir('Season 8', userlists.familyguy8, 2, 'https://upload.wikimedia.org/wikipedia/en/7/70/Family_Guy_Volume_8_DVD_Cover.png')
    addDir('Season 9', userlists.familyguy9, 2, 'https://images-na.ssl-images-amazon.com/images/I/51yAXl5qmgL._SY445_.jpg')
    addDir('Season 10', userlists.familyguy10, 2, 'https://images-na.ssl-images-amazon.com/images/I/91mjfbhKsVL._SL1500_.jpg')
    addDir('Season 11', userlists.familyguy11, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Family_Guy_Season_12_DVD.jpg/220px-Family_Guy_Season_12_DVD.jpg')
    addDir('Season 12', userlists.familyguy12, 2, 'https://images-na.ssl-images-amazon.com/images/I/51cczA8ANuL._SY445_.jpg')
    addDir('Season 13', userlists.familyguy13, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/FG-season_13_coverart.jpeg/220px-FG-season_13_coverart.jpeg')
    addDir('Season 17', userlists.familyguy17, 2, 'https://cdn.watch-series.co/cover/family-guy-season-17.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def SIMPSONS():
    addDir('Season 29', userlists.simpsons29, 2, 'https://i.pinimg.com/736x/10/97/a2/1097a2d8acaab69e35d5f83024805da8.jpg')
    addDir('Season 30', userlists.simpsons30, 2, 'http://www.indiewire.com/wp-content/uploads/2017/07/simpsons_s29_miniposter_2017.jpg?w=663')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def SUPERNATURAL():
    addDir('Season 1', userlists.supernatural1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Supernatural_Season_1.jpg/220px-Supernatural_Season_1.jpg')
    addDir('Season 2', userlists.supernatural2, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Supernatural_Season_2.jpg/220px-Supernatural_Season_2.jpg')
    addDir('Season 3', userlists.supernatural3, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Supernatural_Season_3.jpg/220px-Supernatural_Season_3.jpg')
    addDir('Season 4', userlists.supernatural4, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Supernatural_Season_4.jpg/220px-Supernatural_Season_4.jpg')
    addDir('Season 5', userlists.supernatural5, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c8/Supernatural_Season_5.jpg/220px-Supernatural_Season_5.jpg')
    addDir('Season 6', userlists.supernatural6, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Supernatural_Season_6.jpg/220px-Supernatural_Season_6.jpg')
    addDir('Season 7', userlists.supernatural7, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Supernatural_Season_7.jpg/220px-Supernatural_Season_7.jpg')
    addDir('Season 8', userlists.supernatural8, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Supernatural_Season_8.jpg/220px-Supernatural_Season_8.jpg')
    addDir('Season 9', userlists.supernatural9, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/b/b5/Supernatural_Season_9.jpg/220px-Supernatural_Season_9.jpg')
    addDir('Season 10', userlists.supernatural10, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Supernatural_Season_10.jpg/220px-Supernatural_Season_10.jpg')
    addDir('Season 11', userlists.supernatural11, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Supernatural_Season_11.jpg/220px-Supernatural_Season_11.jpg')
    addDir('Season 12', userlists.supernatural12, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Supernatural_Season_12.jpg/220px-Supernatural_Season_12.jpg')
    addDir('Season 13', userlists.supernatural13, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Supernatural_Season_13.jpg/220px-Supernatural_Season_13.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def STARGATE():
    addDir('Season 1', userlists.stargate1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Stargate_SG-1_Season_1.jpg/220px-Stargate_SG-1_Season_1.jpg')
    addDir('Season 2', userlists.stargate2, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/Stargate_SG-1_Season_2.jpg/220px-Stargate_SG-1_Season_2.jpg')
    addDir('Season 3', userlists.stargate3, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/1/1d/Stargate_SG-1_Season_3.jpg/220px-Stargate_SG-1_Season_3.jpg')
    addDir('Season 4', userlists.stargate4, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Stargate_SG-1_Season_4.jpg/220px-Stargate_SG-1_Season_4.jpg')
    addDir('Season 5', userlists.stargate5, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Stargate_SG-1_Season_5.jpg/220px-Stargate_SG-1_Season_5.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def BALLERS():
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
