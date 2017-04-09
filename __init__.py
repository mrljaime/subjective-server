import sys
import tornado.web
import tornado.ioloop
import json
from stream.Partners import Partners

"""
* Start listening
"""
if __name__ == "__main__":
    port = 9000

    portOverride = None
    try:
        portOverride = sys.argv[1]
    except Exception:
        portOverride = None

    if portOverride is not None:
        port = portOverride

    application = tornado.web.Application([
        (r"/partner", Partners),
    ])
    print("Listening on port %s " % port)
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()