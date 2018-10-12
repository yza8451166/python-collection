# from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor
# import time
# def task(arg):
#     print(arg)
#     time.sleep(1)
#
# # pool = ProcessPoolExecutor(5)
# pool = ThreadPoolExecutor(5)
#
# for i in range(50):
#     pool.submit(task,i)


import json
from datetime import date
from datetime import datetime


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        elif isinstance(field, Response):
            return field.__dict__
        else:
            return json.JSONEncoder.default(self, field)

class Response(object):
    def __init__(self):
        self.status =True
        self.data = "asdf"
data = {
    'k1': 123,
    'k2': datetime.now(),
    'k3': Response()
}
ds = json.dumps(data, cls=JsonCustomEncoder)
print(ds)