# -*- coding: utf-8 -*-
# --[ acronaitv v1.0 ]--|--[ From JewBMX ]--
# IPTV Indexer made from the Alberto_Posadas ArconaiTV Plugin.
# Remade/Updated all the json files and each item as of Aug. 11th, 2019.
# Some Artwork is hosted on my repos.

import os.path, requests, json
import sys, urllib, urllib2, urlparse
import xbmcaddon, xbmcgui, xbmcplugin
from resources.lib.modules import jsunpack, control
from bs4 import BeautifulSoup

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
action = args.get('action', None)


class acronaitv:
    def __init__(self):
        self.artbase_url = "https://github.com/jewbmx/xml/blob/master/img/arconaitv/%s?raw=true"
        self.arconaitv_url = "https://www.arconaitv.us/"

    def build_url(self, query):
        return base_url + '?' + urllib.urlencode(query)

    def getCableInfo(self, title):
        desc_file = os.path.join(os.path.dirname(__file__), 'cable.json')
        with open(desc_file) as file:
            data = file.read()
        parsed = json.loads(data)
        for cable in parsed['cable']:
            if title == cable['title']:
                return cable
        return {'title': title, 'description': 'New Channel!', 'poster':' DefaultVideo.png'}

    def getShowInfo(self, title):
        desc_file = os.path.join(os.path.dirname(__file__), 'shows.json')
        with open(desc_file) as file:
            data = file.read()
        parsed = json.loads(data)
        for show in parsed['shows']:
            if title == show['title']:
                return show
        return {'title': title, 'description': 'New Show!', 'poster': 'DefaultVideo.png'}

    def getMovieInfo(self, title):
        desc_file = os.path.join(os.path.dirname(__file__), 'movies.json')
        with open(desc_file) as file:
            data = file.read()
        parsed = json.loads(data)
        for movie in parsed['movies']:
            if title == movie['title']:
                return movie
        return {'title': title, 'description': 'New Movie!', 'poster': 'DefaultVideo.png'}

    def list_categories(self):
        # url = self.build_url({'action': 'arconai_cable'})
        # li = xbmcgui.ListItem("Live TV Channels")
        # cable_img = self.artbase_url % "arconaiCable.png"  ##############
        # li.setArt({'thumb': cable_img, 'poster': cable_img})
        # il={"plot": "Live TV Channels" }
        # li.setInfo(type='Video', infoLabels=il)
        # xbmcplugin.addDirectoryItem(addon_handle, url=url, listitem=li, isFolder=True)

        url = self.build_url({'action': 'arconai_shows'})
        li = xbmcgui.ListItem("TV Shows")
        shows_img = self.artbase_url % "arconaiShows.png"  ##############
        li.setArt({'thumb': shows_img, 'poster': shows_img})
        il = {"plot": "24/7 Tv Shows"}
        li.setInfo(type='Video', infoLabels=il)
        xbmcplugin.addDirectoryItem(addon_handle, url=url, listitem=li, isFolder=True)

        url = self.build_url({'action': 'arconai_movies'})
        li = xbmcgui.ListItem("Movies")
        movies_img = self.artbase_url % "arconaiMovies.png"  ##############
        li.setArt({'thumb': movies_img, 'poster': movies_img})
        il = {"plot": "24/7 Movies"}
        li.setInfo(type='Video', infoLabels=il)
        xbmcplugin.addDirectoryItem(addon_handle, url=url, listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)

    def list_cable(self):
        arconaitv_r = requests.get(self.arconaitv_url + "index.php")
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
            url = self.build_url({'action': 'arconai_play', 'selection': box.a["href"]})
            title = box.a["title"].strip()
            cableInfo = self.getCableInfo(title)
            li = xbmcgui.ListItem(title, iconImage=cableInfo['poster'])
            il = {"Title": title, "mediatype": "video", "plot": cableInfo['description'], "plotoutline": cableInfo['description']}
            li.setProperty('IsPlayable', 'true')
            li.setInfo(type='Video', infoLabels=il)
            listItemlist.append([url, li, False])
        listLength = len(listItemlist)
        xbmcplugin.addDirectoryItems(addon_handle, items=listItemlist, totalItems=listLength)
        xbmcplugin.setContent(addon_handle, 'tvshows')
        xbmcplugin.endOfDirectory(addon_handle)

    def list_shows(self):
        arconaitv_r = requests.get(self.arconaitv_url + "index.php")
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
            url = self.build_url({'action': 'arconai_play', 'selection': box.a["href"]})
            title = box.a["title"].strip()
            showInfo = self.getShowInfo(title)
            li = xbmcgui.ListItem(showInfo['title'], iconImage=showInfo['poster'])
            il = {"Title": title, "mediatype": "video", "plot": showInfo['description'], "plotoutline": showInfo['description']}
            li.setProperty('IsPlayable', 'true')
            li.setInfo(type='Video', infoLabels=il)
            li.setArt({'poster': showInfo['poster'], 'banner': showInfo['poster']})
            listItemlist.append([url, li, False])
        listLength = len(listItemlist)
        xbmcplugin.addDirectoryItems(addon_handle, items=listItemlist, totalItems=listLength)
        xbmcplugin.setContent(addon_handle, 'tvshows')
        xbmcplugin.endOfDirectory(addon_handle)
        control.idle()

    def list_movies(self):
        arconaitv_r = requests.get(self.arconaitv_url + "index.php")
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
            url = self.build_url({'action': 'arconai_play', 'selection': box.a["href"]})
            title = box.a["title"].strip()
            movieInfo = self.getMovieInfo(title)
            li = xbmcgui.ListItem(movieInfo['title'], iconImage=movieInfo['poster'])
            il = {"Title": title, "mediatype":"video", "plot": movieInfo['description'], "plotoutline": movieInfo['description']}
            li.setProperty('IsPlayable', 'True')
            li.setProperty('mimetype', 'application/x-mpegURL') 
            li.setInfo(type='Video', infoLabels=il)
            li.setArt({'poster': movieInfo['poster'], 'banner': movieInfo['poster']})
            listItemlist.append([url, li, False])
        listLength = len(listItemlist)
        xbmcplugin.addDirectoryItems(addon_handle, items=listItemlist, totalItems=listLength)
        xbmcplugin.setContent(addon_handle, 'movies')
        xbmcplugin.endOfDirectory(addon_handle)
        control.idle()

    def play_video(self, selection):
        USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
        r = requests.get(self.arconaitv_url + selection)
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
            play_item = xbmcgui.ListItem(path=video_location + '|User-Agent=%s' % urllib2.quote(USER_AGENT, safe=''))
            xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)
        else:
            xbmcgui.Dialog().ok('Sorry', 'Could not deobfuscate the code.')
