from unittest.mock import Mock

import pytest

import clog_client as clog


@pytest.fixture
def patch_requests(monkeypatch):
    import requests
    mock = Mock(spec=requests)
    monkeypatch.setattr('clog_client.core.requests', mock)
    return mock


def test_log(patch_requests):
    req = patch_requests
    clog.log('Exception message', metadata={'id': 5})
    req.post.assert_called_once_with(
        'http://localhost:5000/api/v1/logs/',
        data={
            'source': 'test',
            'log': {
                'data': 'Exception message',
                'metadata': {'id': 5}
            }
        },
        timeout=1
    )
