from datetime import datetime
from linkapp import hashids

class Link():

    def __init__(self, url, domain, network, publisher):
        self.url = url
        url = url
        domain = domain
        nwtwork = network
        publisher = publisher

    @staticmethod
    def get_item(code):
        import json
        f = open('config_data.json')
        js_data = json.load(f)
        if code in js_data['urls'].keys():
            return js_data['urls'][code]
        else:
            return -1

    @staticmethod
    def get_all_data():
        import json
        f = open('config_data.json')
        js_data = json.load(f)
        return js_data['urls']

    @staticmethod
    def update_item(code, data):
        import json
        f = open('config_data.json')
        js_data = json.load(f)
        js_data['urls'][code] = data
        # dump into file
        return js_data['urls']

    @staticmethod
    def delete_item(code):
        import json
        with open('config_data.json', 'r+') as f:
            try:
                js_data = json.load(f)
                js_data['urls'].pop(code, None)
                f.seek(0)
                json.dump(js_data, f, indent=4)
                f.truncate()
            except Exception as e:
                print(e.message)
        return js_data['urls']

    @staticmethod
    def add_item(code, data):
        from time import time
        import json
        if code == 0:
            ts = int(time())
            code = hashids.encode(ts)
        with open('config_data.json', 'r+') as f:
            try:
                js_data = json.load(f)
                js_data['urls'][code] = data
                f.seek(0)
                json.dump(js_data, f, indent=4)
                f.truncate()
            except Exception as e:
                print(e.message)
        return js_data['urls']
