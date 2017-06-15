import tornado.websocket
import uuid
import json
import pprint

class Partners(tornado.websocket.WebSocketHandler):

    """
    * Defining constants for each connection
    """
    HANDSHAKE = "handshake"
    UUID = ""
    ID = ""

    clients = {}

    def check_origin(self, origin):
        print("On check origin")
        return True

    def open(self):
        print("Connection opened")
        msg = {}
        msg["type"] = self.HANDSHAKE
        msg["uuid"] = str(uuid.uuid1())

        """
        * Write to send uuid for connection
        """
        print("Write message")
        self.write_message(msg)

    def on_message(self, message):
        print("On message")
        print("The message: %s" % message)
        msg = None

        try:
            msg = json.loads(message)
        except Exception:
            print("The error: %s" % Exception.message)
            print("Close connection, can't load message")
            self.closeConnection(400)

        if msg is None:
            return

        self.dispatchMessage(msg)

    def on_close(self):
        pprint.pprint(self.clients)
        print("Connection closed")
        del self.clients[self.UUID]
        pprint.pprint(self.clients)

    def closeConnection(self, reason):
        print("Closing connection by reason")
        self.clients.pop(self.UUID)
        self.close(reason)

    def dispatchMessage(self, json):
        print("DispachMessage")
        if json["type"] == self.HANDSHAKE:
            print("Type handshake")
            if "id" not in json:
                print("Id not in json")
                self.closeConnection(400)
                return

            self.UUID = json["uuid"]
            self.ID = json["id"]
            self.clients[self.UUID] = self
            pprint.pprint(self.clients)

            print("To see is this is working")
            print(self.clients[self.UUID].ID)

        else:
            self.closeConnection(400)