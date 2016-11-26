import serial
import Decryptie
import os

message=''
decrypted_message=()
ser=serial.Serial('/dev/rfcomm0')
ekgfile = os.open('ekgpipe', os.O_WRONLY)
pofile = os.open('popipe', os.O_WRONLY)

def dereform(string):
    """
    Maakt van de ontvangen vlakke string ('aaa.bbb.ccc. ... .zzz') opnieuw tupple van een lijst, een nummer en een lijst.
    """

    #herwerk de string tot een lijst van afzonderlijke waarden
    list = []
    check_new_point = 1
    index_last_point = -1
    while check_new_point < len(string):
        if string[check_new_point] == '.':
            list.append(int(string[index_last_point + 1:check_new_point]))
            index_last_point = check_new_point
        check_new_point += 1

    list.append(int(string[index_last_point+1:-1]))
    return list[:16], list[16], list[17:]

while True:
    data = str(ser.read(),'utf-8')
    if data == ':':
        #zorgt voor start met :
        while True:
            data = str(ser.read(),'utf-8')
            if data != ':':
                message += data
                
            else:
                decrypted_message = Decryptie.Ontcijfering(dereform(message)) 
                for i in range(0, 8):
                    print(str(decrypted_message[i]) + '\n')
                    os.write(ekgfile, str(decrypted_message[i]).encode('utf-8') + b'\n')

                for i in range(8, 12):
                    print(str(decrypted_message[i]) + '\n')
                    os.write(pofile, str(decrypted_message[i]).convert('utf-8') + b'\n')
