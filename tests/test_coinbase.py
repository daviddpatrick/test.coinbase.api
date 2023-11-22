from common.fixtures.base_test_fixture import BaseTestFixture
from retrying import retry
from json import JSONDecodeError


class TestCoinbase(BaseTestFixture):
    @retry(retry_on_exception=lambda x: isinstance(x, JSONDecodeError), stop_max_attempt_number=3, wait_fixed=4000)
    def test_get_bitcoin_price(self, config, clients, session_logger):
        coinbase_client = clients.create(name="CoinbaseApiClient",
                                         base_url=config["coinbase_url"], logger=session_logger)
        btc_usd_price = coinbase_client.get_btc_usd_price()
        assert int(float(btc_usd_price)) > 0
