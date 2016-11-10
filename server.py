# https://github.com/dpallot/simple-websocket-server
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class ForceWebSocketServer(WebSocket):
    def handleMessage(self):
        #echo
        self.sendMessage(self.data)

    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'

if __name__ == '__main__':
    server = SimpleWebSocketServer('', 8000, ForceWebSocketServer)
    server.serveforever()