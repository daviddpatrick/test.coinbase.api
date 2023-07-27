import json
from common.http_base.http_base import HttpClientBase


class HTTPError(Exception):
    def __init__(self, status):
        self.status = status

    def __str__(self):
        return repr(self.status)


class CoinbaseApiClient(HttpClientBase):

    def __init__(self,
                 base_url,
                 logger,
                 admin_url=None,
                 auth_token=None,
                 http_timeout=(5, 30),
                 content_type='application/json',
                 extra_headers=None):
        super(CoinbaseApiClient, self).__init__(base_url=base_url,
                                                logger=logger,
                                                auth_token=auth_token,
                                                http_timeout=http_timeout,
                                                content_type=content_type,
                                                extra_headers=extra_headers)
        if extra_headers is None:
            extra_headers = {}
        self.admin_url = admin_url
        self.logger = logger
        self.logger.info("Coinbase API Client")

    def get_btc_usd_price(self):
        get_url = 'prices/BTC-USD/buy'
        response = self._get(get_url)
        self.logger.info(f'The price of Bitcoin is: ${json.loads(response.text)["data"]["amount"]}, you\'re a winner!')
        return json.loads(response.text)["data"]["amount"]
