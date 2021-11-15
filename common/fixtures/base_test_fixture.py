import logging
import os
import pytest

from datetime import datetime
from common.utils.configs_util import load_config, create_directory_if_necessary
from common.clients.client_factory import ClientFactory


class BaseTestFixture:

    @pytest.fixture(scope='session')
    def test_env(self, request):
        return request.config.getoption(name='--test_env')

    @pytest.fixture(scope='session')
    def config(self, test_env, session_logger):
        env_config = load_config(test_env)
        session_logger.info(f"Using these Environment Configs: {env_config}")
        return env_config

    @pytest.fixture(scope='session')
    def clients(self):
        return ClientFactory()

    @pytest.fixture(scope='session')
    def session_logger(self, worker_id):
        result_dir = os.path.join("results")
        create_directory_if_necessary(result_dir)
        self.session_logger = self.create_logger(result_dir, f"Log_{worker_id.capitalize()}_Session.log", logger_name="session")
        self.session_logger.info('*********************** Session Logging ****************************')
        self.session_logger.info('=================================================================')
        start = datetime.now()
        self.session_logger.info(f'Starting test:')
        yield self.session_logger

        stop = datetime.now()
        duration = stop - start
        self.session_logger.info(f'Test Duration: {duration.total_seconds()} seconds')
        self.session_logger.info(f'FINISHED')
        self.session_logger.info('=================================================================')

    def create_logger(self, result_dir, log_file_name, logger_name="", log_level=None):
        logging.getLogger("selenium").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("PIL").setLevel(logging.WARNING)
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(asctime)-22s - %(levelname)-8s %(message)s')
        formatter.datefmt = '%m/%d/%Y %I:%M:%S %p'
        log = os.path.join(result_dir, log_file_name)
        file_handler = logging.FileHandler(log, mode='w')
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        if log_level is not None:
            logger.setLevel(log_level)
        else:
            logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        return logger
