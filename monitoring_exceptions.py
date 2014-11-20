__author__ = 'kassandracharalampidou'

import traceback
import logging
logger = logging.getLogger(name='monitoring_log')


class ConfigurationFileNotFound(Exception):
    def __init__(self, filename):
        self.msg = 'Configuration file not found' % filename
        logger.error(self.msg)
        pass

    def __str__(self):
        return self.msg


class SendgridError(Exception):
    def __init__(self, exception):
        self.msg = 'Fail to send mail: %s' % exception
        logger.error(self.msg)
        pass

    def __str__(self):
        return self.msg