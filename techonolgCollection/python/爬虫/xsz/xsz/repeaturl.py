#__anthor:  "xuchen:
#date:   2018/3/26
class UrlFilter(object):

    def __init__(self):
        self.visited_urls= set()

    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):

        if request.url in self.visited_urls:
            return True
        self.visited_urls.add(request.url)
        print(request.url)

        return False

    def open(self):  # can return deferred
        print('open.............')
        pass

    def close(self, reason):  # can return a deferred
        pass

    def log(self, request, spider):  # log that a request has been filtered
        pass