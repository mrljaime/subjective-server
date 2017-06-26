import json
from tornado.escape import json_decode
from tornado.escape import json_encode

"""
Class that handle and stored message at database and message queue
"""

class PartnerMessage:
    clients = {}
    msg = None

    def __init__(self, clients, msg):
        self.clients = clients
        self.msg = json_decode(msg)

    def handle(self):
        """
        Connect it with message queue
        """

        try:
            print(self.msg)
            self.clients[self.msg["to"]].write_message(self.msg["msg"])
        except ValueError:
            print("There's an error: %s" % ValueError.message)
