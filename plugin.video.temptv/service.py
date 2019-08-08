# -*- coding: utf-8 -*-

from resources.lib.modules import log_utils
from resources.lib.modules import control

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

try:
    AddonVersion = control.addon('plugin.video.temptv').getAddonInfo('version')
    RepoVersion = control.addon('repository.temptv').getAddonInfo('version')

    log_utils.log(' TEMPTV PLUGIN VERSION: %s ' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log(' TEMPTV REPOSITORY VERSION: %s ' % str(RepoVersion), log_utils.LOGNOTICE)
except:
    log_utils.log('CURRENT TEMPTV VERSIONS REPORT ', log_utils.LOGNOTICE)
    log_utils.log('### ERROR GETTING TEMPTV VERSIONS - NO HELP WILL BE GIVEN AS THIS IS NOT AN OFFICIAL TEMPTV INSTALL. ', log_utils.LOGNOTICE)

