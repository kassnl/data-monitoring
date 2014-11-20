===========
Simple data monitoring
===========
Runs a list of queries on a list of databases and mails the results

Requirements:
===========
$ sh bootstrap.sh

Use:
===========
$ python data_monitoring.py

Configuration:
===========
conf/settings.conf file contains:

[MISC]
query_dir = Directory that contains all test queries

[MAIL]
recipient = List of mailing recipients
