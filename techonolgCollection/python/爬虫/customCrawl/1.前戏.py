# __anthor:  "xuchen:
# date:   2018/3/27
from twisted.internet import reactor
from twisted.internet import defer
from twisted.web.client import getPage

#
#
#
# def response(content):
#     print(content)
#
# @defer.inlineCallbacks
# def task():
#     url ="http://www.baidu.com"
#     d = getPage(url.encode('utf-8'))
#     d.addCallback(response)
#     yield d
#
# task()
# reactor.run()


# def done(*args,**kwargs):
#     reactor.stop()
#
#
# def response(content):
#     print(content)
#
# @defer.inlineCallbacks
# def task():
#     url ="http://www.baidu.com"
#     d = getPage(url.encode('utf-8'))
#     d.addCallback(response)
#     yield d
#
# d=task()
# dd =defer.DeferredList([d,])
# dd.addBoth(done)
# reactor.run()


_close = None
count = 0


def done(*args, **kwargs):
    reactor.stop()


def response(content):
    print(content)
    global count
    count += 1
    if count == 3:
        _close.callback(None)


@defer.inlineCallbacks
def task():
    url = "http://www.baidu.com"
    d1 = getPage(url.encode('utf-8'))
    d1.addCallback(response)

    url = "http://www.bing.com"
    d2 = getPage(url.encode('utf-8'))
    d2.addCallback(response)

    url = "http://www.cnblogs.com"
    d3 = getPage(url.encode('utf-8'))
    d3.addCallback(response)

    global _close
    _close = defer.Deferred()
    yield _close


spider1 = task()
# spider2 = task()
dd = defer.DeferredList([spider1, ])
dd.addBoth(done)
reactor.run()
