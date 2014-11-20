SELECT count(*) FROM %s.cgnpsdata_awaiting
WHERE
process='P' AND
status='201' AND
month(date_email_sent) = %s AND
year(date_email_sent) = %s