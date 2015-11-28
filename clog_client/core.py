import requests

from .config import Config


def log(data, metadata={}):
    payload = {'log': {'data': data, 'metadata': metadata},
               'source': Config.source}
    return requests.post('{}/api/v1/logs/'.format(Config.server_url),
                         data=payload)
