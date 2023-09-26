from datetime import datetime
import os
import platform
import socket


class Usage:
    def __init__(self) -> None:
        pass

    def get_ip(self):
        return [socket.gethostname(), socket.gethostbyname(socket.gethostname())]
    
    def get_os(self):
        return platform.system()

    def get_time(self):
        return datetime.now()

    def get_all_info(self):
        return [
            self.get_ip(),
            self.get_os(),
            self.get_time()]


if __name__ == "__main__":
    a = Usage()
    for i in (a.get_all_info()):
        print(str(i) + "\n\n")
