from personal_do_not_git import IG
import requests
from pprint import pprint as pp
import json

import logging

#logging.basicConfig(level=logging.DEBUG)

#import http.client

#httpclient_logger = logging.getLogger("http.client")

def httpclient_logging_patch(level=logging.DEBUG):
    """Enable HTTPConnection debug logging to the logging framework"""

    def httpclient_log(*args):
        httpclient_logger.log(level, " ".join(args))

    # mask the print() built-in in the http.client module to use
    # logging instead
    http.client.print = httpclient_log
    # enable debugging
    http.client.HTTPConnection.debuglevel = 1

class Broker():
    pass

class IG(Broker):

    personal = IG()

    ## init
    sessionurl = None
    marketnavigation = None
    
    ### trading
    neworderurl = None
    closeorderurl = None
    checkorderurl = None
    positionsurl = None
    pricesurl = None
    marketsurl = None
    updateorderurl = None
    transactionhistoryurl = None
    confirmsurl = None

    ### other parts of request
    headers = None
    headers_v2 = None
    payload = None
    

    def __init__(self):

        self.timeframes = {'m30':'MINUTE_30',
                            'm1':'MINUTE',
                            'm10':'MINUTE_10'
        }

        if self.personal.is_demo():
            self.ig_host="demo-api.ig.com"
        else:
            self.ig_host="api.ig.com"

        #init
        self.sessionurl = "https://%s/gateway/deal/session" % self.ig_host

        #trading and orders
        self.neworderurl = 'https://%s/gateway/deal/positions/otc' % self.ig_host
        self.closeorderurl = 'https://%s/gateway/deal/positions/otc' % self.ig_host
        self.checkorderurl = 'https://%s/gateway/deal/confirms/' % self.ig_host
        self.positionsurl = 'https://%s/gateway/deal/positions' % self.ig_host
        self.pricesurl = 'https://' + self.ig_host + '/gateway/deal/prices/%s/%s/2'

        self.marketsurl = 'https://'+ self.ig_host + '/gateway/deal/markets/%s'
        self.updateorderurl = 'https://' + self.ig_host + '/gateway/deal/positions/otc/%s'
        self.transactionhistoryurl = 'https://' + self.ig_host + '/gateway/deal/history/transactions/ALL/%s/%s'
        self.confirmsurl = 'https://'+ self.ig_host + '/gateway/deal/confirms/%s'

        self.marketnavigation = f"https://{self.ig_host}/gateway/deal/marketnavigation"

        self.headers = {'content-type': 'application/json; charset=UTF-8', 
                'Accept': 'application/json; charset=UTF-8',
                'version':1, 'X-IG-API-KEY': self.personal.api_key}

        self.headers_v2 = {'content-type': 'application/json; charset=UTF-8',
                        'Accept': 'application/json; charset=UTF-8', 
                        'version':'2', 
                        'X-IG-API-KEY': self.personal.api_key}

        self.payload = {'identifier': self.personal.username, 
                    'password': self.personal.password}
        
        self.get_historical_url = 'https://' + self.ig_host + '/gateway/deal/prices/'


    def connect(self):
        
        #httpclient_logging_patch()
        self.connection = requests.post(self.sessionurl, 
                                        data=json.dumps(self.payload), 
                                        headers=self.headers_v2, 
                                        proxies=self.personal.proxies)

        self.headers_after_login = {'content-type': 'application/json; charset=UTF-8',
                        'Accept': 'application/json; charset=UTF-8', 
                        'version':'3', 
                        'X-IG-API-KEY': self.personal.api_key,
                        'X-SECURITY-TOKEN':self.connection.headers.get('X-SECURITY-TOKEN'),
                        'CST':self.connection.headers.get('CST')}

    def get_historical(self, epic, resolution, start, end):

        data = {'resolution':resolution, 'from': start, 'to': end, 'pageSize': '0'}

        self.history = requests.get(self.get_historical_url + epic, params = data,
                        headers = self.headers_after_login, proxies = self.personal.proxies)

        pp(self.history.json())

if __name__ == "__main__":

    r = IG()
    r.connect()

    epic = 'CS.D.EURUSD.CFD.IP'
    start = "2020-02-01"
    end = "2020-03-01"
    resolution = r.timeframes['m10']

    r.get_historical(epic, resolution, start, end)
    


