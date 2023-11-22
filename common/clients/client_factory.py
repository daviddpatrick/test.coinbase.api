from common.clients.coinbase_client import CoinbaseApiClient


class ClientFactory(object):

    def create(self, name, base_url, logger, auth_token=None, extra_headers=None):
        while name:
            api_clients = {
                "CoinbaseApiClient": lambda: CoinbaseApiClient(base_url, logger, auth_token, extra_headers)
            }
            try:
                return api_clients[name]()
            except KeyError:
                raise ValueError(f"Invalid client name: {name}")
