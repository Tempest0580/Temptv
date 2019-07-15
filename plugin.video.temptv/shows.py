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


def ARROW():
    addDir('Season 1', userlists.arrow1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Arrow_Season_1.png/220px-Arrow_Season_1.png')
    addDir('Season 2', userlists.arrow2, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a0/Arrow_Season_2.png/220px-Arrow_Season_2.png')
    addDir('Season 3', userlists.arrow3, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/6/64/Arrow_Season_3.png/220px-Arrow_Season_3.png')
    addDir('Season 4', userlists.arrow4, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9c/Arrow_season_4.jpg/220px-Arrow_season_4.jpg')
    addDir('Season 5', userlists.arrow5, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Arrow_season_5.jpg/220px-Arrow_season_5.jpg')
    addDir('Season 6', userlists.arrow6, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Arrow_season_6.jpg/220px-Arrow_season_6.jpg')
    addDir('Season 7', userlists.arrow7, 2, 'https://upload.wikimedia.org/wikipedia/en/c/c7/Arrow_season_7.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


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


def HOUSE():
    addDir('Season 1', userlists.housemd1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/HouseMD-s1-UK-DVD.jpg/250px-HouseMD-s1-UK-DVD.jpg')
    addDir('Season 2', userlists.housemd1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/0/07/HouseMD-s2-AU-DVD.jpg/250px-HouseMD-s2-AU-DVD.jpg')
    addDir('Season 3', userlists.housemd1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/HouseMD-s3-US-DVD.jpg/250px-HouseMD-s3-US-DVD.jpg')
    addDir('Season 4', userlists.housemd1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/d/da/HouseMD-s4-US-DVD.jpg/250px-HouseMD-s4-US-DVD.jpg')
    addDir('Season 5', userlists.housemd1, 2, 'https://upload.wikimedia.org/wikipedia/en/c/ce/HouseMD-s5-US-DVD.jpg')
    addDir('Season 6', userlists.housemd1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/1/16/House_S6_DVD.jpg/250px-House_S6_DVD.jpg')
    addDir('Season 7', userlists.housemd1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/3/37/House_S7_DVD.jpg/250px-House_S7_DVD.jpg')
    addDir('Season 8', userlists.housemd1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/e/ee/House_S8_DVD.jpg/220px-House_S8_DVD.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def IZOMBIE():
    addDir('Season 1', userlists.izombie1, 2, 'https://resizing.flixster.com/zFsWD4r6sgKU2_Vf-Xl555P9JaM=/206x305/v1.dDsxNDY2MDI7ajsxODA5MTsxMjAwOzE5OTg7MjY2NA')
    addDir('Season 2', userlists.izombie2, 2, 'https://resizing.flixster.com/ncge5Px1eEa6C5DPAHGHhsSBkBs=/206x305/v1.dDsyNzA0MjE7ajsxODA5MzsxMjAwOzExMjQ7MTY4Ng')
    addDir('Season 3', userlists.izombie3, 2, 'https://vignette.wikia.nocookie.net/izombie/images/e/ef/Brain_Freeze.jpg/revision/latest?cb=20170405224605')
    # addDir('Season 4', userlists.izombie4, 2, 'https://vignette.wikia.nocookie.net/izombie/images/c/c6/4Poster.png/revision/latest?cb=20180216210229')
    addDir('Season 5', userlists.izombie5, 2, 'https://vignette.wikia.nocookie.net/izombie/images/6/63/Final_season_promotional_poster.jpg/revision/latest?cb=20190615092836')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def BALLERS():
    addDir('Season 1', userlists.ballers1, 2, 'https://vignette.wikia.nocookie.net/ballers/images/c/c8/Ballers_Season_1_poster.jpg/revision/latest/scale-to-width-down/300?cb=20150520101615')
    addDir('Season 2', userlists.ballers2, 2, 'https://resizing.flixster.com/i8u0JTgPqGfHXx8B7VNURDZbZPQ=/206x305/v1.dDsyNTkyNzg7ajsxODA5MzsxMjAwOzE5NzQ7Mjk2MQ')
    addDir('Season 3', userlists.ballers3, 2, 'https://is2-ssl.mzstatic.com/image/thumb/Video118/v4/25/13/65/25136577-2b8c-64e8-7f6c-ae9fa5b8c91a/mzl.lozwsaqw.lsr/268x0w.jpg')
    addDir('Season 4', userlists.ballers4, 2, 'https://m.media-amazon.com/images/M/MV5BNTIzMDk3Mzc4Nl5BMl5BanBnXkFtZTgwODExNDAwNjM@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def Designated_Survivor():
    addDir('Season 1', userlists.designated_survivor1, 2,
           'https://upload.wikimedia.org/wikipedia/en/thumb/d/df/Designated_Survivor_season_1_dvd.jpg/250px-Designated_Survivor_season_1_dvd.jpg')
    addDir('Season 2', userlists.designated_survivor2, 2,
           'https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Designated_Survivor_season_2_poster.jpeg/220px-Designated_Survivor_season_2_poster.jpeg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def MURDER_SHE_WROTE():
    addDir('Season 1', userlists.murder_she_wrote1, 2, 'https://images-na.ssl-images-amazon.com/images/I/513AD9ZVJQL.jpg')
    addDir('Season 2', userlists.murder_she_wrote2, 2, 'https://oldies-cdn.freetls.fastly.net/i/boxart/w340/a-z/m/mhv61129410d.jpg?v=5')
    addDir('Season 3', userlists.murder_she_wrote3, 2, 'https://images-na.ssl-images-amazon.com/images/I/51fhtaqKvGL._SY445_.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def TWILIGHT():
    addDir('Season 1', userlists.twilight1, 2,  'https://images-na.ssl-images-amazon.com/images/I/513AD9ZVJQL.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def THE_OFFICE():
    addDir('Season 1', userlists.the_office1, 2, 'https://upload.wikimedia.org/wikipedia/en/b/b6/TheOfficeUSSeason1Cover.jpg')
    addDir('Season 2', userlists.the_office2, 2, 'https://upload.wikimedia.org/wikipedia/en/9/96/Office_Season_2.jpg')
    addDir('Season 3', userlists.the_office3, 2, 'https://upload.wikimedia.org/wikipedia/en/2/24/TheOfficeUSSeason3Cover.jpg')
    addDir('Season 4', userlists.the_office4, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/The_Office_Season_Four_DVD_Cover.jpg/250px-The_Office_Season_Four_DVD_Cover.jpg')
    addDir('Season 5', userlists.the_office5, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Office_S5_DVD.JPG/250px-Office_S5_DVD.JPG')
    addDir('Season 6', userlists.the_office6, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a5/TheOffice_S6_DVD.jpg/250px-TheOffice_S6_DVD.jpg')
    addDir('Season 7', userlists.the_office7, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/5/58/TheOffice_S7_DVD.jpg/250px-TheOffice_S7_DVD.jpg')
    addDir('Season 8', userlists.the_office8, 2, 'https://upload.wikimedia.org/wikipedia/en/a/ae/The_Office_Season_8.jpg')
    addDir('Season 9', userlists.the_office9, 2, 'https://upload.wikimedia.org/wikipedia/en/3/32/The_Office_S9_DVD.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def STAR_TREK_DIS():
    addDir('Season 1', userlists.star_trek_dis1, 2, 'https://images-na.ssl-images-amazon.com/images/I/91UII5jLUOL._SX342_.jpg')
    addDir('Season 2', userlists.star_trek_dis2, 2, 'https://cdn.shopify.com/s/files/1/0004/3407/7751/products/ST2_177d170c-4551-400b-85e7-aa00c5729937_300x300.jpg?v=1556945297')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def CHICAGO_PD():
    addDir('Season 1', userlists.chicago_pd1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Chicago_P.D._Season_1_DVD_Cover.jpg/220px-Chicago_P.D._Season_1_DVD_Cover.jpg')
    addDir('Season 2', userlists.chicago_pd2, 2,  'https://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Chicago_P.D._Season_2_DVD_Cover.jpg/220px-Chicago_P.D._Season_2_DVD_Cover.jpg')
    addDir('Season 3', userlists.chicago_pd3, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Chicago_P.D._Season_3_DVD_Cover.jpg/220px-Chicago_P.D._Season_3_DVD_Cover.jpg')
    addDir('Season 4', userlists.chicago_pd4, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/7/73/CPD_S4_DVD.jpg/220px-CPD_S4_DVD.jpg')
    addDir('Season 5', userlists.chicago_pd5, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/3/36/Season_5_DVD_Cover_art_of_American_police_drama%2C_Chicago_P.D.jpg/220px-Season_5_DVD_Cover_art_of_American_police_drama%2C_Chicago_P.D.jpg')
    addDir('Season 6', userlists.chicago_pd6, 2, 'https://pbs.twimg.com/media/D0R3-YmV4AAA7pk.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def LIE_TO_ME():
    addDir('Season 1', userlists.lie_to_me1, 2, 'https://images-na.ssl-images-amazon.com/images/I/81O74Gm%2BCVL._SX342_.jpg')
    addDir('Season 2', userlists.lie_to_me2, 2, 'https://images-na.ssl-images-amazon.com/images/I/51%2BDKcqi1JL._SY445_.jpg')
    addDir('Season 3', userlists.lie_to_me3, 2, 'https://images-na.ssl-images-amazon.com/images/I/91OfikX%2BxsL._SY445_.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def NEW_GIRL():
    addDir('Season 1', userlists.new_girl1, 2,
           'https://upload.wikimedia.org/wikipedia/en/thumb/8/8c/New_Girl_S1_DVD.jpg/220px-New_Girl_S1_DVD.jpg')
    addDir('Season 2', userlists.new_girl2, 2,
           'https://upload.wikimedia.org/wikipedia/en/thumb/9/94/New_Girl_S2.jpg/220px-New_Girl_S2.jpg')
    addDir('Season 3', userlists.new_girl3, 2,
           'https://upload.wikimedia.org/wikipedia/en/thumb/3/37/New_Girl_S3_DVD.jpg/220px-New_Girl_S3_DVD.jpg')
    addDir('Season 4', userlists.new_girl4, 2,
           'https://upload.wikimedia.org/wikipedia/en/thumb/b/b1/New_Girl_season_4_DVD.png/220px-New_Girl_season_4_DVD.png')
    addDir('Season 5', userlists.new_girl5, 2,
           'https://upload.wikimedia.org/wikipedia/en/e/eb/New_Girl_Season5Cover.png')
    addDir('Season 6', userlists.chicago_pd6, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0e/New_Girl_season_6_DVD.png/220px-New_Girl_season_6_DVD.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def SUITS():
    addDir('Season 1', userlists.suits1, 2, 'https://upload.wikimedia.org/wikipedia/en/2/2c/SuitsSeasn1DVDCover.jpg')
    addDir('Season 2', userlists.suits2, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Suits_season_2_dvd.jpg/240px-Suits_season_2_dvd.jpg')
    addDir('Season 3', userlists.suits3, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Suits_season_3_dvd.jpg/230px-Suits_season_3_dvd.jpg')
    addDir('Season 4', userlists.suits4, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Suits_season_4_dvd.jpg/220px-Suits_season_4_dvd.jpg')
    addDir('Season 5', userlists.suits5, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Suits_season_5_dvd.jpg/220px-Suits_season_5_dvd.jpg')
    addDir('Season 6', userlists.suits6, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Suits_Season_6_DVD_Cover.jpg/220px-Suits_Season_6_DVD_Cover.jpg')
    addDir('Season 7', userlists.suits7, 2,  'https://upload.wikimedia.org/wikipedia/en/thumb/7/78/Suits_season_7_dvd_cover.jpg/220px-Suits_season_7_dvd_cover.jpg')
    addDir('Season 8', userlists.suits8, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Suits_season_8_part_1_dvd_cover.jpg/220px-Suits_season_8_part_1_dvd_cover.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def THE_FLASH():
    addDir('Season 1', userlists.the_flash1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/7/73/The_Flash_season_1.jpg/220px-The_Flash_season_1.jpg')
    addDir('Season 2', userlists.the_flash2, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Flash_season_2.jpg/220px-The_Flash_season_2.jpg')
    addDir('Season 3', userlists.the_flash3, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/The_Flash_season_3.jpg/220px-The_Flash_season_3.jpg')
    addDir('Season 4', userlists.the_flash4, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/The_Flash_season_4.jpg/220px-The_Flash_season_4.jpg')
    addDir('Season 5', userlists.the_flash5, 2, 'https://www.dvdland.com.au/product_images/f/705/flashs5__26640_zoom.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def MARRIED_WITH_CHILDREN():
    addDir('Season 1', userlists.married_with_children1, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Marriedwithchildrendvdseason1.jpg/200px-Marriedwithchildrendvdseason1.jpg')
    addDir('Season 2', userlists.married_with_children2, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/d/dd/Married..._with_Children_season_2.png/220px-Married..._with_Children_season_2.png')
    addDir('Season 3', userlists.married_with_children3, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/6/65/Married..._with_Children_season_3.png/220px-Married..._with_Children_season_3.png')
    addDir('Season 4', userlists.married_with_children4, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Married..._with_Children_season_4.png/220px-Married..._with_Children_season_4.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
