"""
    --- Part 1 ---
In out first step we accept the hostname and port from the user . For this ,our 
program usilizes the optparse library for parsing command-line options.
"""


import optparse
from socket import *

parser = optparse.OptionParser('usage %prog -H <target host> -p  <target port>')

# We are using -H for target host and -p flag for target port so when the program
# runs it will look like this python program_name.py -H <target host> -p <target port>


parser.add_option('-H', dest='tgtHost', type='string',\
        help='specify target host')

parser.add_option('-p' , dest='tgtPort', type='int', \
        help='specify target port')

(options, args) = parser.parse_args()

tgtHost = options.tgtHost

tgtPort = options.tgtPort

if (tgtHost == None) | (tgtPort == None):
    print parser.usage
    exit(0)


"""
    									--- Part 3 ---
Next, we will build two functions connScan and portScan . The portScan function takes the hostname and
target ports as arguments.It will first attemp to resolve an IP address to a friendly hostname using 
the gethostbynme() function.

Next , it will print the hostname (or IP address) and enumerate through each individual port attempting
 to connect using the connScan function

The connScan function will take two arguments: tgtHost and tgtPort and attempt to create a connection to 
the target host and port. It it is successfull,connScan will print and open port message. If unsuccessful, 
it will print the closed port message.
"""

from socket import *

def connScan(tgtHost, tgtPort):

    try:
        connSkt = socket(AF_INET, SOCK_STREAM)

        connSkt.connect((tgtHost, tgtPort))

        connSkt.send('Violent Python\r\n')   # part 3 additional line
        results = connSkt.recv(100)          # part 3 additonal line


        print '[+] %d/tcp open' % tgtPort
        print '[+] ' + str(results)          # part 3 addtional line

        connSkt.close()
    except:
        print '[-]%d/tcp closed' % tgtPort

def portScan(tgtHost, tgtPorts):
    try:

        tgtIP = gethostbyname(tgtHost)
    except:

        print "[-] Cannot resolve '%s' : Unknown host " %tgtHost

        return

    try:

        tgtName = gethostbyaddr(tgtIP)

        print '\n[+] Scan Results for : ' + tgtName[0]

    except:
        print '\n[+] Scan Results for: ' + tgtIP

    setdefualttimeout(1)

    for tgtPort in tgtPorts:

        print 'Scanning port ' + tgtPort

        connScan(tgtHost, int(tgtPort))

"""
    --- Part 3 ---
Applicatoin Banner Grabbing
In order to grab the application banner from out target host, we must insert additional code into the
connScan function.

After discovering an open port, we send a string of data to the port and wait for the response. 
Gathering this response might give us an indication of the application running on the target host 
and port.

For this additional method I am writting code in the comment and add later to the final program


					connSkt.send('Violent Python\r\n')

					results = connSkt.recv(100)

					print '[+] ' + str(results)

"""

# final main function 

def main():

    parser = optparse.OptionParser("usage%prog  -H <target host> -p <target port>")

    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')

    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] seperated by comma')

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost

    tgtPorts = str(options.tgtPort).split(', ')

    if (tgtHost == None) | (tgtPorts[0] == None):    
        print '[-] You must specify a target host and port[s].'
        exit(0)
    portScan(tgtHost, tgtPorts)



"""
    --- Part 5 ---
Threading the Scan

1.  Depending on the timeout variavble for a socket, a scan of each socket can take several seconds.
    While this appears trivial . it quickly adds up it we are scanning multiple hosts or ports.
    It will take lots of time if we do this normally.
2. Thats why we are gonna use Python Threading. Threading provides a way to perform these kinds of 
    executions simultaneously. 
3.  To utilize this in our scan , we will modily the iteration loop in out portScan() function

for tgtPort in tgtPorts:

    t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))

    t.start()

4.  While this provides us with a significant advantage in speed , it does present one disadvantage.
    Out function connScan() prints an output to the screen.
    If multiple threads print an output at the same time , it could appear garbled and out of order

5. In order to allow a function a function to have complete control of the screen, we will use a semaphore.
    A simple semaphore provides us alock to prevent other threads from proceeding. Notice that prior to printing
    an output,  we grabbed a hold of the lock using screenLock.acquire(). If open, the semaphore will grant us
    access to preceed and we will print to the screen. If locked we'll have to wait untill the thread holding 
    the semaphore releases the lock.

    screenLock = Semaphore(value=1)

    def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.send('Violent Python\r\n')
        results = connSkt.recv(100)

        screenLock.acquire()

        print '[+] %dtcp open' % tgtPort
        print '[+] ' + str(results)

    except:
        screenLock.acquire()

        print '[-]%d/tcp closed' % tgtPort
    finally:
        screenLock.release()
        connSkt.close()

"""

if __name__ == '__main__':
    main()
