#! coding:utf-8

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class CustomerList(Base):
    __tablename__ = 'cgcore_companies'

    id = sa.Column(sa.Integer, primary_key=True)
    company_name = sa.Column(sa.String(length=25), default='', nullable=False)
    secure_word = sa.Column(sa.String(length=4), default='', nullable=False)
    timezone = sa.Column(sa.String(length=255), default='Europe/Amsterdam', nullable=False)
    mysql_server = sa.Column(sa.Integer, nullable=False)
    mysql_username = sa.Column(sa.String(length=50), nullable=False)
    mysql_password = sa.Column(sa.String(length=50), nullable=False)
    mysql_database = sa.Column(sa.String(length=50), nullable=False)
    package = sa.Column(sa.String(length=20), nullable=False)
    s3_bucket = sa.Column(sa.String(length=15), nullable=False)
    agent_login = sa.Column(sa.Boolean, nullable=False)
    ip_lock = sa.Column(sa.Boolean, nullable=False)
    mail_report = sa.Column(sa.Boolean, default=False, nullable=False)
    google_translate = sa.Column(sa.Boolean, nullable=False)
    salesforce = sa.Column(sa.Boolean, nullable=False)
    sms = sa.Column(sa.Boolean, nullable=False)
    summary = sa.Column(sa.Boolean, nullable=False)
    open_dashboard = sa.Column(sa.Boolean, nullable=False)
    alias = sa.Column(sa.String(length=120), nullable=False)
    primary_active = sa.Column(sa.Boolean, default=True, nullable=False)
    reminder_active = sa.Column(sa.Boolean, default=True, nullable=False)
    custom_active = sa.Column(sa.Boolean, default=True, nullable=False)
    smtp_active = sa.Column(sa.Boolean, default=True, nullable=False)
    sending_active = sa.Column(sa.Boolean, default=True, nullable=False)
    salesforce_case = sa.Column(sa.Boolean, default=True, nullable=False)
    data_model = sa.Column(sa.Text())

class ActiveQueue(Base):
    __tablename__ = 'active_queues'

    id = sa.Column(sa.Integer, primary_key=True)
    customer = sa.Column(sa.String(length=50), nullable=False)
    active = sa.Column(sa.Boolean, default=True, nullable=False)
    smtp_active = sa.Column(sa.Boolean, default=True, nullable=False)
    reminder_active = sa.Column(sa.Boolean, default=True, nullable=False)
    custom_active = sa.Column(sa.Boolean, default=True, nullable=False)
    cleaner_active = sa.Column(sa.Boolean, default=True, nullable=False)
    sending_active = sa.Column(sa.Boolean, default=True, nullable=False)
    language = sa.Column(sa.String(length=10), default='', nullable=False)
