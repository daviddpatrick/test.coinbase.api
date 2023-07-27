from common.fixtures.base_test_fixture import BaseTestFixture


class TestCoinbase(BaseTestFixture):

    def test_get_bitcoin_price(self, config, clients, session_logger):
        coinbase_client = clients.create(name="CoinbaseApiClient",
                                         base_url=config["coinbase_url"], logger=session_logger)
        btc_usd_price = coinbase_client.get_btc_usd_price()
        assert int(float(btc_usd_price)) > 0
