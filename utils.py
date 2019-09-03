import collections
import socket


def flatten(d: collections.MutableMapping, parent_key='', sep='.') -> dict:
    """flattens directory so there isn't any dict or list in items
    renames keys of nested dictionaries, so that there are no conflicts
    >>> flatten({'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]})
    {'a': 1, 'c.a': 2, 'c.b.x': 5, 'c.b.y': 10, 'd.0': 1, 'd.1': 2, 'd.2': 3}

    """
    items = []

    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        elif isinstance(v, (tuple, list, set)):
            items.extend(flatten(
                dict([(new_key + '.' + str(idx), itm) for idx, itm in enumerate(v)])).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_local_ip():
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        soc.connect(('10.255.255.255', 1))
        IP = soc.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        soc.close()
    return IP