from common.clients.coinbase_client import CoinbaseApiClient


class ClientFactory(object):

    def create(self, name, base_url, logger):
        if name == "CoinbaseApiClient":
            return self.coinbase_api_client(base_url, logger)

    def coinbase_api_client(self, base_url, logger):
        return CoinbaseApiClient(base_url=base_url, logger=logger)
