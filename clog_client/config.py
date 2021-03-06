import os
import socket


class Config:
    host = os.getenv('CLOG_HOST', 'localhost')
    port = os.getenv('CLOG_PORT', '5000')
    server_url = 'http://{}:{}'.format(host, port)
    request_timeout = os.getenv('CLOG_TIMEOUT', 1)
    source = os.getenv('CLOG_SOURCE', socket.gethostname())
