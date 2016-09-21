# coding: utf-8

import sys
from tables import app
from gevent import monkey
monkey.patch_all()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        path = sys.argv[2]
        host, port = path.split(':')
    else:
        host = "127.0.0.1"; port = "5060";
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        app.run(debug=True, host=host, port=int(port))
