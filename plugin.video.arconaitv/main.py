
import os.path, requests, json
import sys, urllib, urllib2, urlparse
import xbmcaddon, xbmcgui, xbmcplugin, xbmc
from resources.lib.modules import jsunpack, client
from bs4 import BeautifulSoup

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
mode = args.get('mode', None)

artbase_url = "https://github.com/jewbmx/xml/blob/master/img/arconaitv/%s?raw=true"
arconaitv_url = "https://www.arconaitv.us/"
headers = {'User-Agent': client.agent()}

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)


def getCableInfo(title):
    desc_file = os.path.join(os.path.dirname(__file__), 'cable.json')
    with open(desc_file) as file:
        data = file.read()
    parsed = json.loads(data)
    for cable in parsed['cable']:
        if title == cable['title']:
            return cable
    return {'title': title, 'description': 'New Channel!', 'poster': ' DefaultVideo.png'}


def getShowInfo(title):
    desc_file = os.path.join(os.path.dirname(__file__), 'shows.json')
    with open(desc_file) as file:
        data = file.read()
    parsed = json.loads(data)
    for show in parsed['shows']:
        if title == show['title']:
            return show
    return {'title': title, 'description': 'New Show!', 'poster': 'DefaultVideo.png'}


def getMovieInfo(title):
    desc_file = os.path.join(os.path.dirname(__file__), 'movies.json')
    with open(desc_file) as file:
        data = file.read()
    parsed = json.loads(data)
    for movie in parsed['movies']:
        if title == movie['title']:
            return movie
    return {'title': title, 'description': 'New Movie!', 'poster': 'DefaultVideo.png'}


def list_categories():
    url = build_url({'action': 'arconai'})
    li = xbmcgui.ListItem("""Arconaitv needs help, Please vist https://www.facebook.com/Arconaitv/
and donate. Anything will help. Thanks""")
    img = artbase_url % 'Arc.jpg'
    li.setArt({'thumb': img, 'poster': img})
    il = {"plot": "Please Help The site get back to normal"}
    li.setInfo(type='Video', infoLabels=il)
    xbmcplugin.addDirectoryItem(addon_handle, url=url, listitem=li, isFolder=False)

    url = build_url({'mode': 'cable'})
    li = xbmcgui.ListItem("Live TV Channels")
    cable_img = artbase_url % "arconaiCable.png"
    li.setArt({'thumb': cable_img, 'poster': cable_img})
    il = {"plot": "Live TV Channels"}
    li.setInfo(type='Video', infoLabels=il)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'shows'})
    li = xbmcgui.ListItem("24/7 TV Shows")
    shows_img = artbase_url % "arconaiShows.png"
    li.setArt({'thumb': shows_img, 'poster': shows_img})
    il = {"plot": "24/7 Streams of Tv Shows"}
    li.setInfo(type='Video', infoLabels=il)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'movies'})
    li = xbmcgui.ListItem("24/7 Movies")
    movies_img = artbase_url % "arconaiMovies.png"
    li.setArt({'thumb': movies_img, 'poster': movies_img})
    il = {"plot": "24/7 Streams of Movies"}
    li.setInfo(type='Video', infoLabels=il)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'play', 'selection': 'stream.php?id=random'})
    li = xbmcgui.ListItem("Random Streams")
    movies_img = artbase_url % "arconaiRandom.png"
    li.setArt({'thumb': movies_img, 'poster': movies_img})
    il = {"plot": "Streams a Random Channel"}
    li.setProperty('IsPlayable', 'true')
    li.setInfo(type='Video', infoLabels=il)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(addon_handle)


def list_cable():
    arconaitv_r = requests.get(urlparse.urljoin(arconaitv_url, "index.php"), headers=headers)
    html_text = arconaitv_r.text.encode('ascii', 'ignore')
    soup = BeautifulSoup(html_text, 'html.parser')
    try:
        cable = soup.find("div", id="cable")
        boxes = cable.find_all("div", class_="box-content")
    except AttributeError:
        xbmcgui.Dialog().ok("Sorry", "The website has changed or we are downloading from wrong website.")
        return
    listItemlist = []
    for box in boxes:
        if box.a is None:
            continue
        url = build_url({'mode': 'play', 'selection': box.a["href"]})
        title = box.a["title"].strip()
        cableInfo = getCableInfo(title)
        li = xbmcgui.ListItem(title, iconImage=cableInfo['poster'])
        il = {"Title": title, "mediatype": "video", "plot": cableInfo['description'], "plotoutline": cableInfo['description']}
        li.setProperty('IsPlayable', 'true')
        li.setInfo(type='Video', infoLabels=il)
        listItemlist.append([url, li, False])
    listLength = len(listItemlist)
    xbmcplugin.addDirectoryItems(handle=addon_handle, items=listItemlist, totalItems=listLength)
    xbmcplugin.setContent(addon_handle, 'tvshows')
    xbmc.executebuiltin("Container.SetViewMode(55)")
    xbmcplugin.endOfDirectory(addon_handle)


