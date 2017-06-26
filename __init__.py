import sys
import tornado.web
import tornado.ioloop
import json
from stream.Partners import Partners
import ConfigParser

"""
* Start listening
"""
if __name__ == "__main__":
    port = 9000

    """
    Loading app config stored at config ini file.
    """
    config = ConfigParser.ConfigParser()
    config.read("config/config.ini")
    configOptions = config.options("app")

    if "port" in configOptions:
        portOverride = config.get("app", "port")

    if portOverride is not None:
        port = portOverride

    application = tornado.web.Application([
        (r"/partner", Partners),
    ])
    print("Listening on port %s " % port)
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()