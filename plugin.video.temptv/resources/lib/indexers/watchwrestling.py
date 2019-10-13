# -*- coding: utf-8 -*-
# --[ WatchWrestling v1.0 ]--|--[ From JewBMX ]--
# Wrestling/Fighting Indexer made with 4 sites as of now.
# Live items/channels probably still need work.

import re, os, sys, urllib, urlparse
import xbmc, xbmcgui, xbmcplugin
from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import workers
import HTMLParser
import resolveurl

sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])
artPath = control.artPath()
addonFanart = control.addonFanart()
addonThumb = control.addonThumb()


class WatchWrestling:
    def __init__(self):
        self.list = []
        self.items = []
        self.cgi_bin_link = 'http://educadegree.com/cgi-bin/'
        self.base1_link = 'http://watchwrestling.la'
        self.art1_link = 'http://watchwrestling.la/wp-content/uploads/2019/02/wwunologo2.png'
        self.base2_link = 'http://watchwrestling.cz'
        self.art2_link = 'http://watchwrestling.cz/wp-content/uploads/2016/03/wwunologo2.png'
        self.base3_link = 'http://watchwrestling24.net'
        self.art3_link = 'http://watchwrestling24.net/wp-content/uploads/2016/11/logo.png'
        self.base4_link = 'http://www.allwrestling.live'
        self.art4_link = 'http://www.allwrestling.live/wp-content/uploads/2018/01/Allwrestling-logo-3.png'

    def root(self):
        self.addDirectoryItem('WatchWrestling.la', 'wrestlingMenuLA', self.art1_link, 'DefaultTVShows.png')
        self.addDirectoryItem('WatchWrestling.cz', 'wrestlingMenuCZ', self.art2_link, 'DefaultTVShows.png')
        self.addDirectoryItem('WatchWrestling24.net', 'wrestlingMenu24', self.art3_link, 'DefaultTVShows.png')
        self.addDirectoryItem('AllWrestling.live', 'wrestlingMenuAWL', self.art4_link, 'DefaultTVShows.png')
        self.endDirectory()

    def rootLA(self):
        channels = [
            ('Boxing', '/category/boxing/'),
            ('Latest AEW Shows', '/category/aew-shows/'),
            ('Latest iMPACT Wrestling', '/category/impact-wrestling/'),
            ('Latest Indy Shows', '/category/indy/'),
            ('Latest NXT', '/category/latest-wwe-shows/nxt/'),
            ('Latest RAW', '/category/latest-wwe-shows/raw/'),
            ('Latest Smackdown', '/category/latest-wwe-shows/smackdown/'),
            ('Latest Total Divas', '/category/latest-wwe-shows/total-divas/'),
            ('Latest UFC Shows', '/category/ufc/'),
            ('Latest Wrestling Archives', '/category/wrestling-archives/'),
            ('Latest WWE Network Shows', '/category/wwe-network/'),
            ('Latest WWE PPVs', '/category/latest-wwe-shows/wwe-ppvs/'),
            ('Latest WWE Shows', '/category/latest-wwe-shows/'),
            ('Latest WWE ShowsALT', '/category/wwe/'),
            ('Lucha Underground', '/category/lucha-underground/'),
            ('Main Event', '/category/main-event/'),
            ('NJPW Wrestling Shows', '/category/njpw-wrestling-shows/'),
            ('NXT', '/category/wwe/nxt/'),
            ('RAW', '/category/wwe/raw/'),
            ('ROH', '/category/roh/'),
            ('Smackdown', '/category/wwe/smackdown/'),
            ('Uncategorized', '/category/uncategorized/'),
            ('WWE Main Event', '/category/wwe/main-event/'),
            ('WWE PPVs', '/category/wwe/wwe-ppvs/')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base1_link + channel[1], 'image': self.art1_link, 'action': 'wrestlingScrape'})
        self.addDirectory(self.list)
        return self.list

    def rootCZ(self):
        channels = [
            ('AEW Shows', '/category/aew-shows/'),
            ('Attitude Era', '/category/attitude-era/'),
            ('Boxing', '/category/boxing/'),
            ('Latest Indy Shows', '/category/indy/'),
            ('Latest NJPW Shows', '/category/njpw/'),
            ('Latest NXT', '/category/latest-wwe-shows/nxt/'),
            ('Latest RAW', '/category/latest-wwe-shows/raw/'),
            ('Latest Smackdown', '/category/latest-wwe-shows/smackdown/'),
            ('Latest TNA Shows', '/category/tna/'),
            ('Latest UFC Shows', '/category/ufc/'),
            ('Latest Wrestling Archives', '/category/wrestling-archives/'),
            ('Latest WWE Network Shows', '/category/wwe-network/'),
            ('Latest WWE PPVs', '/category/latest-wwe-shows/wwe-ppvs/'),
            ('Latest WWE Shows', '/category/wwe/'),
            ('Lucha Underground', '/category/lucha/'),
            ('Main Event', '/category/main-event/'),
            ('NXT', '/category/wwe/nxt/'),
            ('RAW', '/category/wwe/raw/'),
            ('ROH', '/category/roh/'),
            ('Smackdown', '/category/wwe/smackdown/'),
            ('Total Divas', '/category/wwe-total-divas/'),
            ('Uncategorized', '/category/uncategorized/'),
            ('Watch WWE Network 24/7 Live Free', '/watch-wwe-network-247-live-free/'),
            ('WrestleMania', '/category/wrestlemania/'),
            ('WWE Main Event', '/category/wwe/main-event/'),
            ('WWE PPVs', '/category/wwe/wwe-ppvs/'),
            ('WWE SuperStar', '/category/wwe/wwe-superstar/')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base2_link + channel[1], 'image': self.art2_link, 'action': 'wrestlingScrape'})
        self.addDirectory(self.list)
        return self.list

    def root24(self):
        channels = [
            ('AEW Dynamite', '/category/aew-dynamite/'),
            ('AEW PPV', '/category/aew-ppv/'),
            ('AEW', '/category/aew-shows/'),
            ('Bellator MMA', '/category/bellator-mma/'),
            ('Boxing', '/category/boxing/'),
            ('Defiant Wrestling', '/category/defiant-wrestling/'),
            ('DVD Collections', '/category/archives/'),
            ('Evolve Wrestling', '/category/evolve-wrestling/'),
            ('iMPACT', '/category/impact/'),
            ('iMPACT PPV', '/category/impact-ppv/'),
            ('iMPACT Wrestling', '/category/impact-wrestling/'),
            ('iMPACT Xplosion', '/category/impact-xplosion/'),
            ('Indy Wrestling', '/category/indy-wrestling/'),
            ('Lucha Underground', '/category/lucha-underground/'),
            ('MIZ and MRS', '/category/miz-and-mrs/'),
            ('NJPW', '/category/njpw/'),
            ('PPV Collections', '/category/old-ppv-collections/'),
            ('ROH Wrestling iPPV', '/category/roh-wrestling-ippv/'),
            ('ROH Wrestling', '/category/roh-wrestling/'),
            ('RPW PPV', '/category/rpw-ppv/'),
            ('Total Bellas', '/category/total-bellas/'),
            ('TOTAL DIVAS', '/category/total-divas/'),
            ('UFC Fight Night', '/category/ufc-fight-night/'),
            ('UFC PPV', '/category/ufc-ppv/'),
            ('UFC', '/category/ufc/'),
            ('Ultimate Fighter', '/category/ultimate-fighter/'),
            ('WWE 24', '/category/wwe-24/'),
            ('WWE 205 LIVE', '/category/wwe-205-live/'),
            ('WWE After Burn', '/category/wwe-after-burn/'),
            ('WWE Backlash', '/category/wwe-backlash/'),
            ('WWE Battleground', '/category/wwe-battleground/'),
            ('WWE Bottom Line', '/category/wwe-bottom-line/'),
            ('WWE Clash/Night of Champions', '/category/wwe-night-of-champions/'),
            ('WWE Elimination Chamber', '/category/wwe-elimination-chamber/'),
            ('WWE Extreme Rules', '/category/wwe-extreme-rules/'),
            ('WWE Fast Lane', '/category/wwe-fast-lane/'),
            ('WWE Great Balls of Fire', '/category/wwe-great-balls-of-fire/'),
            ('WWE Greatest Matches', '/category/wwe-greatest-matches/'),
            ('WWE Hall of Fame', '/category/wwe-hall-of-fame/'),
            ('WWE Hell in a Cell', '/category/wwe-hell-in-a-cell/'),
            ('WWE Main Event', '/category/wwe-main-event/'),
            ('WWE Money in the Bank', '/category/wwe-money-in-the-bank/'),
            ('WWE Network Shows', '/category/wwe-network/'),
            ('WWE Network Special', '/category/wwe-network-special/'),
            ('WWE NO Mercy', '/category/wwe-no-mercy/'),
            ('WWE NXT TakeOver', '/category/wwe-nxt-takeover/'),
            ('WWE NXT UK', '/category/wwe-nxt-uk/'),
            ('WWE NXT', '/category/wwe-nxt/'),
            ('WWE Payback', '/category/wwe-payback/'),
            ('WWE PPV', '/category/wwe-ppv/'),
            ('WWE RAW', '/category/wwe-raw/'),
            ('WWE Ride Along', '/category/wwe-ride-along/'),
            ('WWE RoadBlock', '/category/wwe-roadblock/'),
            ('WWE Royal Rumble', '/category/wwe-royal-rumble-collections/'),
            ('WWE Shows', '/category/wwe-shows/'),
            ('WWE SmackDown LIVE(Monday?)', '/category/wwe-smackdown-live/'),
            ('WWE SummerSlam', '/category/wwe-summerslam-collections/'),
            ('WWE Survivor Series', '/category/wwe-survivor-series/'),
            ('WWE Table For 3', '/category/wwe-table-for-3/'),
            ('WWE This Week', '/category/wwe-this-week/'),
            ('WWE TLC', '/category/wwe-tlc/'),
            ('WWE Tribute To The Troops', '/category/wwe-tribute-to-the-troops/'),
            ('WWE WrestleMania', '/category/wwe-wrestlemania-collections/')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base3_link + channel[1], 'image': self.art3_link, 'action': 'wrestlingScrape'})
        self.addDirectory(self.list)
        return self.list

    def rootAWL(self):
        channels = [
            ('AEW', '/aew/'),
            ('AEW Pay Per Views', '/aew/aew-ppv/'),
            ('AEW Single Matches', '/aew/aew-single-matches/'),
            ('BattleGround', '/wwe-3/wwe-ppv/battleground/'),
            ('Boxing', '/boxing/'),
            ('Elimination Chamber', '/wwe-3/wwe-ppv/elimination-chamber/'),
            ('Extreme Rules', '/wwe-3/wwe-ppv/extremerules/'),
            ('GFW iMPACT', '/tna/'),
            ('GFW iMPACT Wrestling', '/tna/tna-impact/'),
            ('Greatest Matches', '/more/matches/'),
            ('Hell in a Cell', '/wwe-3/wwe-ppv/hell-in-a-cell/'),
            ('Interviews', '/more/interviews/'),
            ('Lucha Underground', '/lucha-underground/'),
            ('Main Event', '/wwe-3/main-event/'),
            ('Money in the Bank', '/wwe-3/wwe-ppv/money-in-the-bank/'),
            ('More Wrestling', '/more/'),
            ('NJPW', '/njpw/'),
            ('NJPW Pay-Per-Views', '/njpw/njpwppv/'),
            ('Payback', '/wwe-3/wwe-ppv/payback/'),
            ('Ring of Honor', '/ring-of-honor/'),
            ('Ring of Honor Pay Per Views', '/ring-of-honor/roh-ppv/'),
            ('Royal Rumble', '/wwe-3/wwe-ppv/royalrumble/'),
            ('SummerSlam', '/wwe-3/wwe-ppv/summerslam/'),
            ('Survivor Series', '/wwe-3/wwe-ppv/survivor-series/'),
            ('This Week in WWE', '/wwe-3/wwe-network/this-week-in-wwe/'),
            ('TNA Pay Per Views', '/tna/tna-ppv/'),
            ('Total Divas', '/wwe-3/tota-divas/'),
            ('UFC', '/ufc/'),
            ('UFC Fight Night', '/ufc/ufcfightnight/'),
            ('UFC Pay Per Views', '/ufc/ufcppv/'),
            ('Unfiltered with Renee Young', '/wwe-3/wwe-network/wweunfiltered/'),
            ('Wrestlemania', '/wwe-3/wwe-ppv/wrestlemania/'),
            ('Wrestling DVDs', '/more/wrestlingdvds/'),
            ('WWE', '/wwe-3/'),
            ('WWE 24', '/wwe-3/wwe-network/wwe-24/'),
            ('WWE Breaking Ground', '/wwe-3/breaking-ground/'),
            ('WWE Fastlane', '/wwe-3/wwe-ppv/fastlane/'),
            ('WWE Great Balls of Fire', '/wwe-3/wwe-ppv/greate-balls-of-fire/'),
            ('WWE Network Live Stream 24/7', '/watch-wwe-network-online-free-wwe-network-free-live-stream/'),
            ('WWE Network TV Live Stream', '/wwenetwork/'),
            ('WWE Network', '/wwe-3/wwe-network/'),
            ('WWE NXT', '/wwe-3/wwe-nxt/'),
            ('WWE Pay Per Views', '/wwe-3/wwe-ppv/'),
            ('WWE Raw', '/wwe-3/wwe-raw/'),
            ('WWE Ride Along', '/wwe-3/wwe-network/ridealong/'),
            ('WWE SmackDown', '/wwe-3/wwe-smackdown/'),
            ('WWE Superstars', '/wwe-3/superstars/'),
            ('WWE Swerved', '/wwe-3/wwe-network/swerved/')
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base4_link + channel[1], 'image': self.art4_link, 'action': 'wrestlingScrape'})
        self.addDirectory(self.list)
        return self.list

    def scrape(self, url):
        try:
            if self.base1_link in url:
                self.scrape1(url)
            if self.base2_link in url:
                self.scrape2(url)
            if self.base3_link in url:
                self.scrape3(url)
            if self.base4_link in url:
                self.scrape4(url)
        except:
            pass

    def scrape1(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0', 'Referer': self.base1_link}
            html = client.request(url, headers=headers)
            if '/category/' in url:
                page = client.parseDOM(html, 'div', attrs={'class': 'loop-content switchable-view grid-mini'})[0]
                contents = client.parseDOM(page, 'div', attrs={'class': 'thumb'})
                for content in contents:
                    title, link = re.compile('<a class="clip-link" .+? title="(.+?)" href="(.+?)">', re.DOTALL).findall(content)[0]
                    icon = re.compile('<img src="(.+?)"', re.DOTALL).findall(content)[0]
                    item = control.item(label=title)
                    item.setArt({"thumb": icon, "icon": icon})
                    link = '%s?action=wrestlingScrape&url=%s' % (sysaddon, link)
                    self.items.append((link, item, True))
            else:
                contents = re.compile('<p style="text-align: center;">(.+?)</p>', re.DOTALL).findall(html)
                for content in contents:
                    links = re.compile('<a href="(.+?)" class="small cool-blue vision-button" target="_blank">(.+?)</a>', re.DOTALL).findall(content)
                    for link, info1 in links:
                        if not link.startswith('http') or 'educadegree.com' in link:
                            if not link.startswith('http'):
                                link = self.cgi_bin_link + link
                            sourcepage = client.request(link, headers=headers)
                            try:
                                try:
                                    link = re.compile("<iframe.+?src='(.+?)'", flags=re.DOTALL|re.IGNORECASE|re.MULTILINE).findall(sourcepage)[0]
                                except:
                                    link = re.compile('<iframe.+?src="(.+?)"', flags=re.DOTALL|re.IGNORECASE|re.MULTILINE).findall(sourcepage)[0]
                            except:
                                link = link
                        CustomResolved = self.resolve(link)
                        if CustomResolved:
                            link = CustomResolved
                        Blocked = self.checkURL(link)
                        if Blocked:
                            continue
                        icon = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(html)[0]
                        elements = urlparse.urlparse(link)
                        host = elements.netloc
                        title = '[B]%s[/B] - %s' % (host.replace('www.', ''), info1)
                        item = control.item(label=title)
                        item.setProperty("IsPlayable", "true")
                        item.setArt({"thumb": icon, "icon": icon})
                        item.setInfo(type="video", infoLabels={"title": title, "mediatype": "video"})
                        link = '%s?action=wrestlingPlay&url=%s' % (sysaddon, link)
                        self.items.append((link, item, False))
            try:
                navi_link = re.compile('<link rel="next" href="(.+?)" />', re.DOTALL).findall(html)[0]
                next_url = '%s?action=wrestlingScrape&url=%s' % (sysaddon, navi_link)
                item = control.item(label=control.lang(32053).encode('utf-8'))
                item.setArt({"thumb": control.addonNext(), "icon": control.addonNext()})
                self.items.append((next_url, item, True))
            except:
                pass
            if not self.items:
                self.errorForSources()
                self.addDirectoryItem('No Results Found, Go Back to Menu?', 'wrestlingMenuLA', self.art1_link, 'DefaultTVShows.png')
        except Exception:
            pass
        control.addItems(syshandle, self.items)
        self.endDirectory()

    def scrape2(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0', 'Referer': self.base2_link}
            html = client.request(url, headers=headers)
            if '/category/' in url:
                page = client.parseDOM(html, 'div', attrs={'class': 'loop-content switchable-view grid-mini'})[0]
                contents = client.parseDOM(page, 'div', attrs={'class': 'thumb'})
                for content in contents:
                    title, link = re.compile('<a class="clip-link" .+? title="(.+?)" href="(.+?)">', re.DOTALL).findall(content)[0]
                    icon = re.compile('<img src="(.+?)"', re.DOTALL).findall(content)[0]
                    item = control.item(label=title)
                    item.setArt({"thumb": icon, "icon": icon})
                    link = '%s?action=wrestlingScrape&url=%s' % (sysaddon, link)
                    self.items.append((link, item, True))
            else:
                contents = re.compile('<p style="text-align: center;">(.+?)</p>', re.DOTALL).findall(html)
                for content in contents:
                    links = re.compile('<a href="(.+?)" class="small cool-blue vision-button" target="_blank">(.+?)</a>', re.DOTALL).findall(content)
                    for link, info1 in links:
                        if not link.startswith('http') or 'educadegree.com' in link:
                            if not link.startswith('http'):
                                link = self.cgi_bin_link + link
                            sourcepage = client.request(link, headers=headers)
                            try:
                                try:
                                    link = re.compile("<iframe.+?src='(.+?)'", flags=re.DOTALL|re.IGNORECASE|re.MULTILINE).findall(sourcepage)[0]
                                except:
                                    link = re.compile('<iframe.+?src="(.+?)"', flags=re.DOTALL|re.IGNORECASE|re.MULTILINE).findall(sourcepage)[0]
                            except:
                                link = link
                        CustomResolved = self.resolve(link)
                        if CustomResolved:
                            link = CustomResolved
                        Blocked = self.checkURL(link)
                        if Blocked:
                            continue
                        icon = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(html)[0]
                        elements = urlparse.urlparse(link)
                        host = elements.netloc
                        title = '[B]%s[/B] - %s' % (host.replace('www.', ''), info1)
                        item = control.item(label=title)
                        item.setProperty("IsPlayable", "true")
                        item.setArt({"thumb": icon, "icon": icon})
                        item.setInfo(type="video", infoLabels={"title": title, "mediatype": "video"})
                        link = '%s?action=wrestlingPlay&url=%s' % (sysaddon, link)
                        self.items.append((link, item, False))
            try:
                navi_link = re.compile('<link rel="next" href="(.+?)" />', re.DOTALL).findall(html)[0]
                next_url = '%s?action=wrestlingScrape&url=%s' % (sysaddon, navi_link)
                item = control.item(label=control.lang(32053).encode('utf-8'))
                item.setArt({"thumb": control.addonNext(), "icon": control.addonNext()})
                self.items.append((next_url, item, True))
            except:
                pass
            if not self.items:
                self.errorForSources()
                self.addDirectoryItem('No Results Found, Go Back to Menu?', 'wrestlingMenuCZ', self.art2_link, 'DefaultTVShows.png')
        except Exception:
            pass
        control.addItems(syshandle, self.items)
        self.endDirectory()

    def scrape3(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0', 'Referer': self.base3_link}
            html = client.request(url, headers=headers)
            if '/category/' in url:
                page = client.parseDOM(html, 'div', attrs={'class': 'main-content-col-body'})[0]
                contents = client.parseDOM(page, 'div', attrs={'class': 'entry-content'})
                for content in contents:
                    link, title = re.compile('<a href=(.+?) target=_self title="(.+?)">', re.DOTALL).findall(content)[0]
                    icon = re.compile('<img src=(.+?) alt style>', re.DOTALL).findall(content)[0]
                    item = control.item(label=title)
                    item.setArt({"thumb": icon, "icon": icon})
                    link = '%s?action=wrestlingScrape&url=%s' % (sysaddon, link)
                    self.items.append((link, item, True))
            else:
                contents = re.compile('<p style="text-align: center;">(.+?)</p>', re.DOTALL).findall(html)
                for content in contents:
                    links = re.compile('<a class=.+?href="(.+?)" target=_blank.+?>(.+?)</a>', re.DOTALL).findall(content)
                    for link, info1 in links:
                        if 'education-load.com' in link:
                            sourcepage = client.request(link, headers=headers)
                            try:
                                try:
                                    link = re.compile('<iframe.+?src="(.+?)"', flags=re.DOTALL|re.IGNORECASE|re.MULTILINE).findall(sourcepage)[0]
                                except:
                                    link = re.compile("<iframe.+?src='(.+?)'", flags=re.DOTALL|re.IGNORECASE|re.MULTILINE).findall(sourcepage)[0]
                            except:
                                link = link
                        CustomResolved = self.resolve(link)
                        if CustomResolved:
                            link = CustomResolved
                        Blocked = self.checkURL(link)
                        if Blocked:
                            continue
                        icon = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(html)[0]
                        elements = urlparse.urlparse(link)
                        host = elements.netloc
                        title = '[B]%s[/B] - %s' % (host.replace('www.', ''), info1)
                        item = control.item(label=title)
                        item.setProperty("IsPlayable", "true")
                        item.setArt({"thumb": icon, "icon": icon})
                        item.setInfo(type="video", infoLabels={"title": title, "mediatype": "video"})
                        link = '%s?action=wrestlingPlay&url=%s' % (sysaddon, link)
                        self.items.append((link, item, False))
            try:
                navi_link = re.compile('<link rel=next href=(.+?)>', re.DOTALL).findall(html)[0]
                next_url = '%s?action=wrestlingScrape&url=%s' % (sysaddon, navi_link)
                item = control.item(label=control.lang(32053).encode('utf-8'))
                item.setArt({"thumb": control.addonNext(), "icon": control.addonNext()})
                self.items.append((next_url, item, True))
            except:
                pass
            if not self.items:
                self.errorForSources()
                self.addDirectoryItem('No Results Found, Go Back to Menu?', 'wrestlingMenu24', self.art3_link, 'DefaultTVShows.png')
        except Exception:
            pass
        control.addItems(syshandle, self.items)
        self.endDirectory()

    def scrape4(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0', 'Referer': self.base4_link}
            html = client.request(url, headers=headers)
            if '/watch-' in url:
                contents = re.compile('<p style="text-align: center;">(.+?)</p>', re.DOTALL).findall(html)
                for content in contents:
                    links = re.compile('<a href="(.+?)" class="small cool-blue vision-button" target="_blank">(.+?)</a>', re.DOTALL).findall(content)
                    for link, info1 in links:
                        if 'pakfashionstore.com' in link:
                            link = self.cleanURL(link)
                            sourcepage = client.request(link, headers=headers)
                            try:
                                try:
                                    link = re.compile('<iframe.+?src="(.+?)"', flags=re.DOTALL|re.IGNORECASE).findall(sourcepage)[0]
                                except:
                                    link = re.compile("<iframe.+?src='(.+?)'", flags=re.DOTALL|re.IGNORECASE).findall(sourcepage)[0]
                            except:
                                link = link
                        CustomResolved = self.resolve(link)
                        if CustomResolved:
                            link = CustomResolved
                        Blocked = self.checkURL(link)
                        if Blocked:
                            continue
                        icon = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(html)[0]
                        elements = urlparse.urlparse(link)
                        host = elements.netloc
                        title = '[B]%s[/B] - %s' % (host.replace('www.', ''), info1)
                        item = control.item(label=title)
                        item.setProperty("IsPlayable", "true")
                        item.setArt({"thumb": icon, "icon": icon})
                        item.setInfo(type="video", infoLabels={"title": title, "mediatype": "video"})
                        link = '%s?action=wrestlingPlay&url=%s' % (sysaddon, link)
                        self.items.append((link, item, False))
            else:
                page = client.parseDOM(html, 'div', attrs={'class': 'loop-content switchable-view grid-mini'})[0]
                contents = client.parseDOM(page, 'div', attrs={'class': 'thumb'})
                for content in contents:
                    title, link = re.compile('<a class="clip-link" .+? title="(.+?)" href="(.+?)">', re.DOTALL).findall(content)[0]
                    icon = re.compile('<img src="(.+?)"', re.DOTALL).findall(content)[0]
                    item = control.item(label=title)
                    item.setArt({"thumb": icon, "icon": icon})
                    link = '%s?action=wrestlingScrape&url=%s' % (sysaddon, link)
                    self.items.append((link, item, True))
            try:
                navi_link = re.compile('<link rel="next" href="(.+?)" />', re.DOTALL).findall(html)[0]
                next_url = '%s?action=wrestlingScrape&url=%s' % (sysaddon, navi_link)
                item = control.item(label=control.lang(32053).encode('utf-8'))
                item.setArt({"thumb": control.addonNext(), "icon": control.addonNext()})
                self.items.append((next_url, item, True))
            except:
                pass
            if not self.items:
                self.errorForSources()
                self.addDirectoryItem('No Results Found, Go Back to Menu?', 'wrestlingMenuAWL', self.art4_link, 'DefaultTVShows.png')
        except Exception:
            pass
        control.addItems(syshandle, self.items)
        self.endDirectory()

    def cleanURL(self, url):
        url = HTMLParser.HTMLParser().unescape(url)
        url = url.replace('&quot;', '\"')
        url = url.replace('&amp;', '&')
        url = url.replace('\\', '')
        url = url.strip()
        return url

    def checkURL(self, url):
        BlockedList = ['timeanddate.com', 'widgets.amung.us', 'chatangoembed.blogspot.com', 'njpwworldjap.blogspot.com', 'njpwworldeng.blogspot.com',
            'wrestlingnews.in', 'yourvideohost.com', 'vid.gg', 'vidgg.to', 'nowvideo.sx', 'nowdownload.ch', 'novamov.com', 'movshare.net', 'cloudtime.to', 'vidto.me',
            'bestreams.net', 'bitvid.sx', 'auroravid.to', 'vdl.primego.org', 'waaw.tv', 'hqq.tv', 'letwatch.to', 'multiup.org', 'multiup.eu', 'multiup.us', 'moviesfeed.com',
            'intoupload.net', 'youwatch.org', 'player.youku.com', 'player.vimeo.com', 'dailymotion.com', 'imgnuts.com', 'primevideos.net', 'vidgg.club', 'vodhd.net',
            'xn--fu7d.net', 'wholecloud.net'
        ]
        if any([i for i in BlockedList if i in url]):
            return True
        else:
            return False

    def play(self, url):
        try:
            hmf = resolveurl.HostedMediaFile(url, include_disabled=False, include_universal=True)
            if hmf.valid_url() is True:
                link = hmf.resolve()
                if link is None or link is False:
                    link = url
            else:
                link = url
            if not 'User-Agent' in link:
                elements = urlparse.urlparse(link)
                domain = elements.scheme + '://' + elements.netloc
                uAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
                link = '%s|User-Agent=%s&Referer=%s' % (link, uAgent, domain)
            title = control.infoLabel('listitem.label')
            icon = control.infoLabel('listitem.icon')
            li = control.item(title, path=link)
            li.setProperty("IsPlayable", "true")
            li.setArt({"thumb": icon, "icon": icon})
            li.setInfo(type="video", infoLabels={"title": title})
            control.resolve(handle=int(sys.argv[1]), succeeded=True, listitem=li)
        except Exception:
            pass

    def resolve(self, url):
        try:
            url =  "https:" + url if not url.startswith('http') else url
            liveList = ['educadegree.com', 'education-load.com', 'cricfree.ws', 'sawlive.net', 'wlive.tv', 'yoursports.stream']
            if any([i for i in liveList if i in url]):
                link = self.resolveA(url)
                if link is None or link is False:
                    link = url
            else:
                link = url
            link = self.cleanURL(link)
            return link
        except Exception:
            return

    def resolveA(self, url):
        try:
            r = client.request(url)
            r = r.replace('\\', '')
            s = re.findall('\s*:\s*\"(http.+?)\"', r) + re.findall('\s*:\s*\'(http.+?)\'', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = re.findall('\s*\(\s*\"(http.+?)\"', r) + re.findall('\s*\(\s*\'(http.+?)\'', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = re.findall('\s*=\s*\'(http.+?)\'', r) + re.findall('\s*=\s*\"(http.+?)\"', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = re.findall('\s*:\s*\"(//.+?)\"', r) + re.findall('\s*:\s*\'(//.+?)\'', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = re.findall('\:\"(\.+?)\"', r) + re.findall('\:\'(\.+?)\'', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = re.findall('\s*\(\s*\"(//.+?)\"', r) + re.findall('\s*\(\s*\'(//.+?)\'', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = re.findall('\s*=\s*\'(//.+?)\'', r) + re.findall('\s*=\s*\"(//.+?)\"', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = re.findall('\w*:\s*\"(http.+?)\"', r) + re.findall('\w*:\s*\'(http.+?)\'', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = re.findall('\w*=\'([^\']*)', r) + re.findall('\w*="([^"]*)', r)
            s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
            if not s:
                s = client.parseDOM(r,'source', ret='src', attrs={'type': 'video.+?'})
            s = ['http:' + i if i.startswith('//') else i for i in s]
            s = [urlparse.urljoin(url, i) if not i.startswith('http') else i for i in s]
            s = [x for y,x in enumerate(s) if x not in s[:y]]
            self.u = []

            def request(i):
                try:
                    c = client.request(i, output='headers')
                    checks = ['video', 'mpegurl']
                    if any(f for f in checks if f in c['Content-Type']):
                        self.u.append((i, int(c['Content-Length'])))
                except:
                    pass
            threads = []
            for i in s:
                threads.append(workers.Thread(request, i))
            [i.start() for i in threads] ; [i.join() for i in threads]
            u = sorted(self.u, key=lambda x: x[1])[::-1]
            u = client.request(u[0][0], output='geturl', referer=url)
            return u
        except Exception:
            return url

    def errorForSources(self):
        control.infoDialog(control.lang(32401).encode('utf-8'), sound=False, icon='INFO')

    def addDirectory(self, items, queue=False, isFolder=True):
        if items is None or len(items) is 0:
            control.idle()
            sys.exit()
        for i in items:
            try:
                name = i['name']
                if i['image'].startswith('http'):
                    thumb = i['image']
                elif artPath is not None:
                    thumb = os.path.join(artPath, i['image'])
                else:
                    thumb = addonThumb
                item = control.item(label=name)
                if isFolder:
                    url = '%s?action=%s' % (sysaddon, i['action'])
                    try:
                        url += '&url=%s' % urllib.quote_plus(i['url'])
                    except:
                        pass
                    item.setProperty('IsPlayable', 'false')
                else:
                    url = '%s?action=%s' % (sysaddon, i['action'])
                    try:
                        url += '&url=%s' % i['url']
                    except:
                        pass
                    item.setProperty('IsPlayable', 'true')
                    item.setInfo("mediatype", "video")
                item.setArt({'icon': thumb, 'thumb': thumb})
                if addonFanart is not None:
                    item.setProperty('Fanart_Image', addonFanart)
                control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)
            except:
                pass
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)

    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
        try:
            name = control.lang(name).encode('utf-8')
        except:
            pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        if thumb.startswith('http'):
            thumb = thumb
        else:
            thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue is True:
            cm.append((control.lang(32065).encode('utf-8'), 'RunPlugin(%s?action=queueItem)' % sysaddon))
        if not context is None:
            cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart is None:
            item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)

    def endDirectory(self, contentType='addons', sortMethod=xbmcplugin.SORT_METHOD_NONE):
        control.content(syshandle, contentType)
        control.sortMethod(syshandle, sortMethod)
        control.directory(syshandle, cacheToDisc=True)


