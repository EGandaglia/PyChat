import socket
import threading
import time

PORT = 7777

class Server(threading.Thread):
    def __init__(self, port, host='localhost'):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.sockserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        # Method representing the thread s activity.
        self.sockserver.bind((self.host,self.port))
        self.sockserver.listen(5)
        print "Waiting for connection on port %s" % (self.port)
        conn, addr = self.sockserver.accept()
        print "Successfully connected with " + str(addr) + " using socket " + str(conn)
        data = conn.recv(1024)
        reply = 'OK...' + data
        print reply
        conn.close()
        self.sockserver.close()


class Client(threading.Thread):
    def __init__(self, port, host='localhost'):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.sockclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.sockclient.connect((self.host,self.port))
        self.sockclient.send("HELLO SOCKET!")

if __name__ == '__main__':
    
    server = Server(port=PORT)
    server.start()

    client = Client(port=PORT)
    client.start()

# host = socket.gethostbyname(socket.gethostname())
