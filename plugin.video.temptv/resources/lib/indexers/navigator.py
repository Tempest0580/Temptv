# -*- coding: utf-8 -*-


import os, sys
import xbmc, xbmcaddon, xbmcgui
from resources.lib.modules import control
from resources.lib.modules import trakt

sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])

artPath = control.artPath()
addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True
traktCredentials = trakt.getTraktCredentialsInfo()
traktIndicators = trakt.getTraktIndicatorsInfo()
queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
    HOMEPATH = xbmc.translatePath('special://home/')
    ADDONSPATH = os.path.join(HOMEPATH, 'addons')
    THISADDONPATH = os.path.join(ADDONSPATH, ADDON_ID)
    LOCALNEWS = os.path.join(THISADDONPATH, 'changelog.txt')

    def root(self):
        self.addDirectoryItem('Entertainment', 'entertainment', 'channels.png', 'DefaultTvshows.png')
        self.addDirectoryItem('Movies', 'movies', 'channels.png', 'DefaultTvshows.png')
        self.addDirectoryItem('Kids', 'kids', 'channels.png', 'DefaultTvshows.png')
        self.addDirectoryItem('Sports', 'sports', 'channels.png', 'DefaultTvshows.png')
        self.addDirectoryItem('News', 'news', 'channels.png', 'DefaultTvshows.png')
        self.addDirectoryItem('Music', 'music', 'channels.png', 'DefaultTvshows.png')
        self.addDirectoryItem('24/7', 'hour24', 'channels.png', 'DefaultTvshows.png')
        self.addDirectoryItem('1 Click Movies', '1_click_movies', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('1 Click Shows', '1_click_shows', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('In Theaters', 'theaters', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Pluto TV', 'pluto', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Foreign Channels', 'foreign', 'channels.png', 'DefaultTVShows.png')
        # self.addDirectoryItem('iptvChannels', 'iptvChannels', 'channels.png', 'DefaultTVShows.png')
        # self.addDirectoryItem('jewMC', 'jewMC', 'highly-rated.png', 'DefaultVideoPlaylists.png')
        self.addDirectoryItem('[COLOR black]Adult\'s Only[/COLOR]', 'navXXX', 'highly-rated.png', 'DefaultTVShows.png')
        if control.setting('Dev') == 'true':
            self.addDirectoryItem('Testing', 'testing', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Refresh', 'refresh', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'settings.png', 'DefaultAddonProgram.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads is True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')
        self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultFolder.png')
        self.addDirectoryItem('ChangeLog', 'changelog', 'search.png', 'DefaultAddonProgram.png')
        self.endDirectory()

    def shows(self):
        self.addDirectoryItem('Arrow', 'arrow', 'shows/arrow.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem('Ballers', 'ballers', 'shows/ballers.jpg', 'DefaultTVShows.png')
        self.endDirectory()

    def movies(self):
        self.addDirectoryItem('4K', 'four', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('1080p', 'ten', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('720p', 'seven', 'channels.png', 'DefaultTVShows.png')
        self.endDirectory()

    def changelog(self):
            r = open(self.LOCALNEWS)
            compfile = r.read()
            self.showText('Changelog', compfile)

    def showText(self, heading, text):
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

    def settings(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32044, 'openSettings&query=1.0', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=2.0', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=3.0', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32556, 'libraryNavigator', 'settingss.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32048, 'openSettings&query=8.0', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=9.0', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32051, 'clearMetaCache', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32604, 'clearCacheSearch', 'settings.png', 'DefaultAddonProgram.png')

        self.endDirectory()

    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=7.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)
        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png')
        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        self.endDirectory()

    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')

        self.endDirectory()

    def views(self):
        try:
            control.idle()

            items = [(control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes')]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1:
                return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels={'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import views
            views.setView(content, {})
        except:
            return

    def accountCheck(self):
        if traktCredentials is False and imdbCredentials is False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()

    def infoCheck(self, version):
        try:
            control.infoDialog('', control.lang(32074).encode('utf-8'), time=5000, sound=False)
            return '1'
        except:
            return '1'

    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheMeta(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        from resources.lib.modules import cache
        cache.cache_clear_meta()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheProviders(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        from resources.lib.modules import cache
        cache.cache_clear_providers()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheSearch(self):
        control.idle()
        if control.yesnoDialog(control.lang(32056).encode('utf-8'), '', ''):
            control.setSetting('tvsearch', '')
            control.setSetting('moviesearch', '')
            control.refresh()
            control.idle()

    def clearCacheAll(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes:
            return
        from resources.lib.modules import cache
        cache.cache_clear_all()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
        try:
            name = control.lang(name).encode('utf-8')
        except:
            pass
        url = '%s?action=%s' % (sysaddon, query) if isAction is True else query
        thumb = os.path.join(artPath, thumb) if artPath is not None else icon
        cm = []
        if queue is True:
            cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        if context is not None:
            cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if addonFanart is not None:
            item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)

    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)
