from __future__ import print_function
import socket
import threading

class Core(threading.Thread):

    MAX_LENGTH = 1024

    def __init__(self, host, port, receive_func, send_func, send_first=True, timeout=10):
        super(Core, self).__init__()
        self._host = host
        self._port = port

        self._exit_flag = False
        socket.setdefaulttimeout(timeout)
        self._receive_func = receive_func
        self._send_func = send_func
        self._send_first = send_first

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._target_socket = None
        self._connected = False

    def connect(self):
        pass

    def receice(self):

        tmp_data = ""
        all_data = ""
        while len(tmp_data)==0:
            tmp_data = self._target_socket.recv(self.MAX_LENGTH)
            if tmp_data == "":
                break
            all_data += tmp_data
            if len(tmp_data) == self.MAX_LENGTH:
                tmp_data = ""

        print("receive data = {}".format(all_data))
        self._receive_func(all_data)

    def send(self):
        data = self._send_func()
        print("send data = {}".format(data))
        ret = self._target_socket.sendall(data)

        assert ret != 0

    def is_connected(self):
        return self._connected

    def close(self):
        self._connected = False
        self._target_socket.close()

    def main_func(self):

        try:
            while not self._exit_flag:
                if self._send_first:
                    self.send()
                    self.receice()
                else:
                    self.receice()
                    self.send()
        finally:
            print("close")
            self.close()

    def run(self):
        while not self._exit_flag:

            try:
                if not self.is_connected():
                    print("connect...")
                    self.connect()

                if self.is_connected():
                    print("connected")
                    self.main_func()
            except socket.timeout, e:
                print(e)
            except socket.error, e:
                print(e)
            except KeyboardInterrupt:
                break
            except:
                import traceback
                traceback.print_exc()

        self._exit_flag = True

    def exit(self):
        self._exit_flag = True

class TcpServer(Core):
    def __init__(self, host, port, receive_func, send_func, send_first=True, timeout=10):
        super(TcpServer, self).__init__(
            host, port, receive_func, send_func, send_first, timeout
        )

        self._socket.bind((self._host, self._port))
        self._socket.listen(1)

    def connect(self):
        self.client_socket, self._client_address = self._socket.accept()
        self._target_socket = self.client_socket
        self._connected = True

    def close(self):
        self.client_socket.close()
        self._connected = False

class TcpClient(Core):
    def connect(self):
        self._target_socket = self._socket
        self._target_socket.connect((self._host, self._port))
        self._connected = True
