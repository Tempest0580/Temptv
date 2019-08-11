# -*- coding: utf-8 -*-

import os,re,sys,hashlib,urllib,urlparse,json,base64,random,datetime,xbmc
from resources.lib.modules import cache,client,control,metacache,regex
from resources.lib.modules import views,workers,youtube,trailer
try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database


class indexer:
    def __init__(self):
        self.list = []
        self.hash = []

    def entertainment(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvZW5nbGlzaC5tM3U='.decode(
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

    def music(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvbWFpbk11c2ljLnhtbA=='.decode(
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
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvdGVzdGluZy50eHQ='.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            self.addDirectory(self.list)
            return self.list
        except:
            pass

    def click_movies(self):
        try:
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvbWFpbk1vdmllcy54bWw='.decode(
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
            regex.clear()
            url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RlbXBlc3QwNTgwL3htbC9tYXN0ZXIvYWR1bHQubTN1'.decode(
                'base64')
            self.list = self.noname_list(url)
            for i in self.list:
                i.update({'content': 'addons'})
            if control.setting('Show_Adult') == 'false':
                import xbmcgui
                xbmcgui.Dialog().ok('Adults Only 18+', 'If Your 18 or Older Enable Adult Channels in Settings')
                return
            else:
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
            tvm = client.request('http://api.tvmaze.com/lookup/shows?thetvdb=%s' % tvdb)
            if tvm  is None:
                tvm = client.request('http://api.tvmaze.com/lookup/shows?imdb=%s' % imdb)
            tvm = 'http://api.tvmaze.com/shows/%s/episodes' % str(json.loads(tvm).get('id'))
            items = json.loads(client.request(tvm))
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
                return [x for y,x in enumerate((query + [input])) if x not in (query + [input])[:y]]
            cache.get(search, 0, table='rel_srch')
            links = client.request(link)
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
                    season = re.findall('<season>(.+?)</season>', meta)[0]
                except:
                    season = '0'
                try:
                    episode = re.findall('<episode>(.+?)</episode>', meta)[0]
                except:
                    episode = '0'
                self.list.append({'name': name, 'vip': vip, 'url': url, 'action': action, 'folder': folder, 'poster': image2, 'banner': '0', 'fanart': fanart2, 'content': content, 'imdb': imdb, 'tvdb': tvdb, 'tmdb': '0', 'title': title, 'originaltitle': title, 'tvshowtitle': tvshowtitle, 'year': year, 'premiered': premiered, 'season': season, 'episode': episode})
            except:
                pass            
        regex.insert(self.hash)
        return self.list

    def worker(self):
        if not control.setting('metadata') == 'true':
            return
        self.omdb_key = control.setting('omdb.key')
        self.imdb_info_link = 'http://www.omdbapi.com/?i=%s&plot=full&r=json&apikey=%s' % ("%s", self.omdb_key)
        self.tvmaze_info_link = 'http://api.tvmaze.com/lookup/shows?thetvdb=%s'
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
                self.movie_info(0); self.tv_info(0)
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
            [i.start() for i in threads]
            [i.join() for i in threads]
        if self.meta:
            metacache.insert(self.meta)

    def movie_info(self, i):
        try:
            if self.list[i]['metacache'] is True:
                raise Exception()
            if not self.list[i]['content'] == 'movies':
                raise Exception()
            imdb = self.list[i]['imdb']
            if imdb == '0':
                raise Exception()
            url = self.imdb_info_link % imdb
            item = client.request(url, timeout='10')
            item = json.loads(item)
            if 'Error' in item and 'incorrect imdb' in item['Error'].lower():
                return self.meta.append({'imdb': imdb, 'tmdb': '0', 'tvdb': '0', 'lang': self.lang, 'item': {'code': '0'}})
            title = item['Title']
            title = title.encode('utf-8')
            if not title == '0':
                self.list[i].update({'title': title})
            year = item['Year']
            year = year.encode('utf-8')
            if not year == '0':
                self.list[i].update({'year': year})
            imdb = item['imdbID']
            if imdb is None or imdb == '' or imdb == 'N/A':
                imdb = '0'
            imdb = imdb.encode('utf-8')
            if not imdb == '0':
                self.list[i].update({'imdb': imdb, 'code': imdb})
            premiered = item['Released']
            if premiered is None or premiered == '' or premiered == 'N/A':
                premiered = '0'
            premiered = re. findall('(\d*) (.+?) (\d*)', premiered)
            try:
                premiered = '%s-%s-%s' % (premiered[0][2], {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}[premiered[0][1]], premiered[0][0])
            except:
                premiered = '0'
            premiered = premiered.encode('utf-8')
            if not premiered == '0':
                self.list[i].update({'premiered': premiered})
            genre = item['Genre']
            if genre is None or genre == '' or genre == 'N/A':
                genre = '0'
            genre = genre.replace(', ', ' / ')
            genre = genre.encode('utf-8')
            if not genre == '0':
                self.list[i].update({'genre': genre})
            duration = item['Runtime']
            if duration is None or duration == '' or duration == 'N/A':
                duration = '0'
            duration = re.sub('[^0-9]', '', str(duration))
            try:
                duration = str(int(duration) * 60)
            except:
                pass
            duration = duration.encode('utf-8')
            if not duration == '0':
                self.list[i].update({'duration': duration})
            rating = item['imdbRating']
            if rating is None or rating == '' or rating == 'N/A' or rating == '0.0':
                rating = '0'
            rating = rating.encode('utf-8')
            if not rating == '0':
                self.list[i].update({'rating': rating})
            votes = item['imdbVotes']
            try:
                votes = str(format(int(votes),',d'))
            except:
                pass
            if votes is None or votes == '' or votes == 'N/A':
                votes = '0'
            votes = votes.encode('utf-8')
            if not votes == '0':
                self.list[i].update({'votes': votes})
            mpaa = item['Rated']
            if mpaa is None or mpaa == '' or mpaa == 'N/A':
                mpaa = '0'
            mpaa = mpaa.encode('utf-8')
            if not mpaa == '0':
                self.list[i].update({'mpaa': mpaa})
            director = item['Director']
            if director is None or director == '' or director == 'N/A':
                director = '0'
            director = director.replace(', ', ' / ')
            director = re.sub(r'\(.*?\)', '', director)
            director = ' '.join(director.split())
            director = director.encode('utf-8')
            if not director == '0':
                self.list[i].update({'director': director})
            writer = item['Writer']
            if writer is None or writer == '' or writer == 'N/A':
                writer = '0'
            writer = writer.replace(', ', ' / ')
            writer = re.sub(r'\(.*?\)', '', writer)
            writer = ' '.join(writer.split())
            writer = writer.encode('utf-8')
            if not writer == '0':
                self.list[i].update({'writer': writer})
            cast = item['Actors']
            if cast is None or cast == '' or cast == 'N/A':
                cast = '0'
            cast = [x.strip() for x in cast.split(',') if not x == '']
            try:
                cast = [(x.encode('utf-8'), '') for x in cast]
            except:
                cast = []
            if cast == []:
                cast = '0'
            if not cast == '0':
                self.list[i].update({'cast': cast})
            plot = item['Plot']
            if plot is None or plot == '' or plot == 'N/A':
                plot = '0'
            plot = client.replaceHTMLCodes(plot)
            plot = plot.encode('utf-8')
            if not plot == '0':
                self.list[i].update({'plot': plot})
            self.meta.append({'imdb': imdb, 'tmdb': '0', 'tvdb': '0', 'lang': self.lang, 'item': {'title': title, 'year': year, 'code': imdb, 'imdb': imdb, 'premiered': premiered, 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'writer': writer, 'cast': cast, 'plot': plot}})
        except:
            pass

    def tv_info(self, i):
        self.lang = control.apiLanguage()['tvdb']
        self.tvdb_key = control.setting('tvdb.user')
        self.tvdb_info_link = 'http://thetvdb.com/api/%s/series/%s/%s.xml' % (self.tvdb_key, '%s', self. lang)
        try:
            if self.list[i]['metacache'] is True:
                raise Exception()
            if not self.list[i]['content'] in ['tvshows', 'seasons', 'episodes']:
                raise Exception()
            tvdb = self.list[i]['tvdb']
            if tvdb == '0':
                raise Exception()
            url = self.tvdb_info_link % tvdb
            item = client.request(url, timeout='10')
            if item[1] == '404':
                return self.meta.append({'imdb': '0', 'tmdb': '0', 'tvdb': tvdb, 'lang': self.lang, 'item': {'code': '0'}})
            item = json.loads(item[0])
            tvshowtitle = item['name']
            tvshowtitle = tvshowtitle.encode('utf-8')
            if not tvshowtitle == '0':
                self.list[i].update({'tvshowtitle': tvshowtitle})
            year = item['premiered']
            year = re.findall('(\d{4})', year)[0]
            year = year.encode('utf-8')
            if not year == '0':
                self.list[i].update({'year': year})
            try:
                imdb = item['externals']['imdb']
            except:
                imdb = '0'
            if imdb == '' or imdb is None:
                imdb = '0'
            imdb = imdb.encode('utf-8')
            if self.list[i]['imdb'] == '0' and not imdb == '0':
                self.list[i].update({'imdb': imdb})
            try:
                studio = item['network']['name']
            except:
                studio = '0'
            if studio == '' or studio is None:
                studio = '0'
            studio = studio.encode('utf-8')
            if not studio == '0':
                self.list[i].update({'studio': studio})
            genre = item['genres']
            if genre == '' or genre is None or genre == []:
                genre = '0'
            genre = ' / '.join(genre)
            genre = genre.encode('utf-8')
            if not genre == '0':
                self.list[i].update({'genre': genre})
            try:
                duration = str(item['runtime'])
            except:
                duration = '0'
            if duration == '' or duration is None:
                duration = '0'
            try:
                duration = str(int(duration) * 60)
            except:
                pass
            duration = duration.encode('utf-8')
            if not duration == '0':
                self.list[i].update({'duration': duration})
            rating = str(item['rating']['average'])
            if rating == '' or rating is None:
                rating = '0'
            rating = rating.encode('utf-8')
            if not rating == '0':
                self.list[i].update({'rating': rating})
            plot = item['summary']
            if plot == '' or plot is None:
                plot = '0'
            plot = re.sub('\n|<.+?>|</.+?>|.+?#\d*:', '', plot)
            plot = plot.encode('utf-8')
            if not plot == '0':
                self.list[i].update({'plot': plot})
            self.meta.append({'imdb': imdb, 'tmdb': '0', 'tvdb': tvdb, 'lang': self.lang, 'item': {'tvshowtitle': tvshowtitle, 'year': year, 'code': imdb, 'imdb': imdb, 'tvdb': tvdb, 'studio': studio, 'genre': genre, 'duration': duration, 'rating': rating, 'plot': plot}})
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
                try:
                    name = control.lang(int(i['name'])).encode('utf-8')
                except:
                    name = i['name']
                if name == '':
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
                poster = i['poster'] if 'poster' in i else '0'
                banner = i['banner'] if 'banner' in i else '0'
                fanart = i['fanart'] if 'fanart' in i else '0'
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
                    cm.append((control.lang(30707).encode('utf-8'), 'RunPlugin(%s?action=trailer&name=%s)' % (sysaddon, urllib.quote_plus(name))))
                if content in ['movies', 'tvshows', 'seasons', 'episodes']:
                    cm.append((control.lang(30708).encode('utf-8'), 'XBMC.Action(Info)'))
                if (folder is False and '|regex=' not in str(i.get('url'))) or (folder is True and content in ['tvshows', 'seasons']):
                    cm.append((control.lang(32065).encode('utf-8'), 'RunPlugin(%s?action=queueItem)' % sysaddon))
                if content == 'movies':
                    try:
                        dfile = '%s (%s)' % (i['title'], i['year'])
                    except:
                        dfile = name
                    try:
                        cm.append((control.lang(30722).encode('utf-8'), 'RunPlugin(%s?action=addDownload&name=%s&url=%s&image=%s)' % (sysaddon, urllib.quote_plus(dfile), urllib.quote_plus(i['url']), urllib.quote_plus(poster))))
                    except:
                        pass
                elif content == 'episodes':
                    try:
                        dfile = '%s S%02dE%02d' % (i['tvshowtitle'], int(i['season']), int(i['episode']))
                    except:
                        dfile = name
                    try:
                        cm.append((control.lang(30722).encode('utf-8'), 'RunPlugin(%s?action=addDownload&name=%s&url=%s&image=%s)' % (sysaddon, urllib.quote_plus(dfile), urllib.quote_plus(i['url']), urllib.quote_plus(poster))))
                    except:
                        pass
                elif content == 'songs':
                    try:
                        cm.append((control.lang(30722).encode('utf-8'), 'RunPlugin(%s?action=addDownload&name=%s&url=%s&image=%s)' % (sysaddon, urllib.quote_plus(name), urllib.quote_plus(i['url']), urllib.quote_plus(poster))))
                    except:
                        pass
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
                if not fanart == '0':
                    item.setProperty('Fanart_Image', fanart)
                elif addonFanart is not None:
                    item.setProperty('Fanart_Image', addonFanart)
                if queue is False:
                    item.setInfo(type='Video', infoLabels = control.metadataClean(meta))
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
                i = os.path.join(control.dataPath,'img')
                control.deleteFile(i)
                f = control.openFile(i, 'w')
                f.write(client.request(url))
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
            base = url
            url = resolver().get(url)
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
