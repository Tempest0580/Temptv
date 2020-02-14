# -*- coding: UTF-8 -*-

import re, urllib, urllib2
import cookielib, gzip
import StringIO
import socket

socket.setdefaulttimeout(10)


class Net:
    _cj = cookielib.LWPCookieJar()
    _proxy = None
    _user_agent = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
    _http_debug = False

    def __init__(self, cookie_file='', proxy='', user_agent='', ssl_verify=True, http_debug=False):
        if cookie_file:
            self.set_cookies(cookie_file)
        if proxy:
            self.set_proxy(proxy)
        if user_agent:
            self.set_user_agent(user_agent)
        self._ssl_verify = ssl_verify
        self._http_debug = http_debug
        self._update_opener()

    def set_cookies(self, cookie_file):
        try:
            self._cj.load(cookie_file, ignore_discard=True)
            self._update_opener()
            return True
        except:
            return False

    def get_cookies(self, as_dict=False):
        if as_dict:
            return dict((cookie.name, cookie.value) for cookie in self._cj)
        else:
            return self._cj._cookies

    def save_cookies(self, cookie_file):
        self._cj.save(cookie_file, ignore_discard=True)

    def set_proxy(self, proxy):
        self._proxy = proxy
        self._update_opener()

    def get_proxy(self):
        return self._proxy

    def set_user_agent(self, user_agent):
        self._user_agent = user_agent

    def get_user_agent(self):
        return self._user_agent

    def _update_opener(self):
        handlers = [urllib2.HTTPCookieProcessor(self._cj), urllib2.HTTPBasicAuthHandler()]
        if self._http_debug:
            handlers += [urllib2.HTTPHandler(debuglevel=1)]
        else:
            handlers += [urllib2.HTTPHandler()]
        if self._proxy:
            handlers += [urllib2.ProxyHandler({'http': self._proxy})]
        try:
            import platform
            node = platform.node().lower()
        except:
            node = ''
        if not self._ssl_verify or node == 'xboxone':
            try:
                import ssl
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                if self._http_debug:
                    handlers += [urllib2.HTTPSHandler(context=ctx, debuglevel=1)]
                else:
                    handlers += [urllib2.HTTPSHandler(context=ctx)]
            except:
                pass
        opener = urllib2.build_opener(*handlers)
        urllib2.install_opener(opener)

    def http_GET(self, url, headers={}, compression=True):
        return self._fetch(url, headers=headers, compression=compression)

    def http_POST(self, url, form_data, headers={}, compression=True):
        return self._fetch(url, form_data, headers=headers, compression=compression)

    def http_HEAD(self, url, headers={}):
        request = urllib2.Request(url)
        request.get_method = lambda: 'HEAD'
        request.add_header('User-Agent', self._user_agent)
        for key in headers:
            request.add_header(key, headers[key])
        response = urllib2.urlopen(request)
        return HttpResponse(response)

    def http_DELETE(self, url, headers={}):
        request = urllib2.Request(url)
        request.get_method = lambda: 'DELETE'
        request.add_header('User-Agent', self._user_agent)
        for key in headers:
            request.add_header(key, headers[key])
        response = urllib2.urlopen(request)
        return HttpResponse(response)

    def _fetch(self, url, form_data={}, headers={}, compression=True):
        req = urllib2.Request(url)
        if form_data:
            if isinstance(form_data, basestring):
                form_data = form_data
            else:
                form_data = urllib.urlencode(form_data, True)
            req = urllib2.Request(url, form_data)
        req.add_header('User-Agent', self._user_agent)
        for key in headers:
            req.add_header(key, headers[key])
        if compression:
            req.add_header('Accept-Encoding', 'gzip')
        req.add_unredirected_header('Host', req.get_host())
        response = urllib2.urlopen(req)
        return HttpResponse(response)


class HttpResponse:
    content = ''

    def __init__(self, response):
        self._response = response


    @property
    def content(self):
        html = self._response.read()
        encoding = None
        try:
            if self._response.headers['content-encoding'].lower() == 'gzip':
                html = gzip.GzipFile(fileobj=StringIO.StringIO(html)).read()
        except:
            pass
        try:
            content_type = self._response.headers['content-type']
            if 'charset=' in content_type:
                encoding = content_type.split('charset=')[-1]
        except:
            pass
        r = re.search('<meta\s+http-equiv="Content-Type"\s+content="(?:.+?);\s+charset=(.+?)"', html, re.IGNORECASE)
        if r:
            encoding = r.group(1)
        if encoding is not None:
            try:
                html = html.decode(encoding)
            except:
                pass
        return html

    def get_headers(self, as_dict=False):
        if as_dict:
            return dict([(item[0].title(), item[1]) for item in self._response.info().items()])
        else:
            return self._response.info().headers

    def get_url(self):
        return self._response.geturl()


