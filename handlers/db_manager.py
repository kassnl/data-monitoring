#!
__author__ = 'kassandracharalampidou'

from datetime import datetime
from models import ActiveQueue
from helpers import safe_session, autoconnect
import sqlalchemy as sa
import copy

PROD_DB_NAME = 'DATABASE_PROD'
DEV_DB_NAME = 'DATABASE_DEV'

class DBManagerFactory():
    def __init__(self, settings, rds_name, db_name=None):
        self.settings = settings
        self.rds_name = rds_name
        self.db_name = db_name
        if self.db_name is None:
            self.db_name = settings.get(rds_name, 'default_db')

    def get_manager(self):
        engine, session = autoconnect(dict(self.settings.items(self.rds_name)), self.db_name)
        if self.rds_name in (PROD_DB_NAME, DEV_DB_NAME):
            return GlobalDBManager(session, engine)
        return None


class AbstractDBManager():
    '''
    Manages queries from the db and injects results to procedures that need them
    '''
    @safe_session
    def __init__(self, session, engine):
        self.session = session
        self.engine = engine

    def db_flush(self):
        self.session.flush()

    def db_commit(self):
        self.session.commit()

    def close(self):
        self.session.close()
        self.engine.dispose()


class GlobalDBManager(AbstractDBManager):
    def get_active_customers(self):
        customers = self.session.query(ActiveQueue.customer).filter(sa.or_(ActiveQueue.reminder_active == 1,\
                                                                           ActiveQueue.active == 1, \
                                                                           ActiveQueue.custom_active == 1))
        return customers
