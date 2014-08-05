import threading
import time
import Queue
import subprocess
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO


#PPP_ROUTE = 'appserver05.cphandheld.com'
PPP_ROUTE = '23.253.112.132'

class CpGpioMap():
    GPIO_CELLENABLE = "P9_12"
    GPIO_CELLRESET = "P9_23"
    GPIO_CELLONOFF = "P8_12"
    GPIO_CELLPWRMON = "P9_42"
    
class CpConsole(threading.Thread):
    
    def __init__(self, *args):
        self._target = self.console_handler
        self._args = args
        self.__lock = threading.Lock()
        self.closing = False # A flag to indicate thread shutdown
        threading.Thread.__init__(self)
        
    def run(self):
        self._target(*self._args)
    
    def comm_callback_handler(self, result):
        print "comm_callback_handler ", result
        
    def shutdown_thread(self):
        print 'shutting down CpConsole...'
        self.__lock.acquire()
        self.closing = True
        self.__lock.release()
        
    def console_handler(self):
        
        input=1
        while not self.closing:
            # get keyboard input
            input = raw_input(">> ")
                # Python 3 users
                # input = input(">> ")
            if input == 'exit' or input == 'EXIT':
                self.shutdown_thread()
            elif input == 'pon' or input == 'PON':
                auto_pon()
            elif input == 'poff' or input == 'POFF':
                auto_poff()
                
            
                
            time.sleep(.005)
            

# !!! This method must be called before creating the modem object !!!
def modem_init():

    print 'Setting up UART1...'
    UART.setup("UART1")
    print 'Setting up UART2...'
    UART.setup("UART2")
    print 'Setting up UART4...'
    UART.setup("UART4")
    
    print 'Initializing GPIO(s)'
    GPIO.setup(CpGpioMap.GPIO_CELLENABLE, GPIO.OUT) #CELL_ENABLE
    GPIO.setup(CpGpioMap.GPIO_CELLRESET, GPIO.OUT) #CELL_RESET
    GPIO.setup(CpGpioMap.GPIO_CELLONOFF, GPIO.OUT) #CELL_ONOFF
    GPIO.setup(CpGpioMap.GPIO_CELLPWRMON, GPIO.IN) #CELL_PWRMON
    
    GPIO.output(CpGpioMap.GPIO_CELLENABLE, GPIO.LOW)
    GPIO.output(CpGpioMap.GPIO_CELLRESET, GPIO.LOW)
    GPIO.output(CpGpioMap.GPIO_CELLONOFF, GPIO.LOW)
    
    while True:
        if GPIO.input(CpGpioMap.GPIO_CELLPWRMON):
            print "GPIO_CELLPWRMON=LOW"
            break
        else:
            GPIO.output(CpGpioMap.GPIO_CELLENABLE, GPIO.HIGH)
            time.sleep(.01) # 10ms
            GPIO.output(CpGpioMap.GPIO_CELLENABLE, GPIO.LOW)
            time.sleep(.002) # 2ms
            
    while True:
        print "TOGGLE GPIO_CELLONOFF:HIGH wait 3 sec."
        GPIO.output(CpGpioMap.GPIO_CELLONOFF, GPIO.HIGH)
        time.sleep(3)
        print "TOGGLE GPIO_CELLONOFF:LOW wait 2 sec."
        GPIO.output(CpGpioMap.GPIO_CELLONOFF, GPIO.LOW)
        time.sleep(2)
        if GPIO.input(CpGpioMap.GPIO_CELLPWRMON):
            print "GPIO_CELLPWRMON=HIGH"
            break
        
    print 'Modem Initialized' 

def auto_pon():
    

    provider = 'verizon'
    
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
    
def route_add():
    
    ### Static route with route add
    # route add -host PPP_ROUTE dev ppp0
    
    
    print "Adding static route: " + PPP_ROUTE

    proc = subprocess.Popen(['route', 'add', '-host', PPP_ROUTE, 'dev', 'ppp0'],stdout=subprocess.PIPE)
    
    #print "Process Id: %d" % proc.pid       
        
if __name__ == '__main__':
    
    
    modem_init()
    #route_add()
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