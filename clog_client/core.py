import warnings

import requests

from .config import Config


class ClogRequestWarning(Warning):
    pass


def log(data, metadata={}):
    payload = {'log': {'data': data, 'metadata': metadata},
               'source': Config.source}
    try:
        res = requests.post('{}/api/v1/logs/'.format(Config.server_url),
                            data=payload, timeout=Config.request_timeout)
    except requests.exceptions.RequestException as e:
        # TODO: Add retry and/or failover/queue mechanism.
        warnings.warn(str(e), ClogRequestWarning)

    return res
