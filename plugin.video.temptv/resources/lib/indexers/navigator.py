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
        self.addDirectoryItem('24/7', 'acronaitv_menu', 'channels.png', 'DefaultTvshows.png')
        self.addDirectoryItem('1 Click Movies', 'click_movies', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('1 Click Shows', '1_click_shows', 'channels.png', 'DefaultTVShows.png')
        # self.addDirectoryItem('In Theaters', 'theaters', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('AcronaiTV', 'arconai_cable', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Pluto TV', 'pluto', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('UsaTv Go', 'ustvgoNavigator', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Foreign Channels', 'foreign', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[COLOR black]Adult\'s Only[/COLOR]', 'navXXX', 'highly-rated.png', 'DefaultTVShows.png')
        if control.setting('Dev') == 'true':
            self.addDirectoryItem('Testing', 'testing', 'channels.png', 'DefaultTVShows.png')
        # self.addDirectoryItem('Refresh', 'refresh', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('ChangeLog', 'changelog', 'search.png', 'DefaultAddonProgram.png')
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
        # self.addDirectoryItem(32046, 'openSettings&query=1.0', 'settings.png', 'DefaultAddonProgram.png')
        # self.addDirectoryItem(32047, 'openSettings&query=2.0', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32051, 'clearMetaCache', 'settings.png', 'DefaultAddonProgram.png')

        self.endDirectory()

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
