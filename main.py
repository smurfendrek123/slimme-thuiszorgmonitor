## IMPORTS ##
import pyb


## CONSTANTEN ##
FREQ = 128              #frequentie waaraan gemeten wordt
LENGTH_ELEMENT = 12     #constanten voor omzetten naar binair
LENGTH_MESSAGE = 128    #lengte totale boodschap voor aes encryptie


## PIN-NUMMERS ##
PO_PIN_NB = 'X19'           #nummer van de pulse-oximeter pin
ECG_PIN_NB = 'X20'          #nummer van de electrocardiogram pin
PRESSURE_PIN_NB = 'X21'     #nummer van de druksensor pin
PIN_RED_LED_NB = 'X9'       #X9: Naam pin
PIN_INFRARED_LED_NB = 'X10' #X10: Naam pin


## PINNEN AANMAKEN ##
po_pin = pyb.ADC(PO_PIN_NB)
ecg_pin = pyb.ADC(ECG_PIN_NB)
pressure_pin = pyb.ADC(PRESSURE_PIN_NB)
##pin_red_led = pyb.Pin(PIN_RED_LED_NB, Pin.OUT_PP)           # deze code werkt nog niet, pins moeten ook aangepast worden
##pin_infrared_led = pyb.Pin(PIN_INFRARED_LED_NB, Pin.OUT_PP) # deze code werkt nog niet


## INITIALISEREN ##
current_led = pyb.LED(2)    # deze moeten vervangen worden door pin_red_led en pin_infrared_led
next_led = pyb.LED(3)       # voor het testen worden de LED's op het bordje gebruikt


## FUNCTIES ##
def reform_list(list):
    # returns a message from a list in binary that is 128 characters long
    for i in range(len(list)):
        list[i] = bin(list[i])[2:]
    for i in range(len(list)):
        if len(list[i]) < LENGTH_ELEMENT:
            list[i] = (LENGTH_ELEMENT-len(list[i]))*'0' + list[i]
    message = ''
    for i in list:
        message += i
    if len(message) < LENGTH_MESSAGE:
        message += (LENGTH_MESSAGE-len(message))*'0'
    return message


def read_and_send():
    # read the values of the sensor pins, switch the LEDs, encrypt the message, send the message via Bluetooth
    value_ecg = ecg_pin.read()
    value_po = po_pin.read()
    value_pressure = pressure_pin.read()
    switch_leds() 

    list = [value_ecg, value_po, value_pressure]
    
    message = reform_list(list)
    print(message)
    
    #ENCRYPTIE: encrypted_message = encrypt(message)
    #BLUETOOTH: send(encrypted_message)


def switch_leds():
    global current_led
    global next_led
    current_led, next_led = next_led, current_led

"""
def encrypt(message):
    pass

def send(encrypted_message):
    pass
"""


    



## TEST CODE ##

read_and_send()

print('alles werkt')
for i in range(10):
    pyb.LED(4).toggle()
    pyb.LED(1).toggle()
    delay(150)