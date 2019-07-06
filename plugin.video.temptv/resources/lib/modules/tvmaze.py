# -*- coding: utf-8 -*-


import urllib, json

from resources.lib.modules import cache
from resources.lib.modules import client


class tvMaze:
    def __init__(self, show_id=None):
        self.api_url = 'http://api.tvmaze.com/%s%s'
        self.show_id = show_id

    def showID(self, show_id=None):
        if show_id is not None:
            self.show_id = show_id
            return show_id

        return self.show_id

    def request(self, endpoint, query=None):
        try:
            # Encode the queries, if there is any...
            if query is not None:
                query = '?' + urllib.urlencode(query)
            else:
                query = ''

            # Make the request
            request = self.api_url % (endpoint, query)

            # Send the request and get the response
            # Get the results from cache if available
            response = cache.get(client.request, 24, request)

            # Retrun the result as a dictionary
            return json.loads(response)
        except:
            pass

        return {}

    def showLookup(self, type, id):
        try:
            result = self.request('lookup/shows', {type: id})

            # Storing the show id locally
            if 'id' in result:
                self.show_id = result['id']

            return result
        except:
            pass

        return {}

    def shows(self, show_id=None, embed=None):
        try:
            if not self.showID(show_id):
                raise Exception()

            result = self.request('shows/%d' % self.show_id)

            # Storing the show id locally
            if 'id' in result:
                self.show_id = result['id']

            return result
        except:
            pass

        return {}

    def showSeasons(self, show_id=None):
        try:
            if not self.showID(show_id):
                raise Exception()

            result = self.request('shows/%d/seasons' % int(self.show_id))

            if len(result) > 0 and 'id' in result[0]:
                return result
        except:
            pass

        return []

    def showSeasonList(self, show_id):
        return {}

    def showEpisodeList(self, show_id=None, specials=False):
        try:
            if not self.showID(show_id):
                raise Exception()

            result = self.request('shows/%d/episodes' % int(self.show_id), 'specials=1' if specials else '')

            if len(result) > 0 and 'id' in result[0]:
                return result
        except:
            pass

        return []

    def episodeAbsoluteNumber(self, thetvdb, season, episode):
        try:
            url = 'http://thetvdb.com/api/%s/series/%s/default/%01d/%01d' % ('7A9F0F57B6E8132D', thetvdb, int(season), int(episode))
            return int(client.parseDOM(client.request(url), 'absolute_number')[0])
        except:
            pass

        return episode

    def getTVShowTranslation(self, thetvdb, lang):
        try:
            url = 'http://thetvdb.com/api/%s/series/%s/%s.xml' % ('7A9F0F57B6E8132D', thetvdb, lang)
            r = client.request(url)
            title = client.parseDOM(r, 'SeriesName')[0]
            title = client.replaceHTMLCodes(title)
            title = title.encode('utf-8')

            return title
        except:
            pass