def list_shows():
    arconaitv_r = requests.get(urlparse.urljoin(arconaitv_url, "index.php"), headers=headers)
    html_text = arconaitv_r.text.encode('ascii', 'ignore')
    soup = BeautifulSoup(html_text, 'html.parser')
    try:
        shows = soup.find("div", id="shows")
        boxes = shows.find_all("div", class_="box-content")
    except AttributeError:
        xbmcgui.Dialog().ok("Sorry", "The website has changed or we are downloading from wrong website.")
        return
    listItemlist = []
    for box in boxes:
        if box.a is None:
            continue
        url = build_url({'mode': 'play', 'selection': box.a["href"]})
        title = box.a["title"].strip()
        showInfo = getShowInfo(title)
        li = xbmcgui.ListItem(showInfo['title'], iconImage=showInfo['poster'])
        il = {"Title": title, "mediatype": "video", "plot": showInfo['description'], "plotoutline": showInfo['description']}
        li.setProperty('IsPlayable', 'true')
        li.setInfo(type='Video', infoLabels=il)
        li.setArt({'poster': showInfo['poster'], 'banner': showInfo['poster']})
        listItemlist.append([url, li, False])
    listLength = len(listItemlist)
    xbmcplugin.addDirectoryItems(handle=addon_handle, items=listItemlist, totalItems=listLength)
    xbmcplugin.setContent(addon_handle, 'tvshows')
    xbmc.executebuiltin("Container.SetViewMode(55)")
    xbmcplugin.endOfDirectory(addon_handle)


def list_movies():
    arconaitv_r = requests.get(urlparse.urljoin(arconaitv_url, "index.php"), headers=headers)
    html_text = arconaitv_r.text.encode('ascii', 'ignore')
    soup = BeautifulSoup(html_text, 'html.parser')
    try:
        movies = soup.find("div", id="movies")
        boxes = movies.find_all("div", class_="box-content")
    except AttributeError:
        xbmcgui.Dialog().ok("Sorry", "The website has changed or we are downloading from wrong website.")
        return
    listItemlist = []
    for box in boxes:
        if box.a is None:
            continue
        url = build_url({'mode': 'play', 'selection': box.a["href"]})
        title = box.a["title"].strip()
        movieInfo = getMovieInfo(title)
        li = xbmcgui.ListItem(movieInfo['title'], iconImage=movieInfo['poster'])
        il = {"Title": title, "mediatype": "video", "plot": movieInfo['description'], "plotoutline": movieInfo['description']}
        li.setProperty('IsPlayable', 'True')
        li.setProperty('mimetype', 'application/x-mpegURL')
        li.setInfo(type='Video', infoLabels=il)
        li.setArt({'poster': movieInfo['poster'], 'banner': movieInfo['poster']})
        listItemlist.append([url, li, False])
    listLength = len(listItemlist)
    xbmcplugin.addDirectoryItems(handle=addon_handle, items=listItemlist, totalItems=listLength)
    xbmcplugin.setContent(addon_handle, 'movies')
    xbmc.executebuiltin("Container.SetViewMode(55)")
    xbmcplugin.endOfDirectory(addon_handle)


def play_video(selection):
    r = requests.get(urlparse.urljoin(arconaitv_url, selection), headers=headers)
    html_text = r.text
    soup = BeautifulSoup(html_text, 'html.parser')
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string is not None:
            if "document.getElementsByTagName('video')[0].volume = 1.0;" in script.string:
                code = script.string
                startidx = code.find('eval(function(p,a,c,k,e,')
                endidx = code.find('hunterobfuscator =')
                code = code[startidx:endidx]
                if not code.replace(' ', '').startswith('eval(function(p,a,c,k,e,'):
                    code = 'fail'
                break
            else:
                code = 'fail'
        else:
            code = 'fail'
    if code != 'fail':
        unpacked = jsunpack.unpack(code)
        video_location = unpacked[unpacked.rfind('http'):unpacked.rfind('m3u8')+4]
        play_item = xbmcgui.ListItem(path=video_location + '|User-Agent=%s' % client.agent())
        xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)
    else:
        xbmcgui.Dialog().ok('Sorry', 'Could not deobfuscate the code.')


def router(params):
    if params:
        if params['mode'][0] == 'shows':
            list_shows()
        elif params['mode'][0] == 'cable':
            list_cable()
        elif params['mode'][0] == 'movies':
            list_movies()
        elif params['mode'][0] == 'play':
            play_video(params['selection'][0])
    else:
        list_categories()


if __name__ == '__main__':
    router(args)
