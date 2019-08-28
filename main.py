#!/usr/bin/env python3
# encoding: utf-8

import argparse
import time
from http.server import HTTPServer

from handles import ServerHandler


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='NETIO PUSH Data logger')
    parser.add_argument('-n', '--host', help='Address to attach server to', required=False, default='0.0.0.0')
    parser.add_argument('-p', '--port', help='Port to listen on', required=False, default=9000)
    args = vars(parser.parse_args())
    # {'host': 'localhost', 'port': 9000, 'name': 'log', 'output': 'log/'}

    httpd = HTTPServer((args['host'], args['port']), ServerHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (args['host'], args['port']))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (args['host'], args['port']))
