from __future__ import absolute_import


import sys, time, socket, threading

from .daemon import Daemon
from .hal import Hal


class ServerHal(Hal):
    """
    Server interface to hal
    """
    def __init__(self, configpath):
        super(ServerHal, self).__init__(configpath)

    def say_all(self):
        response = "\n".join(self.all_says)
        return response


class HalDaemon(Daemon):

    def __init__(self, pidfile):
        super(HalDaemon, self).__init__(pidfile)
        self.hal = ServerHal()

    def run(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind(('localhost', 3423))
        serversocket.listen(5)
        while True:
            (client, address) = serversocket.accept()
            client.settimeout(60)
            threading.Thread(target = self.listen_to_client, args = (client, address)).start()

    def listen_to_client(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size).decode()
                if data:
                    # Set the response to echo back the recieved data
                    response = self.hal.process(data)
                    client.send(response.encode())
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False


def main():
    daemon = HalDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'test' == sys.argv[1]:
            daemon.test()
        else:
            print("Unknown command")
            return 2
        return 0
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        return 2

if __name__ == "__main__":
    sys.exit(main())
