# -*- coding: utf-8 -*-

import urlparse, sys, urllib
import xbmc, xbmcaddon, xbmcgui

dialog = xbmcgui.Dialog()
params = dict(urlparse.parse_qsl(sys.argv[2].replace('?', '')))
mode = params.get('mode')
action = params.get('action')
name = params.get('name')
title = params.get('title')
year = params.get('year')
imdb = params.get('imdb')
tvdb = params.get('tvdb')
tmdb = params.get('tmdb')
season = params.get('season')
episode = params.get('episode')
tvshowtitle = params.get('tvshowtitle')
premiered = params.get('premiered')
url = params.get('url')
image = params.get('image')
meta = params.get('meta')
select = params.get('select')
query = params.get('query')
source = params.get('source')
content = params.get('content')
folder = params.get('folder')
poster = params.get('poster')
windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0", "1") else 0

arconai_cable = params.get('arconai_cable')
arconai_shows = params.get('arconai_shows')
arconai_movies = params.get('arconai_movies')
arconai_play = params.get('arconai_play')
selection = params.get('selection')


if action is None:
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache
    cache.cache_version_check()
    navigator.navigator().root()

if action == 'entertainment':
    from resources.lib.indexers import lists
    lists.indexer().entertainment()

if action == 'movies':
    from resources.lib.indexers import lists
    lists.indexer().movies()

if action == 'kids':
    from resources.lib.indexers import lists
    lists.indexer().kids()

if action == 'sports':
    from resources.lib.indexers import lists
    lists.indexer().sports()

if action == 'news':
    from resources.lib.indexers import lists
    lists.indexer().news()

if action == 'music':
    from resources.lib.indexers import lists
    lists.indexer().music()

if action == 'hour24':
    from resources.lib.indexers import lists
    lists.indexer().hour24()

if action == 'testing':
    from resources.lib.indexers import lists
    lists.indexer().testing()

if action == 'jewMC':
    from resources.lib.indexers import lists
    lists.indexer().rootMC()

if action == 'click_movies':
    from resources.lib.indexers import lists
    lists.indexer().click_movies()

if action == '1_click_shows':
    from resources.lib.indexers import lists
    lists.indexer().shows()

if action == 'foreign':
    from resources.lib.indexers import lists
    lists.indexer().foreign()

if action == 'pluto':
    from resources.lib.indexers import lists
    lists.indexer().pluto()

if action == 'theaters':
    from resources.lib.indexers import lists
    lists.indexer().theaters()

if action == 'iptvChannels':
    from resources.lib.indexers import lists
    lists.indexer().root()

if action == 'navXXX':
    from resources.lib.indexers import lists
    lists.indexer().rootXXX()

elif action == 'directory':
    from resources.lib.indexers import lists
    lists.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists
    lists.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists
    lists.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists
    lists.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists
    lists.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists
    lists.indexer().youtube(url, action)

elif action == 'browser':
    from resources.lib.indexers import lists
    lists.resolver().browser(url)

elif action == 'lists_play':
    from resources.lib.indexers import lists
    lists.player().play(url, content)

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().settings()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheSearch()

elif action == 'clearMetaCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheMeta()

elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()

elif action == 'changelog':
    from resources.lib.indexers import navigator
    navigator.navigator().changelog()

elif action == 'play':
    from resources.lib.modules import sources
    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)

elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)

elif action == 'moviesToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libmovies().silent(url)

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)

elif action == 'tvshowsToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libtvshows().silent(url)

elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)

elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()

elif action == 'ustvgoNavigator':
    from resources.lib.indexers import ustvgo
    ustvgo.ustvgo().root()

elif action == 'ustvgoPlay':
    from resources.lib.indexers import ustvgo
    ustvgo.ustvgo().play(url)

elif action == 'acronaitv_menu':
    from resources.lib.indexers import acronaitv
    acronaitv.acronaitv().list_categories()

elif action == 'arconai_cable':
    from resources.lib.indexers import acronaitv
    acronaitv.acronaitv().list_cable()

elif action == 'arconai_shows':
    from resources.lib.indexers import acronaitv
    acronaitv.acronaitv().list_shows()

elif action == 'arconai_movies':
    from resources.lib.indexers import acronaitv
    acronaitv.acronaitv().list_movies()

elif action == 'arconai_play':
    from resources.lib.indexers import acronaitv
    acronaitv.acronaitv().play_video(params['selection'])
