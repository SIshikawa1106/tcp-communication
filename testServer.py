import tcp
import random

class ServerData(object):
    def __init__(self):
        self._data = ""
    def receive(self, data):

        print("input data = {}".format(data))

        self._data = data

    def send(self):
        data = self._data + "{}".format(random.randint(0, 10))
        print("make data = {}".format(data))
        return data


server_data = ServerData()
server = tcp.TcpServer("localhost", 999,
                       server_data.receive,
                       server_data.send,
                       send_first=False
                       )

server.daemon = True
server.start()

import time

time.sleep(100)
server.exit()