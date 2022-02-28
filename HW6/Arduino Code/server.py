try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import ujson
import secrets
import servoM
import time

import gc
gc.collect()
motor=servoM.Servo(15)

print("Updated")

try:
    ssid = secrets.SSID  
    password = secrets.PWD

except:
    print("secrets.py missing!! create a secrets.py and add SSID and PWD variables with correct credentials")

station = network.WLAN(network.STA_IF)


station.active(True)
station.connect("Tufts_Wireless")



while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

seq= []
startF=False
playF=False


def play():
    for i in seq:
        motor.move(i)
        time.sleep(1)


def doSomething(a):

    response={'ret':''}
    global startF
    global playF
    global seq


    if (a==b'Start' and startF == False):      
        startF=True
        playF=False
        seq=[]
        response['ret']="Start"
        print("Start")

    elif(a==b'Play' and playF==True):
        play()
        response['ret']="Play"
        print("Play")

    elif(startF==True):
        if(a==b'Stop'):
            startF=False
            playF=True
            response['ret']="Stop"
            print("Stop")

        elif(a==b'0'):
            
            seq.append(0)
            response['ret']="0"
            print(0)

        elif(a==b'45'):
            
            seq.append(45)
            response['ret']="45"
            print(45)
        
        elif(a==b'90'):
            
            seq.append(90)
            response['ret']="90"
            print(90)

        elif(a==b'135'):
            
            seq.append(135)
            response['ret']="135"
            print(135)
        
        elif(a==b'180'):
            
            seq.append(180)
            response['ret']="180"
            print(180)

        else:
            pass

    else:
        pass

    #except:
        #response['ret']="Error"
        
    return(ujson.dumps(response))





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',5050))
s.listen(5)

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP connection request from %s' % str(addr))
        request = conn.recv(1024) # receive the data
        conn.settimeout(None)
        body=request.split(b'\r\n')[-1] # parse the string to isolate the payload
        resp=doSomething(body)          # send the json string to do whatever you want
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Access-Control-Allow-Origin: *\n')
        conn.send('Access-Control-Allow-Credentials: true\n')
        conn.send('Application-Type: text/json\n')
        conn.send('Content-Type: text/json\n')
        conn.send('Connection: close\n\n')
        conn.send(resp)
        conn.close()

    except OSError as e:
        conn.close()
        print('Connection closed')