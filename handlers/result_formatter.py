__author__ = 'kassandracharalampidou'

class RDSResultFormatter():
    def __init__(self):
        self.queries_results = []

    def add_query_result(self, query_name):
        self.queries_results.append(query_name)

    def get_string(self):
        message = ''
        for query_result in self.queries_results:
            message = message + query_result.get_string() + "\n"
        return message



class QueryResultsFormatter():
    def __init__(self, name):
        self.query_name = name
        self.results = {}

    def add_result(self, customer, result):
        count = result.fetchall()[0]
        if count[0] > 0:
            self.results[customer] = str(count[0])

    def get_string(self):
        message = self.query_name
        if len(self.results) == 0:
            return message + '................... OK'
        for key, value in self.results.iteritems():
            message = message + "\n" + key + '...................' + value
        return message