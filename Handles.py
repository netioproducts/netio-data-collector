import json
from http.server import BaseHTTPRequestHandler
import os

from Config import Config
from Utils import flatten


class ServerHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Expose nodes for cobra to post requests to
        parse the input according to request and send it to proper parser
        """
        print(self.headers['Content-Type'])

        if self.path == '/push/json' and 'application/json' in self.headers['Content-Type']:
            data = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
            parse_json(data)
        elif self.path == '/push/xml' and 'application/xml' in self.headers['Content-Type']:
            data = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
            parse_xml(data)
        else:
            self.respond()

        self.respond(200)

    def respond(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('OK', 'UTF-8'))


def save(dict_data: dict):
    """
    Accept data in common format, convert them and save it.
    The folder to save to and the format to save it is specified in Config.

    The file name is composed of specified file name, MAC address specified in the request and
    file format
    [fname] + [mac] + [.json | .csv ...]
    """

    serial = dict_data['Status']['Agent']['MAC']
    fname = Config.fname + serial.lower().replace(':', '') + '.' + Config.format
    fpath = os.path.join(Config.folder, fname)

    if not os.path.exists(Config.folder):
        os.makedirs(Config.folder)

    is_first = not(os.path.exists(fpath))

    with open(fpath, 'a') as fp:

        if Config.format == 'CSV':
            save_to_csv(dict_data, fp, is_first)
        elif Config.format == 'JSON':
            save_to_json(dict_data, fp)
        else:
            raise Exception('invalid save format or not supported')


def parse_json(data: str) -> None:
    """
    parse the incoming json string to dictionary and save it
    :param data:
    :return:
    """
    json_data = json.loads(data)
    save(json_data)


def parse_xml(data: str) -> None:
    """
    parse the incoming xml request to dictionary and save it
    """
    raise NotImplementedError('XML parsing was not yet implemented, but you could be the one '
                              'who will do it')


def save_to_json(data: dict, fp):
    """
    Convert to json and write the json to file with trailing new-line, each request to new line.
    The whole file will not be JSON compatible as it will have more top-level entries per file,
    but filebeat can work with that.

    :param data: dictionary to save
    :param fp: stream to save the json to
    """
    fp.write(json.dumps(data))
    fp.write('\n')


def save_to_csv(json_data: dict, fp, is_first=False):
    """
        Let's abuse the fact, that cobra scheme doesn't change between each entry, so we log the
    scheme on the first request and then assume it will not change

    :param json_data: dictionary with data to log
    :param fp: file stream to write to
    :param is_first: if True, save the scheme
    """

    if is_first:
        for key, value in flatten(json_data).items():
            fp.write(str(key))
            fp.write(',')
        fp.write('\n')

    for key, value in flatten(json_data).items():
        fp.write(str(value))
        fp.write(',')
    fp.write('\n')


