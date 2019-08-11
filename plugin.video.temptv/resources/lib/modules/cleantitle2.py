# -*- coding: UTF-8 -*-

import re, unicodedata


def get(title):
    if title is None:
        return
    try:
        title = title.encode('utf-8')
    except:
        pass
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&')
    title = re.sub('\n|([[].+?[]])|([(].+?[)])|\s(vs|v[.])\s|(:|;|-|–|"|,|\'|\_|\.|\?)|\s', '', title).lower()
    return title


def geturl(title):
    if title is None:
        return
    title = title.lower()
    title = title.translate(None, ':*?"\'\.<>|&!,')
    title = title.replace('/', '-')
    title = title.replace(' ', '-')
    title = title.replace('--', '-')
    return title


def get_simple(title):
    if title is None:
        return
    title = title.lower()
    title = re.sub('(\d{4})', '', title)
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&')
    title = re.sub('\n|\(|\)|\[|\]|\{|\}|\s(vs|v[.])\s|(:|;|-|–|"|,|\'|\_|\.|\?)|\s', '', title).lower()
    title = re.sub(r'<.*?>', '', title, count=0)
    return title


def getsearch(title):
    if title is None:
        return
    title = title.lower()
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&')
    title = re.sub('\\\|/|-|–|:|;|\*|\?|"|\'|<|>|\|', '', title).lower()
    return title


def query(title):
    if title is None:
        return
    title = title.replace('\'', '').rsplit(':', 1)[0].rsplit(' -', 1)[0].replace('-', ' ')
    return title


def get_query(title):
    if title is None:
        return
    title = title.replace(' ', '.').replace(':', '').replace('.-.', '.').replace('\'', '')
    return title


def normalize(title):
    try:
        try:
            return title.decode('ascii').encode("utf-8")
        except:
            pass
        return str(''.join(c for c in unicodedata.normalize(
            'NFKD', unicode(title.decode('utf-8'))) if unicodedata.category(c) != 'Mn'))
    except:
        return title


def clean_search_query(url):
    url = url.replace('-', '+')
    url = url.replace(' ', '+')
    return url

