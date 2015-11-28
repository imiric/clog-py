clog-py
=======

Clog is a centralized logging system.

This is the Python client-side counterpart to
[clog-server](https://github.com/imiric/clog-server) for submitting log data via
a JSON API.


Setup
-----

```
pip install git+https://github.com/imiric/clog-py.git
```


Usage
-----


```
import traceback
from clog_client import log

try:
    1/0
except ZeroDivisionError:
    log(traceback.format_exc())
```

You can also include some metadata about the event:

```
log('Exception', metadata={'id': 5})
```


Configuration
-------------

Configuration is done via environment variables:

- `CLOG_HOST`: Host name or IP address to connect to. [default: `"localhost"`]
- `CLOG_PORT`: The port the server is listening on. [default: `5000`]
- `CLOG_SOURCE`: The identifier for the client's logs on the server. [default: current hostname]
- `CLOG_TIMEOUT`: Server request timeout. [default: 1s]


Tests
-----

Install [tox](https://tox.readthedocs.org/en/latest/install.html) and run:

```
$ tox
```


License
-------

[MIT](LICENSE)
