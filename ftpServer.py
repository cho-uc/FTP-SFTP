import time
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import threading

class FtpThread(threading.Thread):

    def run(self):
        logging.basicConfig(level=logging.ERROR)
        
        authorizer = DummyAuthorizer()
		authorizer.add_user('someUser', 'somePassword', 'test_data', perm='elradfmwMT') # add more permission to R/W
        handler = FTPHandler
        handler.authorizer = authorizer

        address = ('', 2121)
        self.server = FTPServer(address, handler)
        self.server.serve_forever(timeout=1)
        

    def stop(self):
        self.server.close_all()


class RunWithFtp:
    def __init__(self):
        self.ftp_server = FtpThread()

    def __enter__(self):
        self.ftp_server.start()
        #time.sleep(1)
        return self

    def __exit__(self, *args):
        self.ftp_server.stop()

if __name__ == "__main__":
    print("Running FTP server")
    with RunWithFtp() as serve:
        time.sleep(10000) # run server for 10000s

