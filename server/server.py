# -*- coding: utf-8 -*-
from socket import *
import thread
import operations
import RecognizeSong
import Lyric


BUFF = 1024
HOST = ''# must be input parameter @TODO
PORT = 5110 # must be input parameter @TODO
dataFile=""

def printData(data):
    print repr(data)

def handler(clientsock,addr):
    with open('pcap_r.cap', 'wb') as file_to_write:
      while True:
        data = clientsock.recv(128)
        if not data:
              break
        file_to_write.write(data)
    clientsock.send("File saved on server")
    operations.makeOperations()
    clientsock.send("File send to recognize")
    RecognizeSong.recognizeThis()
    clientsock.send("Downloading subtitle in progress..")
    artist=RecognizeSong.recognizeThis()[0]
    title=RecognizeSong.recognizeThis()[1]
    output =Lyric.FindLyric(artist,title)
    clientsock.send(output)
    clientsock.close()
    print addr, "- closed connection" #log on console



if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print 'waiting for connection... listening on port', PORT
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))