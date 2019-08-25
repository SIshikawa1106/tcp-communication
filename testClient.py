import tcp
import random

class ClientData(object):
    def __init__(self):
        self._data = ""
    def receive(self, data):

        print("input data = {}".format(data))

    def send(self):
        data = "TEST"
        print("make data = {}".format(data))
        return data

client_data = ClientData()
client = tcp.TcpClient("localhost", 999,
                       client_data.receive,
                       client_data.send,
                       send_first=True
                       )

client.daemon = True
client.start()

import time

time.sleep(1000)

