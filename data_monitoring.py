__author__ = 'kassandracharalampidou'
from logging.config import dictConfig
from handlers.db_manager import PROD_DB_NAME, DEV_DB_NAME
from handlers.db_manager import DBManagerFactory
from settings.logging_settings import LOGGING
from settings.constants import SettingsGenerator
from handlers.result_formatter import QueryResultsFormatter, RDSResultFormatter
from os import listdir
from os.path import isfile, join
import datetime
import sendgrid


def run(host_name):
    settings = SettingsGenerator().get_settings()
    db_manager = DBManagerFactory(settings, host_name).get_manager()
    customers = db_manager.get_active_customers()
    db_manager.session.close()
    rds_formatter = RDSResultFormatter()

    for f in listdir(settings.get('MISC', 'query_dir')):
        with open (QUERY_DIR + f, "r") as myfile:
            sql_query = myfile.read().replace('\n', ' ')
            query_formatter = QueryResultsFormatter(f)
            for customer in customers:
                customer_name = str(customer[0])
                customer_manager = DBManagerFactory(settings, host_name, customer_name).get_manager()
                now = datetime.datetime.now()
                result = customer_manager.engine.execute(sql_query %(customer_name, now.month, now.year))
                query_formatter.add_result(customer_name, result)
                result.close()
                customer_manager.close()
    rds_formatter.add_query_result(query_formatter)
    send_mail(rds_formatter.get_string())



def send_mail(text):
    settings = SettingsGenerator().get_settings()
    message = sendgrid.Mail(to=settings.get('MAIL', 'recipient'),
                            subject=settings.get('MAIL', 'subject'),
                            text=text,
                            from_email=settings.get('MAIL', 'sender'))
    sg = sendgrid.SendGridClient(settings.get('SENDGRID', 'user'), settings.get('SENDGRID', 'pasw'), raise_errors=True)
    try:
        sg.send(message)
    except Exception as e:
        raise SendgridError(e)


if __name__ == '__main__':
    dictConfig(LOGGING)
    run(DEV_DB_NAME)
