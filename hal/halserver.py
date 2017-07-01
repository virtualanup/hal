#!/usr/bin/env python

import sys, time, socket, threading
from .daemon import Daemon
from .hal import Hal


class DummyHal(Hal):
    def __init__(self, configpath):
        super(DummyHal, self).__init__(configpath)

    def say_all(self):
        pass

    def display_help(self, help_content):
        pass

class HalDaemon(Daemon):

    def __init__(self, pidfile, configpath):
        super(HalDaemon, self).__init__(pidfile)
        self.hal = DummyHal(configpath)

    def process_data(self, data):
        return ">" + self.hal.process(data.decode())

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
                    response = self.process_data(data)
                    client.send(response.encode())
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

def main():
    daemon = HalDaemon('/tmp/hal-daemon.pid', '~/')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: halserver start | stop | restart")
        sys.exit(2)

if __name__ == "__main__":
    sys.exit(main())
