#! coding:utf-8
'''
Parses settings file
@author: kcharalampidou
@date: 14.04.2014
@copyright (c) 2014 Directness

'''

import os
import json
import urllib2
import ConfigParser
import __root__
from monitoring_exceptions import ConfigurationFileNotFound

CONFIG_DIR = "settings/conf/"
SETTINGS_FILENAME = "settings.conf"


class SettingsGenerator:
    def get_settings(self):
        config = ConfigParser.RawConfigParser()
        # Checks if the settings settings file already exists
        if os.path.isfile(os.path.join(__root__.path(), CONFIG_DIR + SETTINGS_FILENAME)):
            config.read(CONFIG_DIR + SETTINGS_FILENAME)
            return config
        raise ConfigurationFileNotFound(CONFIG_DIR + SETTINGS_FILENAME)
