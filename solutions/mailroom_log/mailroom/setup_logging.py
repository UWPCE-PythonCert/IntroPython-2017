import os
import logging.config
import yaml


def setup_logging(
    default_path='mailroom/logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'):
    """Setup logging configuration

    """
    # fancy setup that lets you override the default config with 
    # an environmental variable. Handy for when others want to
    # use their code, and you want an easy way for them to use
    # their own config without changing your code or over-writing
    # the default yaml file.
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    logging.addHandler()
