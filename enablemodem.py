import threading
import time
import Queue
import subprocess
import sys, getopt
#import Adafruit_BBIO.UART as UART
#import Adafruit_BBIO.GPIO as GPIO
import wiringpi as GPIO



class CpGpioMap():
    GPIO_CELLENABLE = 17
    GPIO_CELLRESET = 6
    GPIO_CELLONOFF = 5
    GPIO_CELLPWRMON = 26
    GPIO_LED1 = 23
    GPIO_LED2 = 24

            

# !!! This method must be called before creating the modem object !!!
def modem_init():

    print 'Initializing GPIO(s)'
    GPIO.pinMode(CpGpioMap.GPIO_CELLENABLE, GPIO.OUTPUT) #CELL_ENABLE
    GPIO.pinMode(CpGpioMap.GPIO_CELLRESET, GPIO.OUTPUT) #CELL_RESET
    GPIO.pinMode(CpGpioMap.GPIO_CELLONOFF, GPIO.OUTPUT) #CELL_ONOFF
    GPIO.pinMode(CpGpioMap.GPIO_CELLPWRMON, GPIO.INPUT) #CELL_PWRMON
    
    GPIO.digitalWrite(CpGpioMap.GPIO_CELLENABLE, GPIO.GPIO.LOW)
    GPIO.digitalWrite(CpGpioMap.GPIO_CELLRESET, GPIO.GPIO.LOW)
    GPIO.digitalWrite(CpGpioMap.GPIO_CELLONOFF, GPIO.GPIO.LOW)
    
    print 'Initializing Modem...'
    #while True:
    #    time.sleep(3)
    #    if not GPIO.digitalRead(CpGpioMap.GPIO_CELLPWRMON):
    #        print "GPIO_CELLPWRMON=LOW"
    #        break
    #    else:
    #        GPIO.digitalWrite(CpGpioMap.GPIO_CELLENABLE, GPIO.GPIO.HIGH)
    #        time.sleep(.01) # 10ms
    #        GPIO.digitalWrite(CpGpioMap.GPIO_CELLENABLE, GPIO.GPIO.LOW)
            
    while True:
        print "TOGGLE GPIO_CELLONOFF:HIGH wait 3 sec."
        GPIO.digitalWrite(CpGpioMap.GPIO_CELLONOFF, GPIO.GPIO.HIGH)
        time.sleep(3)
        print "TOGGLE GPIO_CELLONOFF:LOW wait 2 sec."
        GPIO.digitalWrite(CpGpioMap.GPIO_CELLONOFF, GPIO.GPIO.LOW)
        time.sleep(2)
        if GPIO.digitalRead(CpGpioMap.GPIO_CELLPWRMON):
            print "GPIO_CELLPWRMON=HIGH"
            break

   # print 'Setting up UART1...'
   # UART.setup("UART1")
   # print 'Setting up UART2...'
   # UART.setup("UART2")
   # print 'Setting up UART4...'
   # UART.setup("UART4")
    
    print 'Modem Initialized' 

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
   

    GPIO.wiringPiSetupGpio()

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
 
