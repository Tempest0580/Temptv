# -*- coding: utf-8 -*-

import os,re,sys,hashlib,urllib,urlparse,json,base64,random,datetime,xbmc
from resources.lib.modules import cache,client,control,metacache,regex
from resources.lib.modules import views,workers,youtube,trailer
from resources.lib.modules import debrid, trakt

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database


class indexer:
    def __init__(self):
        self.list = []
        self.list2 = []
        self.hash = []

        self.tm_user = control.setting('tm.user')
        self.fanart_tv_user = control.setting('fanart.tv.user')
        self.fanart_tv_art_link = 'https://webservice.fanart.tv/v3/tv/%s'
        self.fanart_tv_level_link = 'https://webservice.fanart.tv/v3/level'
        self.fanart_movie_art_link = 'https://webservice.fanart.tv/v3/movies/%s'
        self.fanart_movie_level_link = 'https://webservice.fanart.tv/v3/level'
        self.tm_art_link = 'https://api.themoviedb.org/3/movie/%s/images?api_key=%s&language=en-US&include_image_language=en,en,null' % ('%s', self.tm_user)
        self.tm_img_link = 'https://image.tmdb.org/t/p/w%s%s'
        self.tvdb_key = control.setting('tvdb.user')
        self.tvdb_image = 'https://thetvdb.com/banners/'
        self.tvdb_info_link = 'http://thetvdb.com/api/%s/series/%s/en.xml' % (self.tvdb_key, '%s')
        self.tvdb_ep_info_link = 'http://thetvdb.com/api/%s/episodes/%s/en.xml' % (self.tvdb_key, '%s')

    def entertainment(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9pcHR2LW9yZy5naXRodWIuaW8vaXB0di9jb3VudHJpZXMvdXMubTN1'.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def allsprk(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvYWxsc3Byay5tM3U='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def foreign(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvZm9yZWlnbi54bWw='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def movies(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvbW92aWVzLm0zdQ=='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def kids(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIva2lkcy5tM3U='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def sports(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvc3BvcnRzLm0zdQ=='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def news(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvbmV3cy5tM3U='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def all_english(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvYWxsX2VuZ2xpc2gubTN1'.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def tvnow(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvMTIzdHZub3cubTN1'.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def music(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvbXVzaWMubTN1'.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def hour24(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvMjQtNy5tM3U='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def theaters(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvdGhlYXRlci54bWw='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def pluto(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvcGx1dG8ubTN1'.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def foreign(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvZm9yZWlnbi54bWw='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def testing(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvdGVzdGluZ19zdHVmZi54bWw='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def clicks(self):
        try:
            if debrid.status() is False:
                import xbmcgui
                xbmcgui.Dialog().ok('Debrid Account is Required', 'Please Enable Debrid in the settings')
                return
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvZGVicmlkX2NsaWNrcy9jbGlja3MueG1s'.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def free_clicks(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvZnJlZV9jbGlja3MvY2xpY2tzLnhtbA=='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def shows(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvbWFpblNob3dzLnhtbA=='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def rootXXX(self):
        try:
            if control.setting('Show_Adult') == 'false':
                import xbmcgui
                xbmcgui.Dialog().ok('Adults Only 18+', 'If Your 18 or Older Enable Adult Channels in Settings')
                return
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvYWR1bHQubTN1'.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def get(self, url):
        try:
            self.list = self.noname_list(url)
            self.worker()
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def getq(self, url):
        try:
            self.list = self.noname_list(url)
            self.worker()
            self.addDirectory(self.list, queue=True)
            return self.list
        except:
            pass

    def getx(self, url, worker=False):
        try:
            r, x = re.findall('(.+?)\|regex=(.+?)$', url)[0]
            x = regex.fetch(x)
            r += urllib.unquote_plus(x)
            url = regex.resolve(r)
            self.list = self.noname_list('', result=url)
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def youtube(self, url, action):
        try:
            key = trailer.trailer().key_link.split('=', 1)[-1]
            if 'PlaylistTuner' in action:
                self.list = cache.get(youtube.youtube(key=key).playlist, 1, url)
            elif 'Playlist' in action:
                self.list = cache.get(youtube.youtube(key=key).playlist, 1, url, True)
            elif 'ChannelTuner' in action:
                self.list = cache.get(youtube.youtube(key=key).videos, 1, url)
            elif 'Channel' in action:
                self.list = cache.get(youtube.youtube(key=key).videos, 1, url, True)
            if 'Tuner' in action:
                for i in self.list:
                    i.update({'name': i['title'], 'poster': i['image'], 'action': 'plugin', 'folder': False})
                if 'Tuner2' in action:
                    self.list = sorted(self.list, key=lambda x: random.random())
                self.addDirectory(self.list, queue=True)
            else:
                for i in self.list:
                    i.update({'name': i['title'], 'poster': i['image'], 'nextaction': action, 'action': 'lists_play', 'folder': False})
                self.addDirectory(self.list)
            return self.list
        except:
            pass

    def tvtuner(self, url):
        try:
            preset = re.findall('<preset>(.+?)</preset>', url)[0]
            today = (datetime.datetime.utcnow() - datetime.timedelta(hours = 5)).strftime('%Y-%m-%d')
            today = int(re.sub('[^0-9]', '', str(today)))
            url, imdb, tvdb, tvshowtitle, year, thumbnail, fanart = re.findall('<url>(.+?)</url>', url)[0], re.findall('<imdb>(.+?)</imdb>', url)[0], re.findall('<tvdb>(.+?)</tvdb>', url)[0], re.findall('<tvshowtitle>(.+?)</tvshowtitle>', url)[0], re.findall('<year>(.+?)</year>', url)[0], re.findall('<thumbnail>(.+?)</thumbnail>', url)[0], re.findall('<fanart>(.+?)</fanart>', url)[0]
            tvm = client.request('https://api.tvmaze.com/lookup/shows?thetvdb=%s' % tvdb)
            if tvm  is None:
                tvm = client.request('https://api.tvmaze.com/lookup/shows?imdb=%s' % imdb)
            tvm = 'https://api.tvmaze.com/shows/%s/episodes' % str(json.loads(tvm).get('id'))
            items = json.loads(client.getHTML(tvm))
            items = [(str(i.get('season')), str(i.get('number')), i.get('name').strip(), i.get('airdate')) for i in items]
            if preset == 'tvtuner':
                choice = random.choice(items)
                items = items[items.index(choice):] + items[:items.index(choice)]
                items = items[:100]
            result = ''
            for i in items:
                try:
                    if int(re.sub('[^0-9]', '', str(i[3]))) > today:
                        raise Exception()
                    result += '<item><title> %01dx%02d . %s</title><meta><content>episode</content><imdb>%s</imdb><tvdb>%s</tvdb><tvshowtitle>%s</tvshowtitle><year>%s</year><title>%s</title><premiered>%s</premiered><season>%01d</season><episode>%01d</episode></meta><link><sublink>search</sublink><sublink>searchsd</sublink></link><thumbnail>%s</thumbnail><fanart>%s</fanart></item>' % (int(i[0]), int(i[1]), i[2], imdb, tvdb, tvshowtitle, year, i[2], i[3], int(i[0]), int(i[1]), thumbnail, fanart)
                except:
                    pass
            result = re.sub(r'[^\x00-\x7F]+', ' ', result)
            if preset == 'tvtuner':
                result = result.replace('<sublink>searchsd</sublink>', '')
            self.list = self.noname_list('', result=result)
            if preset == 'tvtuner':
                self.addDirectory(self.list, queue=True)
            else:
                self.worker()
                self.addDirectory(self.list)
        except:
            pass

    def search(self, url):
        try:
            mark = False
            if url is None or url == '':
                self.list = [{'name': 30702, 'action': 'addSearch'}]
                self.list += [{'name': 30703, 'action': 'delSearch'}]
            else:
                if '|SECTION|' in url:
                    mark = url.split('|SECTION|')[0]
                self.list = [{'name': 30702, 'url': url, 'action': 'addSearch'}]
                self.list += [{'name': 30703, 'action': 'delSearch'}]
            try:
                def search():
                    return
                query = cache.get(search, 600000000, table='rel_srch')
                for url in query:
                    if mark != False:
                        if mark in url:
                            name = url.split('|SPLITER|')[0]
                            try:
                                self.list += [{'name': '%s...' % name, 'url': url, 'action': 'addSearch'}]
                            except:
                                pass
                    else:
                        if '|SPLITER|' not in url:
                            try:
                                self.list += [{'name': '%s...' % url, 'url': url, 'action': 'addSearch'}]
                            except:
                                pass
            except:
                pass
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def delSearch(self):
        try:
            cache.clear('rel_srch')
            control.refresh()
        except:
            pass

    def addSearch(self, url):
            try:
                skip = 0
                if '|SPLITER|' in url:
                    keep = url
                    url, matcher = url.split('|SPLITER|')
                    skip = 1
                    section = 1
                elif '|SECTION|' in url:
                    matcher = url.replace('|SECTION|','')
                    section = 1
                else: 
                    section = 0
            except:
                section = 0
            link = 'http://'
            if skip == 0:
                if section == 1:
                    keyboard = control.keyboard('', control.lang(30702).encode('utf-8'))
                    keyboard.doModal()
                    if not (keyboard.isConfirmed()):
                        return
                    url = keyboard.getText()
                    keep = url + '|SPLITER|' + matcher
                else:
                    if url is None or url == '':
                        keyboard = control.keyboard('', control.lang(30702).encode('utf-8'))
                        keyboard.doModal()
                        if not (keyboard.isConfirmed()):
                            return
                        url = keyboard.getText()
            if url is None or url == '':
                return
            if section == 1:
                input = keep
            else: 
                input = url

            def search():
                return [input]
            query = cache.get(search, 600000000, table='rel_srch')

            def search():
                return [x for y, x in enumerate((query + [input])) if x not in (query + [input])[:y]]
            cache.get(search, 0, table='rel_srch')
            links = client.getHTML(link)
            links = re.findall('<link>(.+?)</link>', links)
            if section == 0:
                links = [i for i in links if str(i).startswith('http')]
            else:
                links = [i for i in links if str(i).startswith('http') and matcher.lower() in str(i).lower()]
            self.list = [] ; threads = [] 
            for link in links:
                threads.append(workers.Thread(self.noname_list, link))
            [i.start() for i in threads] ; [i.join() for i in threads]
            self.list = [i for i in self.list if url.lower() in i['name'].lower()]
            for i in self.list:
                try:
                    name = ''
                    if not i['vip'] in ['No-Name TV']:
                        name += '[B]%s[/B] | ' % i['vip'].upper()
                    name += i['name']
                    i.update({'name': name})
                except:
                    pass
            for i in self.list:
                i.update({'content': 'videos'})
            self.addDirectory(self.list)

    def noname_list(self, url, result=None):
        try:
            if result is None:
                result = cache.get(client.request, 0, url)
            if result.strip().startswith('#EXTM3U') and '#EXTINF' in result:
                try:
                    result = re.compile('#.+? tvg-logo="(.+?)" .+?",(.+?)\n(.+?)\n', re.MULTILINE|re.DOTALL).findall(result)
                    result = ['<item><thumbnail>%s</thumbnail><title>%s</title><link>%s</link></item>' % (i[0], i[1], i[2]) for i in result]
                    result = ''.join(result)
                except:
                    result = re.compile('#EXTINF:.+?\,(.+?)\n(.+?)\n', re.MULTILINE|re.DOTALL).findall(result)
                    result = ['<item><title>%s</title><link>%s</link></item>' % (i[0], i[1]) for i in result]
                    result = ''.join(result)
            try:
                r = base64.b64decode(result)
            except:
                r = ''
            if '</link>' in r:
                result = r
            result = str(result)
            info = result.split('<item>')[0].split('<dir>')[0]
            try:
                vip = re.findall('<poster>(.+?)</poster>', info)[0]
            except:
                vip = '0'
            try:
                image = re.findall('<thumbnail>(.+?)</thumbnail>', info)[0]
            except:
                image = '0'
            try:
                fanart = re.findall('<fanart>(.+?)</fanart>', info)[0]
            except:
                fanart = '0'
            api_data = client.request(base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2pld2JteC94bWwvbWFzdGVyL2xpc3RzL2FwaS50eHQ='), timeout='5')
            tmdb_api = re.compile('<api>(.+?)</api>').findall(api_data)[0]
            items = re.compile('((?:<item>.+?</item>|<dir>.+?</dir>|<plugin>.+?</plugin>|<info>.+?</info>|<name>[^<]+</name><link>[^<]+</link><thumbnail>[^<]+</thumbnail><mode>[^<]+</mode>|<name>[^<]+</name><link>[^<]+</link><thumbnail>[^<]+</thumbnail><date>[^<]+</date>))', re.MULTILINE|re.DOTALL).findall(result)
        except:
            return
        for item in items:
            try:
                regdata = re.compile('(<regex>.+?</regex>)', re.MULTILINE|re.DOTALL).findall(item)
                regdata = ''.join(regdata)
                reglist = re.compile('(<listrepeat>.+?</listrepeat>)', re.MULTILINE|re.DOTALL).findall(regdata)
                regdata = urllib.quote_plus(regdata)
                reghash = hashlib.md5()
                for i in regdata:
                    reghash.update(str(i))
                reghash = str(reghash.hexdigest())
                item = item.replace('\r' ,'').replace('\n', '').replace('\t', '').replace('&nbsp;', '').replace('<tmdb_data>true</tmdb_data>','<tmdb_data>all</tmdb_data>')
                try:
                    meta = re.findall('<meta>(.+?)</meta>', item)[0]
                except:
                    meta = '0'
                try:
                    imdb = re.findall('<imdb>(.+?)</imdb>', meta)[0]
                except:
                    imdb = '0'
                try:
                    tmdb_get = re.findall('<tmdb_data>(.+?)</tmdb_data>', meta)[0]
                except:
                    tmdb_get = '0'
                try:
                    tvshowtitle = re.findall('<tvshowtitle>(.+?)</tvshowtitle>', item)[0]
                except:
                    tvshowtitle = '0'
                item = re.sub('<regex>.+?</regex>','', item)
                item = re.sub('<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>','', item)
                item = re.sub('<link></link>','', item)
                try:
                    meta = re.findall('<meta>(.+?)</meta>', item)[0]
                except:
                    meta = '0'
                if any(f for f in ['all','data','images'] if f == tmdb_get.lower()):         
                    try:
                        url_api = 'https://api.themoviedb.org/3/movie/' + imdb + '?api_key=' + tmdb_api
                        item_json = client.request(url_api, timeout='5')
                        item_json = json.loads(item_json)
                    except: pass
                    if any(f for f in ['all','data'] if f == tmdb_get.lower()):         
                        try:
                            if item_json['original_title'] is not None: 
                               title = item_json['original_title']
                               name = title
                            else:        
                                name = re.sub('<meta>.+?</meta>','', item)
                                try:
                                    name = re.findall('<title>(.+?)</title>', name)[0]
                                except:
                                    name = re.findall('<name>(.+?)</name>', name)[0]
                                try:
                                    title = name
                                except:
                                    title = '0'
                                if title == '0' and not tvshowtitle == '0':
                                    title = tvshowtitle
                        except:
                            name = re.sub('<meta>.+?</meta>','', item)
                            try:
                                name = re.findall('<title>(.+?)</title>', name)[0]
                            except:
                                name = re.findall('<name>(.+?)</name>', name)[0]
                            try:
                                title = name
                            except:
                                title = '0'
                            if title == '0' and not tvshowtitle == '0':
                                title = tvshowtitle
                        if '<title></title>' in item:
                            item = item.replace('<title></title>','<title>'+title+'</title>')
                        try:
                            if item_json['release_date'] is not None:
                                year = item_json['release_date']; year = year.split('-')[0]; name = title + ' (' + year + ')'
                            else: 
                                try:
                                    year = re.findall('<year>(.+?)</year>', meta)[0]
                                except:
                                    year = '0'
                        except:
                            try:
                                year = re.findall('<year>(.+?)</year>', meta)[0]
                            except:
                                year = '0'
                        if '<year></year>' in item:
                            item = item.replace('<year></year>','<year>'+title+'</year>')
                    else:
                        name = re.sub('<meta>.+?</meta>','', item)
                        try:
                            name = re.findall('<title>(.+?)</title>', name)[0]
                        except:
                            name = re.findall('<name>(.+?)</name>', name)[0]
                        try:
                            title = name
                        except:
                            title = '0'
                        if '<title></title>' in item:
                            item = item.replace('<title></title>','<title>'+title+'</title>')
                        try:
                            year = re.findall('<year>(.+?)</year>', meta)[0]
                        except:
                            year = '0'
                        if '<year></year>' in item:
                            item = item.replace('<year></year>','<year>'+title+'</year>')
                    if any(f for f in ['all','images'] if f == tmdb_get.lower()):         
                        try:
                            if item_json['backdrop_path'] is not None:
                                fanart2 = 'http://image.tmdb.org/t/p/original/' + item_json['backdrop_path']
                            else: 
                                try:
                                    fanart2 = re.findall('<fanart>(.+?)</fanart>', item)[0]
                                except:
                                    fanart2 = fanart
                        except:
                            try:
                                fanart2 = re.findall('<fanart>(.+?)</fanart>', item)[0]
                            except:
                                fanart2 = fanart
                        try:
                            if item_json['poster_path'] is not None:
                                image2 = 'http://image.tmdb.org/t/p/original/' + item_json['poster_path']
                            else: 
                                try:
                                    image2 = re.findall('<thumbnail>(.+?)</thumbnail>', item)[0]
                                except:
                                    image2 = image
                        except:
                            try:
                                image2 = re.findall('<thumbnail>(.+?)</thumbnail>', item)[0]
                            except:
                                image2 = image
                    else:
                        try:
                            fanart2 = re.findall('<fanart>(.+?)</fanart>', item)[0]
                        except:
                            fanart2 = fanart
                        try:
                            image2 = re.findall('<thumbnail>(.+?)</thumbnail>', item)[0]
                        except:
                            image2 = image
                else:
                    name = re.sub('<meta>.+?</meta>','', item)
                    try:
                        name = re.findall('<title>(.+?)</title>', name)[0]
                    except:
                        name = re.findall('<name>(.+?)</name>', name)[0]
                    try:
                        title = re.findall('<title>(.+?)</title>', meta)[0]
                    except:
                        title = '0'
                    if title == '0' and not tvshowtitle == '0':
                        title = tvshowtitle
                    try:
                        year = re.findall('<year>(.+?)</year>', meta)[0]
                    except:
                        year = '0'
                    try:
                        image2 = re.findall('<thumbnail>(.+?)</thumbnail>', item)[0]
                    except:
                        image2 = image
                    try:
                        fanart2 = re.findall('<fanart>(.+?)</fanart>', item)[0]
                    except:
                        fanart2 = fanart
                try:
                    date = re.findall('<date>(.+?)</date>', item)[0]
                except:
                    date = ''
                if re.search(r'\d+', date):
                    name += ' [COLOR red] Updated %s[/COLOR]' % date
                try:
                    meta = re.findall('<meta>(.+?)</meta>', item)[0]
                except:
                    meta = '0'
                try:
                    url = re.findall('<link>(.+?)</link>', item)[0]
                except:
                    url = '0'
                url = url.replace('>search<', '><preset>search</preset>%s<' % meta)
                url = '<preset>search</preset>%s' % meta if url == 'search' else url
                url = url.replace('>searchsd<', '><preset>searchsd</preset>%s<' % meta)
                url = '<preset>searchsd</preset>%s' % meta if url == 'searchsd' else url
                url = re.sub('<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>','', url)
                if item.startswith('<item>'):
                    action = 'lists_play'
                elif item.startswith('<plugin>'):
                    action = 'plugin'
                elif item.startswith('<info>') or url == '0':
                    action = '0'
                else:
                    action = 'directory'
                if action == 'lists_play' and reglist:
                    action = 'xdirectory'
                if not regdata == '':
                    self.hash.append({'regex': reghash, 'response': regdata})
                    url += '|regex=%s' % reghash
                if action in ['directory', 'xdirectory', 'plugin']:
                    folder = True
                else:
                    folder = False
                try:
                    content = re.findall('<content>(.+?)</content>', meta)[0]
                except:
                    content = '0'
                if content == '0': 
                    try:
                        content = re.findall('<content>(.+?)</content>', item)[0]
                    except:
                        content = '0'
                if not content == '0':
                    content += 's'
                if 'tvshow' in content and not url.strip().endswith('.xml'):
                    url = '<preset>tvindexer</preset><url>%s</url><thumbnail>%s</thumbnail><fanart>%s</fanart>%s' % (url, image2, fanart2, meta)
                    action = 'tvtuner'
                if 'tvtuner' in content and not url.strip().endswith('.xml'):
                    url = '<preset>tvtuner</preset><url>%s</url><thumbnail>%s</thumbnail><fanart>%s</fanart>%s' % (url, image2, fanart2, meta)
                    action = 'tvtuner'
                try:
                    tvdb = re.findall('<tvdb>(.+?)</tvdb>', meta)[0]
                except:
                    tvdb = '0'
                try:
                    premiered = re.findall('<premiered>(.+?)</premiered>', meta)[0]
                except:
                    premiered = '0'
                try:
                    seasons = re.findall('<season>(.+?)</season>', meta)[0]
                except:
                    seasons = '0'
                try:
                    episode = re.findall('<episode>(.+?)</episode>', meta)[0]
                except:
                    episode = '0'
                self.list2.append({'poster': image2, 'tvdb': tvdb})
                self.list.append({'name': name, 'vip': vip, 'url': url, 'action': action, 'folder': folder, 'poster': image2, 'banner': '0', 'fanart': fanart2, 'content': content, 'imdb': imdb, 'tvdb': tvdb, 'tmdb': '0', 'title': title, 'originaltitle': title, 'tvshowtitle': tvshowtitle, 'year': year, 'premiered': premiered, 'seasons': seasons, 'episode': episode})
            except:
                pass            
        regex.insert(self.hash)
        return self.list

    def worker(self):
        self.fanart_tv_headers = {'api-key': 'db10619c97af83891690f4cfd7205d62'}
        if not self.fanart_tv_user == '':
            self.fanart_tv_headers.update({'client-key': self.fanart_tv_user})
        self.lang = 'en'
        self.meta = []
        total = len(self.list)
        if total == 0:
            return
        for i in range(0, total):
            self.list[i].update({'metacache': False})
        self.list = metacache.fetch(self.list, self.lang)
        multi = [i['imdb'] for i in self.list]
        multi = [x for y, x in enumerate(multi) if x not in multi[:y]]
        if len(multi) == 1:
                self.movie_info(0); self.tv_info(0); self.tv_info2(0); self.tv_info3(0)
                if self.meta:
                    metacache.insert(self.meta)
        for i in range(0, total):
            self.list[i].update({'metacache': False})
        self.list = metacache.fetch(self.list, self.lang)
        for r in range(0, total, 50):
            threads = []
            for i in range(r, r+50):
                if i <= total:
                    threads.append(workers.Thread(self.movie_info, i))
                if i <= total:
                    threads.append(workers.Thread(self.tv_info, i))
                if i <= total:
                    threads.append(workers.Thread(self.tv_info2, i))
                if i <= total:
                    threads.append(workers.Thread(self.tv_info3, i))
            [i.start() for i in threads]
            [i.join() for i in threads]
        if self.meta:
            metacache.insert(self.meta)

        self.list = metacache.local(self.list, self.tm_img_link, 'poster3', 'fanart2')

    def movie_info(self, i):
        try:
            if not self.list[i]['content'] == 'movies':
                raise Exception()
            imdb = self.list[i]['imdb']
            if imdb == '0':
                raise Exception()
            item = trakt.getMovieSummary(imdb)

            title = item.get('title')
            title = client.replaceHTMLCodes(title)

            originaltitle = title

            year = item.get('year', 0)
            year = re.sub('[^0-9]', '', str(year))

            imdb = item.get('ids', {}).get('imdb', '0')
            imdb = 'tt' + re.sub('[^0-9]', '', str(imdb))

            tmdb = str(item.get('ids', {}).get('tmdb', 0))

            premiered = item.get('released', '0')
            try:
                premiered = re.compile('(\d{4}-\d{2}-\d{2})').findall(premiered)[0]
            except:
                premiered = '0'

            genre = item.get('genres', [])
            genre = [x.title() for x in genre]
            genre = ' / '.join(genre).strip()
            if not genre:
                genre = '0'

            duration = str(item.get('runtime', 0))
            duration = str(int(duration) * 60)

            rating = item.get('rating', '0')
            if not rating or rating == '0.0':
                rating = '0'

            votes = item.get('votes', '0')
            try:
                votes = str(format(int(votes), ',d'))
            except:
                pass

            mpaa = item.get('certification', '0')
            if not mpaa:
                mpaa = '0'

            tagline = item.get('tagline', '0')

            plot = item.get('overview', '0')

            people = trakt.getPeople(imdb, 'movies')

            director = writer = ''
            if 'crew' in people and 'directing' in people['crew']:
                director = ', '.join([director['person']['name'] for director in people['crew']['directing'] if director['job'].lower() == 'director'])
            if 'crew' in people and 'writing' in people['crew']:
                writer = ', '.join([writer['person']['name'] for writer in people['crew']['writing'] if writer['job'].lower() in ['writer', 'screenplay', 'author']])

            cast = []
            for person in people.get('cast', []):
                cast.append({'name': person['person']['name'], 'role': person['character']})
            cast = [(person['name'], person['role']) for person in cast]

            try:
                if self.lang == 'en' or self.lang not in item.get('available_translations', [self.lang]):
                    raise Exception()

                trans_item = trakt.getMovieTranslation(imdb, self.lang, full=True)

                title = trans_item.get('title') or title
                tagline = trans_item.get('tagline') or tagline
                plot = trans_item.get('overview') or plot
            except:
                pass

            try:
                artmeta = True
                art = client.request(self.fanart_movie_art_link % imdb, headers=self.fanart_tv_headers, timeout='10', error=True)
                try:
                    art = json.loads(art)
                except:
                    artmeta = False
            except:
                pass

            try:
                poster2 = art['movieposter']
                poster2 = [x for x in poster2 if x.get('lang') == self.lang][::-1] + [x for x in poster2 if x.get('lang') == 'en'][::-1] + [x for x in poster2 if x.get('lang') in ['00', '']][::-1]
                poster2 = poster2[0]['url'].encode('utf-8')
            except:
                poster2 = '0'

            try:
                if 'moviebackground' in art: fanart = art['moviebackground']
                else: fanart = art['moviethumb']
                fanart = [x for x in fanart if x.get('lang') == self.lang][::-1] + [x for x in fanart if x.get('lang') == 'en'][::-1] + [x for x in fanart if x.get('lang') in ['00', '']][::-1]
                fanart = fanart[0]['url'].encode('utf-8')
            except:
                fanart = '0'

            try:
                banner = art['moviebanner']
                banner = [x for x in banner if x.get('lang') == self.lang][::-1] + [x for x in banner if x.get('lang') == 'en'][::-1] + [x for x in banner if x.get('lang') in ['00', '']][::-1]
                banner = banner[0]['url'].encode('utf-8')
            except:
                banner = '0'

            try:
                if 'hdmovielogo' in art: clearlogo = art['hdmovielogo']
                else: clearlogo = art['clearlogo']
                clearlogo = [x for x in clearlogo if x.get('lang') == self.lang][::-1] + [x for x in clearlogo if x.get('lang') == 'en'][::-1] + [x for x in clearlogo if x.get('lang') in ['00', '']][::-1]
                clearlogo = clearlogo[0]['url'].encode('utf-8')
            except:
                clearlogo = '0'

            try:
                if 'hdmovieclearart' in art: clearart = art['hdmovieclearart']
                else: clearart = art['clearart']
                clearart = [x for x in clearart if x.get('lang') == self.lang][::-1] + [x for x in clearart if x.get('lang') == 'en'][::-1] + [x for x in clearart if x.get('lang') in ['00', '']][::-1]
                clearart = clearart[0]['url'].encode('utf-8')
            except:
                clearart = '0'

            try:
                if self.tm_user == '':
                    raise Exception()

                art2 = client.request(self.tm_art_link % imdb, timeout='10', error=True)
                art2 = json.loads(art2)
            except:
                pass

            try:
                poster3 = art2['posters']
                poster3 = [x for x in poster3 if x.get('iso_639_1') == self.lang] + [x for x in poster3 if x.get('iso_639_1') == 'en'] + [x for x in poster3 if x.get('iso_639_1') not in [self.lang, 'en']]
                poster3 = [(x['width'], x['file_path']) for x in poster3]
                poster3 = [(x[0], x[1]) if x[0] < 300 else ('300', x[1]) for x in poster3]
                poster3 = self.tm_img_link % poster3[0]
                poster3 = poster3.encode('utf-8')
            except:
                poster3 = '0'

            try:
                fanart2 = art2['backdrops']
                fanart2 = [x for x in fanart2 if x.get('iso_639_1') == self.lang] + [x for x in fanart2 if x.get('iso_639_1') == 'en'] + [x for x in fanart2 if x.get('iso_639_1') not in [self.lang, 'en']]
                fanart2 = [x for x in fanart2 if x.get('width') == 1920] + [x for x in fanart2 if x.get('width') < 1920]
                fanart2 = [(x['width'], x['file_path']) for x in fanart2]
                fanart2 = [(x[0], x[1]) if x[0] < 1280 else ('1280', x[1]) for x in fanart2]
                fanart2 = self.tm_img_link % fanart2[0]
                fanart2 = fanart2.encode('utf-8')
            except:
                fanart2 = '0'

            item = {'title': title, 'originaltitle': originaltitle, 'year': year, 'imdb': imdb, 'tmdb': tmdb, 'poster': '0', 'poster2': poster2, 'poster3': poster3, 'banner': banner, 'fanart': fanart, 'fanart2': fanart2, 'clearlogo': clearlogo, 'clearart': clearart, 'premiered': premiered, 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'writer': writer, 'cast': cast, 'plot': plot, 'tagline': tagline}
            item = dict((k, v) for k, v in item.iteritems() if not v == '0')
            self.list[i].update(item)

            if artmeta is False:
                raise Exception()

            meta = {'imdb': imdb, 'tmdb': tmdb, 'tvdb': '0', 'lang': self.lang, 'item': item}
            self.meta.append(meta)
        except:
            pass

    def tv_info(self, i):
        try:
            if not self.list[i]['content'] in ['tvshows']:
                raise Exception()
            tvdb = self.list[i]['tvdb']
            if tvdb == '0':
                raise Exception()
            url = self.tvdb_info_link % tvdb
            item = client.getHTML(url)

            try:
                imdb = client.parseDOM(item, 'IMDB_ID')[0]
            except:
                pass
            if imdb == '':
                imdb = '0'
            imdb = imdb.encode('utf-8')

            try:
                title = client.parseDOM(item, 'SeriesName')[0]
            except:
                title = ''
            if title == '':
                title = '0'
            title = client.replaceHTMLCodes(title)
            title = title.encode('utf-8')

            try:
                year = client.parseDOM(item, 'FirstAired')[0]
            except:
                year = ''
            try:
                year = re.compile('(\d{4})').findall(year)[0]
            except:
                year = ''
            if year == '':
                year = '0'
            year = year.encode('utf-8')

            try:
                premiered = client.parseDOM(item, 'FirstAired')[0]
            except:
                premiered = '0'
            if premiered == '':
                premiered = '0'
            premiered = client.replaceHTMLCodes(premiered)
            premiered = premiered.encode('utf-8')

            try:
                studio = client.parseDOM(item, 'Network')[0]
            except:
                studio = ''
            if studio == '':
                studio = '0'
            studio = client.replaceHTMLCodes(studio)
            studio = studio.encode('utf-8')

            try:
                genre = client.parseDOM(item, 'Genre')[0]
            except:
                genre = ''
            genre = [x for x in genre.split('|') if not x == '']
            genre = ' / '.join(genre)
            if genre == '':
                genre = '0'
            genre = client.replaceHTMLCodes(genre)
            genre = genre.encode('utf-8')

            try:
                duration = client.parseDOM(item, 'Runtime')[0]
            except:
                duration = ''
            if duration == '':
                duration = '0'
            duration = client.replaceHTMLCodes(duration)
            duration = duration.encode('utf-8')

            try:
                rating = client.parseDOM(item, 'Rating')[0]
            except:
                rating = ''
            if 'rating' in self.list[i] and not self.list[i]['rating'] == '0':
                rating = self.list[i]['rating']
            if rating == '':
                rating = '0'
            rating = client.replaceHTMLCodes(rating)
            rating = rating.encode('utf-8')

            try:
                votes = client.parseDOM(item, 'RatingCount')[0]
            except:
                votes = ''
            if 'votes' in self.list[i] and not self.list[i]['votes'] == '0':
                votes = self.list[i]['votes']
            if votes == '':
                votes = '0'
            votes = client.replaceHTMLCodes(votes)
            votes = votes.encode('utf-8')

            try:
                mpaa = client.parseDOM(item, 'ContentRating')[0]
            except:
                mpaa = ''
            if mpaa == '':
                mpaa = '0'
            mpaa = client.replaceHTMLCodes(mpaa)
            mpaa = mpaa.encode('utf-8')

            try:
                cast = client.parseDOM(item, 'Actors')[0]
            except:
                cast = ''
            cast = [x for x in cast.split('|') if not x == '']
            try:
                cast = [(x.encode('utf-8'), '') for x in cast]
            except:
                cast = []
            if cast == []:
                cast = '0'

            try:
                plot = client.parseDOM(item, 'Overview')[0]
            except:
                plot = ''
            if plot == '':
                plot = '0'
            plot = client.replaceHTMLCodes(plot)
            plot = plot.encode('utf-8')

            try:
                poster = client.parseDOM(item, 'poster')[0]
            except:
                poster = ''
            if not poster == '':
                poster = self.tvdb_image + poster
            else:
                poster = '0'
            if 'poster' in self.list[i] and poster == '0':
                poster = self.list[i]['poster']
            poster = client.replaceHTMLCodes(poster)
            poster = poster.encode('utf-8')

            try:
                banner = client.parseDOM(item, 'banner')[0]
            except:
                banner = ''
            if not banner == '':
                banner = self.tvdb_image + banner
            else:
                banner = '0'
            banner = client.replaceHTMLCodes(banner)
            banner = banner.encode('utf-8')

            try:
                fanart = client.parseDOM(item, 'fanart')[0]
            except:
                fanart = ''
            if not fanart == '':
                fanart = self.tvdb_image + fanart
            else:
                fanart = '0'
            fanart = client.replaceHTMLCodes(fanart)
            fanart = fanart.encode('utf-8')

            try:
                artmeta = True
                art = client.request(self.fanart_tv_art_link % tvdb, headers=self.fanart_tv_headers, timeout='10', error=True)
                try:
                    art = json.loads(art)
                except:
                    artmeta = False
            except:
                pass

            try:
                poster2 = art['tvposter']
                poster2 = [x for x in poster2 if x.get('lang') == self.lang][::-1] + [x for x in poster2 if x.get('lang') == 'en'][::-1] + [x for x in poster2 if x.get('lang') in ['00', '']][::-1]
                poster2 = poster2[0]['url'].encode('utf-8')
            except:
                poster2 = '0'

            try:
                fanart2 = art['showbackground']
                fanart2 = [x for x in fanart2 if x.get('lang') == self.lang][::-1] + [x for x in fanart2 if x.get('lang') == 'en'][::-1] + [x for x in fanart2 if x.get('lang') in ['00', '']][::-1]
                fanart2 = fanart2[0]['url'].encode('utf-8')
            except:
                fanart2 = '0'

            try:
                banner2 = art['tvbanner']
                banner2 = [x for x in banner2 if x.get('lang') == self.lang][::-1] + [x for x in banner2 if x.get('lang') == 'en'][::-1] + [x for x in banner2 if x.get('lang') in ['00', '']][::-1]
                banner2 = banner2[0]['url'].encode('utf-8')
            except:
                banner2 = '0'

            try:
                if 'hdtvlogo' in art:
                    clearlogo = art['hdtvlogo']
                else:
                    clearlogo = art['clearlogo']
                clearlogo = [x for x in clearlogo if x.get('lang') == self.lang][::-1] + [x for x in clearlogo if x.get('lang') == 'en'][::-1] + [x for x in clearlogo if x.get('lang') in ['00', '']][::-1]
                clearlogo = clearlogo[0]['url'].encode('utf-8')
            except:
                clearlogo = '0'

            try:
                if 'hdclearart' in art:
                    clearart = art['hdclearart']
                else:
                    clearart = art['clearart']
                clearart = [x for x in clearart if x.get('lang') == self.lang][::-1] + [x for x in clearart if x.get('lang') == 'en'][::-1] + [x for x in clearart if x.get('lang') in ['00', '']][::-1]
                clearart = clearart[0]['url'].encode('utf-8')
            except:
                clearart = '0'

            item = {'title': title, 'year': year, 'imdb': imdb, 'tvdb': tvdb, 'poster': poster, 'poster2': poster2, 'banner': banner, 'banner2': banner2, 'fanart': fanart, 'fanart2': fanart2, 'clearlogo': clearlogo, 'clearart': clearart, 'premiered': premiered, 'studio': studio, 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'cast': cast, 'plot': plot}
            item = dict((k, v) for k, v in item.iteritems() if not v == '0')
            self.list[i].update(item)

            if artmeta is False:
                raise Exception()

            meta = {'imdb': imdb, 'tvdb': tvdb, 'lang': self.lang, 'item': item}
            self.meta.append(meta)
        except:
            pass

    def tv_info2(self, i):
        try:
            if not self.list[i]['content'] in ['seasons']:
                raise Exception()

            tvdb = self.list2[i]['tvdb']
            if tvdb == '0':
                raise Exception()
            url = self.tvdb_info_link % tvdb
            item = client.getHTML(url)

            try:
                imdb = client.parseDOM(item, 'IMDB_ID')[0]
            except:
                pass
            if imdb == '':
                imdb = '0'
            imdb = imdb.encode('utf-8')

            try:
                title = client.parseDOM(item, 'SeriesName')[0]
            except:
                title = ''
            if title == '':
                title = '0'
            title = client.replaceHTMLCodes(title)
            title = title.encode('utf-8')

            try:
                year = client.parseDOM(item, 'FirstAired')[0]
            except:
                year = ''
            try:
                year = re.compile('(\d{4})').findall(year)[0]
            except:
                year = ''
            if year == '':
                year = '0'
            year = year.encode('utf-8')

            try:
                premiered = client.parseDOM(item, 'FirstAired')[0]
            except:
                premiered = '0'
            if premiered == '':
                premiered = '0'
            premiered = client.replaceHTMLCodes(premiered)
            premiered = premiered.encode('utf-8')

            try:
                studio = client.parseDOM(item, 'Network')[0]
            except:
                studio = ''
            if studio == '':
                studio = '0'
            studio = client.replaceHTMLCodes(studio)
            studio = studio.encode('utf-8')

            try:
                genre = client.parseDOM(item, 'Genre')[0]
            except:
                genre = ''
            genre = [x for x in genre.split('|') if not x == '']
            genre = ' / '.join(genre)
            if genre == '':
                genre = '0'
            genre = client.replaceHTMLCodes(genre)
            genre = genre.encode('utf-8')

            try:
                duration = client.parseDOM(item, 'Runtime')[0]
            except:
                duration = ''
            if duration == '':
                duration = '0'
            duration = client.replaceHTMLCodes(duration)
            duration = duration.encode('utf-8')

            try:
                rating = client.parseDOM(item, 'Rating')[0]
            except:
                rating = ''
            if 'rating' in self.list[i] and not self.list[i]['rating'] == '0':
                rating = self.list[i]['rating']
            if rating == '':
                rating = '0'
            rating = client.replaceHTMLCodes(rating)
            rating = rating.encode('utf-8')

            try:
                votes = client.parseDOM(item, 'RatingCount')[0]
            except:
                votes = ''
            if 'votes' in self.list[i] and not self.list[i]['votes'] == '0':
                votes = self.list[i]['votes']
            if votes == '':
                votes = '0'
            votes = client.replaceHTMLCodes(votes)
            votes = votes.encode('utf-8')

            try:
                mpaa = client.parseDOM(item, 'ContentRating')[0]
            except:
                mpaa = ''
            if mpaa == '':
                mpaa = '0'
            mpaa = client.replaceHTMLCodes(mpaa)
            mpaa = mpaa.encode('utf-8')

            try:
                cast = client.parseDOM(item, 'Actors')[0]
            except:
                cast = ''
            cast = [x for x in cast.split('|') if not x == '']
            try:
                cast = [(x.encode('utf-8'), '') for x in cast]
            except:
                cast = []
            if cast == []:
                cast = '0'

            try:
                plot = client.parseDOM(item, 'Overview')[0]
            except:
                plot = ''
            if plot == '':
                plot = '0'
            plot = client.replaceHTMLCodes(plot)
            plot = plot.encode('utf-8')

            try:
                status = client.parseDOM(item, 'Status')[0]
            except:
                status = ''
            if status == '':
                status = 'Ended'
            status = client.replaceHTMLCodes(status)
            status = status.encode('utf-8')


            try:
                artmeta = True
                art = client.request(self.fanart_tv_art_link % tvdb, headers=self.fanart_tv_headers, timeout='10', error=True)
                try:
                    art = json.loads(art)
                except:
                    artmeta = False
            except:
                pass
            
            try:
                season = art['seasonposter']
                season = [x for x in season if x.get('lang') == self.lang][::-1] + [x for x in season if x.get('lang') == 'en'][::-1] + [x for x in season if x.get('lang') in ['00', '']][::-1]
                season = [x for x in season if x.get('season') in self.list[i]['seasons']][::-1]
                season = season[0]['url'].encode('utf-8')
            except:
                season = art['tvposter']
                season = [x for x in season if x.get('lang') == self.lang][::-1] + [x for x in season if x.get('lang') == 'en'][::-1] + [x for x in season if x.get('lang') in ['00', '']][::-1]
                season = season[0]['url'].encode('utf-8')


            try:
                fanart2 = art['showbackground']
                fanart2 = [x for x in fanart2 if x.get('lang') == self.lang][::-1] + [x for x in fanart2 if x.get('lang') == 'en'][::-1] + [x for x in fanart2 if x.get('lang') in ['00', '']][::-1]
                fanart2 = fanart2[0]['url'].encode('utf-8')
            except:
                fanart2 = '0'

            try:
                banner2 = art['tvbanner']
                banner2 = [x for x in banner2 if x.get('lang') == self.lang][::-1] + [x for x in banner2 if x.get('lang') == 'en'][::-1] + [x for x in banner2 if x.get('lang') in ['00', '']][::-1]
                banner2 = banner2[0]['url'].encode('utf-8')
            except:
                banner2 = '0'

            try:
                if 'hdtvlogo' in art:
                    clearlogo = art['hdtvlogo']
                else:
                    clearlogo = art['clearlogo']
                clearlogo = [x for x in clearlogo if x.get('lang') == self.lang][::-1] + [x for x in clearlogo if x.get('lang') == 'en'][::-1] + [x for x in clearlogo if x.get('lang') in ['00', '']][::-1]
                clearlogo = clearlogo[0]['url'].encode('utf-8')
            except:
                clearlogo = '0'

            try:
                if 'hdclearart' in art:
                    clearart = art['hdclearart']
                else:
                    clearart = art['clearart']
                clearart = [x for x in clearart if x.get('lang') == self.lang][::-1] + [x for x in clearart if x.get('lang') == 'en'][::-1] + [x for x in clearart if x.get('lang') in ['00', '']][::-1]
                clearart = clearart[0]['url'].encode('utf-8')
            except:
                clearart = '0'

            item = {'title': title, 'year': year, 'imdb': imdb, 'tvdb': tvdb, 'poster': season, 'poster2': '0', 'banner2': banner2, 'fanart': '0', 'fanart2': fanart2, 'clearlogo': clearlogo, 'clearart': clearart, 'premiered': premiered, 'studio': studio, 'genre': genre, 'duration': duration, 'status': status, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'cast': cast, 'plot': plot}
            item = dict((k, v) for k, v in item.iteritems() if not v == '0')
            self.list[i].update(item)

            if artmeta is False:
                raise Exception()

            meta = {'imdb': imdb, 'tvdb': tvdb, 'lang': self.lang, 'item': item}
            self.meta.append(meta)
        except:
            pass

    def tv_info3(self, i):
        try:
            if not self.list[i]['content'] in ['episodes']:
                raise Exception()
            tvdb = self.list2[i]['tvdb']
            if tvdb == '0':
                raise Exception()
            url = self.tvdb_ep_info_link % tvdb
            item = client.getHTML(url)

            try:
                imdb = client.parseDOM(item, 'IMDB_ID')[0]
            except:
                pass
            if imdb == '':
                imdb = '0'
            imdb = imdb.encode('utf-8')

            season = client.parseDOM(item, 'SeasonNumber')[0]
            season = '%01d' % int(season)
            season = season.encode('utf-8')

            episode = client.parseDOM(item, 'EpisodeNumber')[0]
            episode = re.sub('[^0-9]', '', '%01d' % int(episode))
            episode = episode.encode('utf-8')

            try:
                year = client.parseDOM(item, 'FirstAired')[0]
            except:
                year = ''
            try:
                year = re.compile('(\d{4})').findall(year)[0]
            except:
                year = ''
            if year == '':
                year = '0'
            year = year.encode('utf-8')

            try:
                premiered = client.parseDOM(item, 'FirstAired')[0]
            except:
                premiered = '0'
            if premiered == '':
                premiered = '0'
            premiered = client.replaceHTMLCodes(premiered)
            premiered = premiered.encode('utf-8')
    
            try:
                poster = client.parseDOM(item, 'filename')[0]
            except:
                poster = ''
            if not poster == '':
                poster = self.tvdb_image + poster
            else:
                poster = '0'
            if 'poster' in self.list[i] and poster == '0':
                poster = self.list[i]['poster']
            poster = client.replaceHTMLCodes(poster)
            poster = poster.encode('utf-8')

            try:
                showid = client.parseDOM(item, 'seriesid')[0]
                urlid = self.tvdb_info_link % showid
                itemid = client.getHTML(urlid)
                duration = client.parseDOM(itemid, 'Runtime')[0]
            except:
                duration = ''
            if duration == '':
                duration = '0'
            duration = client.replaceHTMLCodes(duration)
            duration = duration.encode('utf-8')

            try:
                showid = client.parseDOM(item, 'seriesid')[0]
                urlid = self.tvdb_info_link % showid
                itemid = client.getHTML(urlid)
                studio = client.parseDOM(itemid, 'Network')[0]
            except:
                studio = ''
            if studio == '':
                studio = '0'
            studio = client.replaceHTMLCodes(studio)
            studio = studio.encode('utf-8')

            try:
                rating = client.parseDOM(item, 'Rating')[0]
            except:
                rating = ''
            if 'rating' in self.list[i] and not self.list[i]['rating'] == '0':
                rating = self.list[i]['rating']
            if rating == '':
                rating = '0'
            rating = client.replaceHTMLCodes(rating)
            rating = rating.encode('utf-8')

            try:
                votes = client.parseDOM(item, 'RatingCount')[0]
            except:
                votes = ''
            if 'votes' in self.list[i] and not self.list[i]['votes'] == '0':
                votes = self.list[i]['votes']
            if votes == '':
                votes = '0'
            votes = client.replaceHTMLCodes(votes)
            votes = votes.encode('utf-8')

            try:
                showid = client.parseDOM(item, 'seriesid')[0]
                urlid = self.tvdb_info_link % showid
                itemid = client.getHTML(urlid)
                status = client.parseDOM(itemid, 'Status')[0]
            except:
                status = ''
            if status == '':
                status = 'Ended'
            status = client.replaceHTMLCodes(status)
            status = status.encode('utf-8')

            try:
                writer = client.parseDOM(item, 'Writer')[0]
            except:
                writer = ''
            writer = [x for x in writer.split('|') if not x == '']
            writer = ' / '.join(writer)
            if writer == '':
                writer = '0'
            writer = client.replaceHTMLCodes(writer)
            writer = writer.encode('utf-8')

            try:
                showid = client.parseDOM(item, 'seriesid')[0]
                urlid = self.tvdb_info_link % showid
                itemid = client.getHTML(urlid)
                cast = client.parseDOM(itemid, 'Actors')[0]
            except:
                cast = ''
            cast = [x for x in cast.split('|') if not x == '']
            try:
                cast = [(x.encode('utf-8'), '') for x in cast]
            except:
                cast = []
            if cast == []:
                cast = '0'

            try:
                plot = client.parseDOM(item, 'Overview')[0]
            except:
                plot = ''
            if plot == '':
                plot = '0'
            plot = client.replaceHTMLCodes(plot)
            plot = plot.encode('utf-8')

            try:
                artmeta = True
                tvdb = client.parseDOM(item, 'seriesid')[0]
                art = client.request(self.fanart_tv_art_link % tvdb, headers=self.fanart_tv_headers, timeout='10', error=True)
                try:
                    art = json.loads(art)
                except:
                    artmeta = False
            except:
                pass

            try:
                fanart2 = art['showbackground']
                fanart2 = [x for x in fanart2 if x.get('lang') == self.lang][::-1] + [x for x in fanart2 if x.get('lang') == 'en'][::-1] + [x for x in fanart2 if x.get('lang') in ['00', '']][::-1]
                fanart2 = fanart2[0]['url'].encode('utf-8')
            except:
                fanart2 = '0'

            try:
                banner2 = art['tvbanner']
                banner2 = [x for x in banner2 if x.get('lang') == self.lang][::-1] + [x for x in banner2 if x.get('lang') == 'en'][::-1] + [x for x in banner2 if x.get('lang') in ['00', '']][::-1]
                banner2 = banner2[0]['url'].encode('utf-8')
            except:
                banner2 = '0'

            try:
                if 'hdtvlogo' in art:
                    clearlogo = art['hdtvlogo']
                else:
                    clearlogo = art['clearlogo']
                clearlogo = [x for x in clearlogo if x.get('lang') == self.lang][::-1] + [x for x in clearlogo if x.get('lang') == 'en'][::-1] + [x for x in clearlogo if x.get('lang') in ['00', '']][::-1]
                clearlogo = clearlogo[0]['url'].encode('utf-8')
            except:
                clearlogo = '0'

            try:
                if 'hdclearart' in art:
                    clearart = art['hdclearart']
                else:
                    clearart = art['clearart']
                clearart = [x for x in clearart if x.get('lang') == self.lang][::-1] + [x for x in clearart if x.get('lang') == 'en'][::-1] + [x for x in clearart if x.get('lang') in ['00', '']][::-1]
                clearart = clearart[0]['url'].encode('utf-8')
            except:
                clearart = '0'

            item = { 'year': year, 'tvdb': tvdb, 'poster': poster, 'poster2': '0', 'banner': '0', 'banner2': banner2, 'fanart': '0', 'fanart': fanart2, 'clearlogo': clearlogo, 'clearart': clearart, 'premiered': premiered, 'studio': studio, 'season': season, 'duration': duration, 'rating': rating, 'writer': writer, 'votes': votes, 'episode': episode, 'cast': cast, 'plot': plot}
            item = dict((k, v) for k, v in item.iteritems() if not v == '0')
            self.list[i].update(item)

            if artmeta is False:
                raise Exception()

            meta = {'imdb': imdb, 'tvdb': tvdb, 'lang': self.lang, 'item': item}
            self.meta.append(meta)
        except:
            pass

    def addDirectory(self, items, queue=False):
        if items is None or len(items) == 0:
            return
        sysaddon = sys.argv[0]
        addonPoster = addonBanner = control.addonInfo('icon')
        addonFanart = control.addonInfo('fanart')
        playlist = control.playlist
        if queue is not False:
            playlist.clear()
        mode = [i['content'] for i in items if 'content' in i]
        if 'movies' in mode:
            mode = 'movies'
        elif 'tvshows' in mode:
            mode = 'tvshows'
        elif 'seasons' in mode:
            mode = 'seasons'
        elif 'episodes' in mode:
            mode = 'episodes'
        elif 'videos' in mode:
            mode = 'videos'
        else:
            mode = 'addons'
        for i in items:
            try:
                year = i['year']
                try:
                    name = control.lang(int(i['title'])).encode('utf-8')
                except:
                    name = i['title']
                    name = name + '  ' + '(%s)' % year
                    if year == '0':
                        name = i['title']
                    if mode == 'seasons' or mode == 'episodes':
                        name = i['name']
                if name == '':
                    name = i['name']
                    name = name + '  ' + '(%s)' % year
                    if year == '0':
                        name = i['name']
                    if mode == 'seasons' or mode == 'episodes':
                        name = i['name']
                url = '%s?action=%s' % (sysaddon, i['action'])
                try:
                    url += '&url=%s' % urllib.quote_plus(i['url'])
                except:
                    pass
                try:
                    url += '&content=%s' % urllib.quote_plus(i['content'])
                except:
                    pass
                if i['action'] == 'plugin' and 'url' in i:
                    url = i['url']
                poster = [i[x] for x in ['poster3', 'poster', 'poster2'] if i.get(x, '0') != '0']
                poster = poster[0] if poster else addonPoster
                banner = i['banner'] if 'banner' in i else '0'
                fanart = i['fanart'] if 'fanart' in i else '0'
                fanart2 = i['fanart2'] if 'fanart2' in i else '0'
                if poster == '0':
                    poster = addonPoster
                if banner == '0' and poster == '0':
                    banner = addonBanner
                elif banner == '0':
                    banner = poster
                content = i['content'] if 'content' in i else '0'
                folder = i['folder'] if 'folder' in i else True
                meta = dict((k, v) for k, v in i.iteritems() if not v == '0')
                cm = []
                if content in ['movies', 'tvshows']:
                    meta.update({'trailer': '%s?action=trailer&name=%s' % (sysaddon, urllib.quote_plus(name))})
                #    cm.append((control.lang(30707).encode('utf-8'), 'RunPlugin(%s?action=trailer&name=%s)' % (sysaddon, urllib.quote_plus(name))))
                if content in ['movies', 'tvshows', 'seasons', 'episodes']:
                    cm.append((control.lang(30708).encode('utf-8'), 'XBMC.Action(Info)'))
                if (folder is False and '|regex=' not in str(i.get('url'))) or (folder is True and content in ['tvshows', 'seasons']):
                    cm.append((control.lang(32065).encode('utf-8'), 'RunPlugin(%s?action=queueItem)' % sysaddon))
                # if content == 'movies':
                #    try:
                #        dfile = '%s (%s)' % (i['title'], i['year'])
                #    except:
                #        dfile = name
                #    try:
                #        cm.append((control.lang(30722).encode('utf-8'), 'RunPlugin(%s?action=addDownload&name=%s&url=%s&image=%s)' % (sysaddon, urllib.quote_plus(dfile), urllib.quote_plus(i['url']), urllib.quote_plus(poster))))
                #    except:
                #        pass
                # elif content == 'episodes':
                #    try:
                #        dfile = '%s S%02dE%02d' % (i['tvshowtitle'], int(i['season']), int(i['episode']))
                #    except:
                #        dfile = name
                #    try:
                #        cm.append((control.lang(30722).encode('utf-8'), 'RunPlugin(%s?action=addDownload&name=%s&url=%s&image=%s)' % (sysaddon, urllib.quote_plus(dfile), urllib.quote_plus(i['url']), urllib.quote_plus(poster))))
                #    except:
                #        pass
                # elif content == 'songs':
                #    try:
                #        cm.append((control.lang(30722).encode('utf-8'), 'RunPlugin(%s?action=addDownload&name=%s&url=%s&image=%s)' % (sysaddon, urllib.quote_plus(name), urllib.quote_plus(i['url']), urllib.quote_plus(poster))))
                #    except:
                #        pass
                if mode == 'movies':
                    cm.append((control.lang(30711).encode('utf-8'), 'RunPlugin(%s?action=addView&content=movies)' % sysaddon))
                elif mode == 'tvshows':
                    cm.append((control.lang(30712).encode('utf-8'), 'RunPlugin(%s?action=addView&content=tvshows)' % sysaddon))
                elif mode == 'seasons':
                    cm.append((control.lang(30713).encode('utf-8'), 'RunPlugin(%s?action=addView&content=seasons)' % sysaddon))
                elif mode == 'episodes':
                    cm.append((control.lang(30714).encode('utf-8'), 'RunPlugin(%s?action=addView&content=episodes)' % sysaddon))
                item = control.item(label=name, iconImage=poster, thumbnailImage=poster)
                try:
                    item.setArt({'poster': poster, 'tvshow.poster': poster, 'season.poster': poster, 'banner': banner, 'tvshow.banner': banner, 'season.banner': banner})
                except:
                    pass
                if not fanart == '0' and control.setting('fanart') == 'true':
                    item.setProperty('Fanart_Image', fanart)
                elif not fanart == '0' and control.setting('fanart') == 'false':
                    item.setProperty('Fanart_Image', fanart2)
                elif addonFanart is not None:
                    item.setProperty('Fanart_Image', addonFanart)
                if queue is False:
                    item.setInfo(type='Video', infoLabels=control.metadataClean(meta))
                    # item.setInfo(type='Video', infoLabels = meta) # old code
                    item.addContextMenuItems(cm)
                    control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=folder)
                else:
                    item.setInfo(type='Video', infoLabels = control.metadataClean(meta))
                    # item.setInfo(type='Video', infoLabels = meta) # old code
                    playlist.add(url=url, listitem=item)
            except:
                pass
        if queue is not False:
            return control.player.play(playlist)
        try:
            i = items[0]
            if i['next'] == '':
                raise Exception()
            url = '%s?action=%s&url=%s' % (sysaddon, i['nextaction'], urllib.quote_plus(i['next']))
            item = control.item(label=control.lang(30500).encode('utf-8'))
            item.setArt({'addonPoster': addonPoster, 'thumb': addonPoster, 'poster': addonPoster, 'tvshow.poster': addonPoster, 'season.poster': addonPoster, 'banner': addonPoster, 'tvshow.banner': addonPoster, 'season.banner': addonPoster})
            item.setProperty('addonFanart_Image', addonFanart)
            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=True)
        except:
            pass
        if mode is not None:
            control.content(int(sys.argv[1]), mode)
        control.directory(int(sys.argv[1]), cacheToDisc=True)
        if mode in ['movies', 'tvshows', 'seasons', 'episodes']:
            views.setView(mode, {'skin.estuary': 55})


class resolver:
    def browser(self, url):
        try:
            url = self.get(url)
            if url is False:
                return
            control.execute('RunPlugin(plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no)' % urllib.quote_plus(url))
        except:
            pass

    def link(self, url):
        try:
            url = self.get(url)
            if url is False:
                return
            control.execute('ActivateWindow(busydialog)')
            url = self.process(url)
            control.execute('Dialog.Close(busydialog)')
            if url is None:
                return control.infoDialog(control.lang(30705).encode('utf-8'))
            return url
        except:
            pass

    def get(self, url):
        try:
            items = re.compile('<sublink(?:\s+name=|)(?:\'|\"|)(.*?)(?:\'|\"|)>(.+?)</sublink>').findall(url)
            if len(items) == 0:
                return url
            if len(items) == 1:
                return items[0][1]
            items = [('Link %s' % (int(items.index(i))+1) if i[0] == '' else i[0], i[1]) for i in items]
            select = control.selectDialog([i[0] for i in items], control.infoLabel('listitem.label'))
            if select == -1:
                return False
            else:
                return items[select][1]
        except:
            pass

    def f4m(self, url, name):
            try:
                if not any(i in url for i in ['.f4m', '.ts']):
                    raise Exception()
                ext = url.split('?')[0].split('&')[0].split('|')[0].rsplit('.')[-1].replace('/', '').lower()
                if ext not in ['f4m', 'ts']:
                    raise Exception()
                params = urlparse.parse_qs(url)
                try:
                    proxy = params['proxy'][0]
                except:
                    proxy = None
                try:
                    proxy_use_chunks = json.loads(params['proxy_for_chunks'][0])
                except:
                    proxy_use_chunks = True
                try:
                    maxbitrate = int(params['maxbitrate'][0])
                except:
                    maxbitrate = 0
                try:
                    simpleDownloader = json.loads(params['simpledownloader'][0])
                except:
                    simpleDownloader = False
                try:
                    auth_string = params['auth'][0]
                except:
                    auth_string = ''
                try:
                    streamtype = params['streamtype'][0]
                except:
                    streamtype = 'TSDOWNLOADER' if ext == 'ts' else 'HDS'
                try:
                    swf = params['swf'][0]
                except:
                    swf = None
                from F4mProxy import f4mProxyHelper
                return f4mProxyHelper().playF4mLink(url, name, proxy, proxy_use_chunks, maxbitrate, simpleDownloader, auth_string, streamtype, False, swf)
            except:
                pass

    def process(self, url, direct=True):
        try:
            if not any(i in url for i in ['.jpg', '.png', '.gif']):
                raise Exception()
            ext = url.split('?')[0].split('&')[0].split('|')[0].rsplit('.')[-1].replace('/', '').lower()
            if ext not in ['jpg', 'png', 'gif']:
                raise Exception()
            try:
                i = os.path.join(control.dataPath, 'img')
                control.deleteFile(i)
                f = control.openFile(i, 'w')
                f.write(client.getHTML(url))
                f.close()
                control.execute('ShowPicture("%s")' % i)
                return False
            except:
                return
        except:
            pass
        try:
            r, x = re.findall('(.+?)\|regex=(.+?)$', url)[0]
            x = regex.fetch(x)
            r += urllib.unquote_plus(x)
            if not '</regex>' in r:
                raise Exception()
            u = regex.resolve(r)
            if u is not None:
                url = u
        except:
            pass
        try:
            if not url.startswith('rtmp'):
                raise Exception()
            if len(re.compile('\s*timeout=(\d*)').findall(url)) == 0:
                url += ' timeout=10'
            return url
        except:
            pass
        try:
            if not any(i in url for i in ['.m3u8', '.f4m', '.ts']):
                raise Exception()
            ext = url.split('?')[0].split('&')[0].split('|')[0].rsplit('.')[-1].replace('/', '').lower()
            if ext not in ['m3u8', 'f4m', 'ts']:
                raise Exception()
            return url
        except:
            pass
        try:
            preset = re.findall('<preset>(.+?)</preset>', url)[0]
            if 'search' not in preset:
                raise Exception()
            title, year, imdb = re.findall('<title>(.+?)</title>', url)[0], re.findall('<year>(.+?)</year>', url)[0], re.findall('<imdb>(.+?)</imdb>', url)[0]
            try:
                tvdb, tvshowtitle, premiered, season, episode = re.findall('<tvdb>(.+?)</tvdb>', url)[0], re.findall('<tvshowtitle>(.+?)</tvshowtitle>', url)[0], re.findall('<premiered>(.+?)</premiered>', url)[0], re.findall('<season>(.+?)</season>', url)[0], re.findall('<episode>(.+?)</episode>', url)[0]
            except:
                tvdb = tvshowtitle = premiered = season = episode = None
            direct = False
            quality = 'HD' if not preset == 'searchsd' else 'SD'
            from resources.lib.modules import sources
            u = sources.sources().getSources(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, quality)
            if u is not None:
                return u
        except:
            pass
        try:
            from resources.lib.modules import sources
            u = sources.sources().getURISource(url)
            if u is not False:
                direct = False
            if u is None or u is False:
                raise Exception()
            return u
        except:
            pass
        try:
            if '.google.com' not in url:
                raise Exception()
            from resources.lib.modules import directstream
            u = directstream.google(url)[0]['url']
            return u
        except:
            pass
        try:
            if 'filmon.com/' not in url:
                raise Exception()
            from resources.lib.modules import filmon
            u = filmon.resolve(url)
            return u
        except:
            pass
        try:
            try:
                headers = dict(urlparse.parse_qsl(url.rsplit('|', 1)[1]))
            except:
                headers = dict('')
            if not url.startswith('http'):
                raise Exception()
            result = client.request(url.split('|')[0], headers=headers, output='headers', timeout='20')
            if 'Content-Type' in result and 'html' not in result['Content-Type']:
                raise Exception()
            import liveresolver
            if liveresolver.isValid(url) is True:
                direct = False
            u = liveresolver.resolve(url)
            if u is not None:
                try:
                    dialog.close()
                except:
                    pass
                return u
        except:
            pass
        try:
            import resolveurl
            hmf = resolveurl.HostedMediaFile(url=url)
            if hmf.valid_url() is False:
                raise Exception()
            direct = False
            u = hmf.resolve()
            if u is not False:
                return u
        except:
            pass
        if direct is True:
            return url


class player(xbmc.Player):
    def __init__(self):
        xbmc.Player.__init__(self)

    def play(self, url, content=None):
        try:
            try:
                if url.startswith('http'):
                    url = resolver().get(url)
                else:
                    url = url.decode('base64')
            except:
                pass
            if url.endswith('?a=view'):
                url = url.split('?a=view')[0]
            if url is False:
                return
            control.execute('ActivateWindow(busydialog)')
            url = resolver().process(url)
            control.execute('Dialog.Close(busydialog)')
            if url is None:
                return control.infoDialog(control.lang(30705).encode('utf-8'))
            if url is False:
                return
            meta = {}
            for i in ['title', 'originaltitle', 'tvshowtitle', 'year', 'season', 'episode', 'genre', 'rating', 'votes', 'director', 'writer', 'plot', 'tagline']:
                try:
                    meta[i] = control.infoLabel('listitem.%s' % i)
                except:
                    pass
            meta = dict((k, v) for k, v in meta.iteritems() if not v == '')
            if 'title' not in meta:
                meta['title'] = control.infoLabel('listitem.label')
            icon = control.infoLabel('listitem.icon')
            self.name = meta['title']
            self.year = meta['year'] if 'year' in meta else '0'
            self.getbookmark = True if (content == 'movies' or content == 'episodes') else False
            self.offset = bookmarks().get(self.name, self.year)
            f4m = resolver().f4m(url, self.name)
            if f4m is not None:
                return
            item = control.item(path=url, iconImage=icon, thumbnailImage=icon)
            try:
                item.setArt({'icon': icon})
            except:
                pass
            item.setInfo(type='Video', infoLabels=control.metadataClean(meta))
            # item.setInfo(type='Video', infoLabels = meta) # old code
            control.player.play(url, item)
            control.resolve(int(sys.argv[1]), True, item)
            self.totalTime = 0
            self.currentTime = 0
            for i in range(0, 240):
                if self.isPlayingVideo():
                    break
                control.sleep(1000)
            while self.isPlayingVideo():
                try:
                    self.totalTime = self.getTotalTime()
                    self.currentTime = self.getTime()
                except:
                    pass
                control.sleep(2000)
            control.sleep(5000)
        except:
            pass

    def onPlayBackStarted(self):
        control.execute('Dialog.Close(all,true)')
        if self.getbookmark is True and not self.offset == '0':
            self.seekTime(float(self.offset))

    def onPlayBackStopped(self):
        if self.getbookmark is True:
            bookmarks().reset(self.currentTime, self.totalTime, self.name, self.year)

    def onPlayBackEnded(self):
        self.onPlayBackStopped()


class bookmarks:
    def get(self, name, year='0'):
        try:
            offset = '0'
            idFile = hashlib.md5()
            for i in name:
                idFile.update(str(i))
            for i in year:
                idFile.update(str(i))
            idFile = str(idFile.hexdigest())
            dbcon = database.connect(control.bookmarksFile)
            dbcur = dbcon.cursor()
            dbcur.execute("SELECT * FROM bookmark WHERE idFile = '%s'" % idFile)
            match = dbcur.fetchone()
            self.offset = str(match[1])
            dbcon.commit()
            if self.offset == '0':
                raise Exception()
            minutes, seconds = divmod(float(self.offset), 60)
            hours, minutes = divmod(minutes, 60)
            label = '%02d:%02d:%02d' % (hours, minutes, seconds)
            label = (control.lang(32502) % label).encode('utf-8')
            try:
                yes = control.dialog.contextmenu([label, control.lang(32501).encode('utf-8'), ])
            except:
                yes = control.yesnoDialog(label, '', '', str(name), control.lang(32503).encode('utf-8'), control.lang(32501).encode('utf-8'))
            if yes:
                self.offset = '0'
            return self.offset
        except:
            return offset

    def reset(self, currentTime, totalTime, name, year='0'):
        try:
            timeInSeconds = str(currentTime)
            ok = int(currentTime) > 180 and (currentTime / totalTime) <= .92
            idFile = hashlib.md5()
            for i in name:
                idFile.update(str(i))
            for i in year:
                idFile.update(str(i))
            idFile = str(idFile.hexdigest())
            control.makeFile(control.dataPath)
            dbcon = database.connect(control.bookmarksFile)
            dbcur = dbcon.cursor()
            dbcur.execute("CREATE TABLE IF NOT EXISTS bookmark (""idFile TEXT, ""timeInSeconds TEXT, ""UNIQUE(idFile)"");")
            dbcur.execute("DELETE FROM bookmark WHERE idFile = '%s'" % idFile)
            if ok:
                dbcur.execute("INSERT INTO bookmark Values (?, ?)", (idFile, timeInSeconds))
            dbcon.commit()
        except:
            pass
