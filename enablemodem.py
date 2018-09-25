import threading
import time
import Queue
import subprocess
import sys, getopt
#import Adafruit_BBIO.UART as UART
#import Adafruit_BBIO.GPIO as GPIO
from enablehardware import modem_init



def auto_pon(provider):
    #provider = 'verizon'
    
    print 'pon ' + provider + ':'
    
    proc = subprocess.Popen(['pon', provider] , stdout=subprocess.PIPE)
    
    response = proc.communicate()
    
    print "Results:"
    print response[0]
    
    
def auto_poff():
    
    provider = 'verizon'
    
    print 'poff ' + provider + ':'
    
    proc = subprocess.Popen(['poff', provider] , stdout=subprocess.PIPE)
    
    response = proc.communicate()
    
    print "Results:"
    print response[0]


def main(argv):
   

    runas = 'kore'
    try:
        opts, args = getopt.getopt(argv,"hp:",["provider="])
    except getopt.GetoptError:
        print 'enablemodempy -p <kore>|<verizon>|<att>'
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print 'main.py.py -p <kore>|<verizon>|<att>'
            sys.exit()
        elif opt in ("-p", "--provider"):
            print "Starting thread main..."
            provider = arg.strip()
            
            modem_init()
            time.sleep(5)
            auto_pon(provider)
            
            while True:
                time.sleep(.005)
            
            print 'Exiting App...'
            exit()
        else:
            print 'Invalid provider parameter'
            
               
if __name__ == '__main__':
    
    main(sys.argv[1:])
    
    '''
    modem_init()

    time.sleep(5)
    auto_pon()
    
    while True:
        time.sleep(.005)
    
    consoleThread = CpConsole()
    consoleThread.start()
    
    while(consoleThread.isAlive()):
        time.sleep(.005)

    print 'Exiting App...'
    exit()
    '''
 
