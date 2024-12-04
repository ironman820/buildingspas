from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):
    def connect(self):
        """Event when client connects"""

        self.accept()
        self.send(text_data="You are connected by Websockets!")

    def disconnect(self, close_code):
        """Event when client disconnects"""
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass
