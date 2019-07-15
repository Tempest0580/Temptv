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
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
HOMEPATH = xbmc.translatePath('special://home/')
ADDONSPATH = os.path.join(HOMEPATH, 'addons')
THISADDONPATH = os.path.join(ADDONSPATH, ADDON_ID)
LOCALNEWS = os.path.join(THISADDONPATH, 'changelog.txt')
adult = addon.getSetting('Show_Adult')
dev = addon.getSetting('Dev')


def MAIN():
    addDir('Entertainment', userlists.english, 2,
           'https://i2.wp.com/www.somersetcounty4h.org/wp-content/uploads/entertainment-icon.png?fit=567%2C567')
    addDir('Movies', userlists.movies, 2,
           'https://d1nhio0ox7pgb.cloudfront.net/_img/o_collection_png/green_dark_grey/256x256/plain/movies.png')
    addDir('Kids', userlists.kids, 2,
           'https://yt3.ggpht.com/a/AGF-l7-eRsuCOQ43Hj9WVVU1xGY2L6sgA8S1DZLM2w=s900-mo-c-c0xffffffff-rj-k-no')
    addDir('Sports', userlists.sports, 2,
           'https://images.all-free-download.com/images/graphicthumb/free_sport_vector_pack_557881.jpg')
    addDir('News', userlists.news, 2,
           'https://esemag.com/wp-content/uploads/2015/11/News-Items.jpg')
    addDir('Music', userlists.music, 2,
           'https://c8.alamy.com/comp/PE2FM5/vector-cartoon-music-icon-in-comic-style-sound-note-sign-illustration-pictogram-melody-music-business-splash-effect-concept-PE2FM5.jpg')
    addDir('24/7', userlists.hour24, 2,
           'https://depo8.com/wp-content/uploads/2014/07/24-7-icon.png')
    addDir('1 Click Movies', '', 7,
           'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/c72e2f68-1a1c-48a2-aa5f-edf7eaaf3548/d704h5l-8e40963d-18aa-4982-a412-5c0ef52f6acf.png')
    addDir('1 Click Shows', '', 11,
           'http://chittagongit.com/images/tv-series-icon/tv-series-icon-15.jpg')
    addDir('In Theaters', userlists.theater, 2,
           'http://mytnnews.com/wp-content/uploads/2012/06/now-in-theaters.jpg')
    addDir('Pluto TV', userlists.pluto, 2,
           'https://images-na.ssl-images-amazon.com/images/I/519H2haYtzL._SY355_.png')
    addDir('Foreign Channels', '', 22,
           'https://www.inquirer.com/resizer/eVOmYXsz5FaBFcUDeCAosuKSCYM=/1400x932/smart/arc-anglerfish-arc2-prod-pmn.s3.amazonaws.com/public/X7GA4RXELJH7JFMTU4ONBWEPFU.jpg')
    addDir('Adult\'s Only', '', 13,
           'https://previews.123rf.com/images/123vector/123vector1403/123vector140300027/26460698-vector-illustration-of-red-adult-icon-on-white-background.jpg')
    if dev == 'true':
        addDir('Testing', '', 5,
               'http://icons.iconarchive.com/icons/aaron-sinuhe/series-season-folder/256/extras-icon.png')
    addDir('[B] Settings [/B]', 'url', 4,
           'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyhtqOw2iVU3-nBZMb1cWTDw_bsR4dkNtLvSkqQn3jsApD1A3', Folder=False)
    addDir('Refresh', '', 6,
           'https://maxcdn.icons8.com/app/uploads/2016/11/refresh1.png', Folder=False)
    addDir('Changelog', '', 12,
           'https://apprecs.org/gp/images/app-icons/300/ca/org.polaric.cyanogenmodchangelog.jpg', Folder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def ADULT():
    if adult == 'false':
        import xbmcgui
        xbmcgui.Dialog().ok('Adults Only 18+', 'If Your 18 or Older Enable Adult Channels in Settings')
        return
    else:
        LIST(userlists.adult)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def changelog():
    r = open(LOCALNEWS)
    compfile = r.read()
    showText('Changelog', compfile)


def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while retry > 0:
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            quit()
            return
        except:
            pass


def CLICK_SHOWS():
    addDir('Arrow', '', 30, 'https://images-na.ssl-images-amazon.com/images/I/81Jsimt3qAL._RI_.jpg')
    addDir('Ballers', '', 20, 'https://m.media-amazon.com/images/M/MV5BNTIzMDk3Mzc4Nl5BMl5BanBnXkFtZTgwODExNDAwNjM@._V1_.jpg')
    addDir('Chicago PD', '', 28, 'https://m.media-amazon.com/images/M/MV5BYjI4NjY0NTktZmMwMy00Yzk1LTk5NTgtYTU5MjAzYmY4NmY4XkEyXkFqcGdeQXVyODUxOTU0OTg@._V1_UX182_CR0,0,182,268_AL_.jpg')
    addDir('Designated Survivor', '', 23, 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Designated_Survivor_season_2_poster.jpeg/220px-Designated_Survivor_season_2_poster.jpeg')
    addDir('Family Guy', '', 15, 'https://m.media-amazon.com/images/M/MV5BODEwZjEzMjAtNjQxMy00Yjc4LWFlMDAtYjhjZTAxNDU3OTg3XkEyXkFqcGdeQXVyOTM2NTM4MjA@._V1_.jpg')
    addDir('The Flash 2014', '', 33, 'https://m.media-amazon.com/images/M/MV5BMjI1MDAwNDM4OV5BMl5BanBnXkFtZTgwNjUwNDIxNjM@._V1_UY268_CR16,0,182,268_AL_.jpg')
    addDir('House MD', '', 19, 'https://blog.cyrildason.com/wp-content/uploads/2016/11/House-MD.png')
    addDir('Izombie', '', 21, 'https://images-na.ssl-images-amazon.com/images/I/51msaPPK-sL._SY445_.jpg')
    addDir('Lie to Me', '', 29, 'https://m.media-amazon.com/images/M/MV5BMTc2MjA4MTM2OV5BMl5BanBnXkFtZTcwMTYzMzA1Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg')
    addDir('Married with Children', '', 34, 'https://m.media-amazon.com/images/M/MV5BMzk2OWYzNDUtNGE5NC00MDI0LTkyMDktY2RmZjE0NGNmMWE1XkEyXkFqcGdeQXVyMzU3MTc5OTE@._V1_UY268_CR0,0,182,268_AL_.jpg')
    addDir('Murder She Wrote', '', 24, 'https://m.media-amazon.com/images/M/MV5BOWQ1YjAyNzItYzkzYS00MDFlLTlmNWYtYjYyZWU1YjdiZDMzXkEyXkFqcGdeQXVyMTYzMDM0NTU@._V1_UY268_CR0,0,182,268_AL_.jpg')
    addDir('New Girl', '', 31, 'https://images-na.ssl-images-amazon.com/images/I/91nZQNPpSHL._RI_.jpg')
    addDir('Smallville', '', 14, 'https://m.media-amazon.com/images/M/MV5BYmNiNzlhOWItMDM5Mi00MGYzLWI1ZDYtNmI5NzI0MWFkMTIwXkEyXkFqcGdeQXVyNjU2NjA5NjM@._V1_.jpg')
    # addDir('Anger Managment', userlists.angermanagment, 2, 'https://i1.wp.com/hitenism.com/wp-content/uploads/Fotolia_61714948_L.jpg?ssl=1')
    addDir('The Simpsons', '', 16, 'https://m.media-amazon.com/images/M/MV5BYjFkMTlkYWUtZWFhNy00M2FmLThiOTYtYTRiYjVlZWYxNmJkXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg')
    addDir('Stargate SG1', '', 18, 'https://cdn1us.denofgeek.com/sites/denofgeekus/files/styles/main_wide/public/stargate_sg-1_cast.jpg?itok=EucgrKA3')
    addDir('Star Trek Discovery', '', 27, 'https://m.media-amazon.com/images/M/MV5BOTg5MzA1MjAwNV5BMl5BanBnXkFtZTgwNzAwMDU5NjM@._V1_.jpg')
    addDir('Suits', '', 32, 'https://images-na.ssl-images-amazon.com/images/I/81DPd3NRq0L._RI_.jpg')
    addDir('Supernatural', '', 17, 'https://cdn1us.denofgeek.com/sites/denofgeekus/files/styles/main_wide/public/supernatural_season_12_poster.jpg?itok=ocBbj_o5')
    addDir('The Twilight Zone 2019', '', 25, 'https://m.media-amazon.com/images/M/MV5BNzNkNjM0YTEtY2MwNi00OTJmLWFhMjAtN2M0ZTMwOTMxOTY1XkEyXkFqcGdeQXVyMjIwMjY2MzU@._V1_UY268_CR1,0,182,268_AL_.jpg')
    addDir('The Office', '', 26, 'https://m.media-amazon.com/images/M/MV5BMTgzNjAzMDE0NF5BMl5BanBnXkFtZTcwNTEyMzM3OA@@._V1_.jpg')
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


    addDir('Bosnia and Herzegovina', userlists.Bosnia_and_Herzegovina, 2, 'https://cdn.britannica.com/02/6202-004-E8117B4F.jpg')
    addDir('Brazil', userlists.Brazil, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/1280px-Flag_of_Brazil.svg.png')
    addDir('Bulgaria', userlists.Bulgaria, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Bulgaria.svg/2000px-Flag_of_Bulgaria.svg.png')
    addDir('Cambodia', userlists.Cambodia, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Flag_of_Cambodia_vertical.svg/2000px-Flag_of_Cambodia_vertical.svg.png')
    addDir('Canada', userlists.Canada, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Canadian_Duality_Flag.svg/1200px-Canadian_Duality_Flag.svg.png')
    addDir('Chile', userlists.Chile, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Flag_of_Chile.svg/2000px-Flag_of_Chile.svg.png')
    addDir('China', userlists.China, 2, 'http://3temp.com/wp-content/uploads/2017/12/kinas-flagga.png')
    addDir('Colombia', userlists.Colombia, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/255px-Flag_of_Colombia.svg.png')
    addDir('Costa Rica', userlists.Costa_Rica, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Costa_Rica_%28state%29.svg/255px-Flag_of_Costa_Rica_%28state%29.svg.png')
    addDir('Croatia', userlists.Croatia, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Flag_of_Croatia.svg/2000px-Flag_of_Croatia.svg.png')
    addDir('Cuba', userlists.Cuba, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Flag_of_Cuba.svg/2000px-Flag_of_Cuba.svg.png')
    addDir('Cyprus', userlists.Cyprus, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Cyprus.svg/2000px-Flag_of_Cyprus.svg.png')
    addDir('Czech Republic', userlists.Czech_Republic, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_Czech_Republic.svg/255px-Flag_of_the_Czech_Republic.svg.png')
    addDir('Democratic Republic of the Congo', userlists.Democratic_Republic_of_the_Congo, 2, 'https://www.carnegiecouncil.org/publications/ethics_online/0046/_res/id=Picture/feature_DRC_Flag.jpg')
    addDir('Denmark', userlists.Denmark, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/2000px-Flag_of_Denmark.svg.png')
    addDir('Dominican Republic', userlists.Dominican_Republic, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_the_Dominican_Republic.svg/255px-Flag_of_the_Dominican_Republic.svg.png')
    addDir('Ecuador', userlists.Ecuador, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Flag_of_Ecuador.svg/2000px-Flag_of_Ecuador.svg.png')
    addDir('Egypt', userlists.Egypt, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Egypt.svg/255px-Flag_of_Egypt.svg.png')
    addDir('El Salvador', userlists.El_Salvador, 2, 'https://www.flagsimporter.com/pub/media/catalog/product/cache/image/600x800/e9c3970ab036de70892d86c6d221abfe/e/l/el-salvador35_tn_1.jpg')
    addDir('Equatorial Guinea', userlists.Equatorial_Guinea, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Flag_of_Equatorial_Guinea.svg/2000px-Flag_of_Equatorial_Guinea.svg.png')
    addDir('Estonia', userlists.Estonia, 2, 'https://www.flags-flagpoles-banners.co.uk/wp-content/uploads/2015/01/Estonia-flag.jpg')
    addDir('Finland', userlists.Finland, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Finland.svg/2000px-Flag_of_Finland.svg.png')
    addDir('France', userlists.France, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/250px-Flag_of_France.svg.png')
    addDir('Georgia', userlists.Georgia, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag_of_Georgia.svg/1200px-Flag_of_Georgia.svg.png')
    addDir('Germany', userlists.Germany, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/1280px-Flag_of_Germany.svg.png')
    addDir('Ghana', userlists.Ghana, 2, 'https://www.bankingtech.com/files/2016/12/Ghana-flag.jpg')
    addDir('Greece', userlists.Greece, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Greece.svg/2000px-Flag_of_Greece.svg.png')
    #addDir('Guatemala', userlists.Guatemala, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Flag_of_Guatemala.svg/2000px-Flag_of_Guatemala.svg.png')
    addDir('Guinea', userlists.Guinea, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Flag_of_Guinea.svg/2000px-Flag_of_Guinea.svg.png')
    addDir('Guyana', userlists.Guyana, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_Guyana.svg/2000px-Flag_of_Guyana.svg.png')
    addDir('Haiti', userlists.Haiti, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_Haiti.svg/2000px-Flag_of_Haiti.svg.png')
    addDir('Honduras', userlists.Honduras, 2, 'https://worthingtoncc.org/wp-content/uploads/hn.png')
    addDir('Hong Kong', userlists.Hong_Kong, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/2000px-Flag_of_Hong_Kong.svg.png')
    addDir('Iceland', userlists.Iceland, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Iceland.svg/2000px-Flag_of_Iceland.svg.png')
    addDir('India', userlists.India, 2, 'https://i.redd.it/2zaqa12lfsp01.png')
    addDir('Indonesia', userlists.Indonesia, 2, 'https://cdn.britannica.com/48/1648-004-644EBE62.jpg')
    addDir('Iran', userlists.Iran, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_Iran_%28official%29.svg/2000px-Flag_of_Iran_%28official%29.svg.png')
    addDir('Iraq', userlists.Iraq, 2, 'https://swassets.visitcanberra.com.au/atdw/0002/36/thumb_135210_atdw_gallery.jpeg')
    addDir('Ireland', userlists.Ireland, 2, 'https://upload.wikimedia.org/wikipedia/en/0/02/IRL_FLAG.jpg')
    addDir('Israel', userlists.Israel, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Israel.svg/1200px-Flag_of_Israel.svg.png')

    addDir('Italy', userlists.Italy, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/255px-Flag_of_Italy.svg.png')
    addDir('Mexico', userlists.Mexico, 2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/2000px-Flag_of_Mexico.svg.png')
    addDir('Russia', userlists.Russia, 2, 'https://image.shutterstock.com/image-vector/russia-flag-vector-icon-260nw-549159163.jpg')
    addDir('Spain', userlists.Spain, 2, 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1280px-Flag_of_Spain.svg.png')
    addDir('United Kingdom', userlists.uk, 2, 'https://images-na.ssl-images-amazon.com/images/I/512-H5HhT6L._SX425_.jpg')
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
    changelog()
elif mode == 13:
    ADULT()
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
elif mode == 23:
    shows.Designated_Survivor()
elif mode == 24:
    shows.MURDER_SHE_WROTE()
elif mode == 25:
    shows.TWILIGHT()
elif mode == 26:
    shows.THE_OFFICE()
elif mode == 27:
    shows.STAR_TREK_DIS()
elif mode == 28:
    shows.CHICAGO_PD()
elif mode == 29:
    shows.LIE_TO_ME()
elif mode == 30:
    shows.ARROW()
elif mode == 31:
    shows.NEW_GIRL()
elif mode == 32:
    shows.SUITS()
elif mode == 33:
    shows.THE_FLASH()
elif mode == 34:
    shows.MARRIED_WITH_CHILDREN()

