"""
PortScanner()  class object will allow us the capbility to perform a scan on that object.

The PortScanner class has a function scan() that takes a list of targets and ports as

input and performs a basic Nmap scan. Additionally ,we can now index the object by

target hosts and ports and print the status of the port . 

"""

import nmap
import optparse

def main():

    parser = optparse.OptionParser('usage%prog ' + \
            '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string',\
            help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',\
            help='specify target ports[s] seperated by comma')
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost

    tgtPorts = str(options.tgtPort).split(', ')

    if (tgtHost == None ) | (tgtPort[0] == None):
        print parser.usage
        exit(0)


def nmapScan(tgtHost, tgtPort):

    nmScan = nmap.PortScanner()

    nmScan(tgtHost, tgtPort)

    state = nmScan[tgHost]['tcp'][int(tgtPort)]['state']

    print "[*] " tgtHost + "tcp/"+tgtPort + " " + state
if __name__ == '__main__':
    main()
    
