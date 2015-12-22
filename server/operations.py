from subprocess import call
import magic
import os
import Mp3Valid

files = []
for (path, dirnames, filenames) in os.walk('flow'):
    files.extend(os.path.join( name) for name in filenames)




def makeOperations():
    call(["tcpflow", "-r","pcap_r.cap","-o","flow/"])
    m=magic.open(magic.MAGIC_NONE)
    m.load()
    for i in files:
        # print m.file('flow/'+i)
        # print isMp3Valid('flow/'+i)
        if "MPEG" in m.file('flow/'+i):
            os.rename('flow/'+i,'sample.mp3')
        if Mp3Valid.isMp3Valid('flow/'+i) is True:
             os.rename('flow/'+i,'sample.mp3')
        else:
            return "Nie można odczytać danych ze streamu"

