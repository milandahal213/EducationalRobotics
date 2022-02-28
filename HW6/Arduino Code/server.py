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



try:
    ssid = secrets.SSID  
    password = secrets.PWD

except:
    print("secrets.py missing!! create a secrets.py and add SSID and PWD variables with correct credentials")

station = network.WLAN(network.STA_IF)

station.active(True)
if (password==""):
    station.connect("Tufts_Wireless")
else:
    station.connect(ssid, password)

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


def do(req):
    global startF
    global playF
    global seq
    print(type(req))
    a=str(ujson.loads(req)) #Start, Stop , Ignore, o,45, 90,135, 180, Play
    try:
        if (a=="Start" and startF == False): 
            print("Start")
            startF=True
            playF=False
            seq=[]

        elif(a=="Play" and playF==True):
            print("Play")
            play()
        elif(startF==True):
            print("Start is now False")
            if(a=="Stop"):
                print("Stop")
                startF=False
                playF=True

            elif(a=="0"):
                print(0)
                seq.append(0)

            elif(a=="45"):
                print(45)
                seq.append(45)
            
            elif(a=="90"):
                print(90)
                seq.append(90)

            elif(a=="135"):
                print(135)
                seq.append(135)
            
            elif(a=="180"):
                print(180)
                seq.append(180)

            else:
                pass
        else:
        pass

    except:
        return("Error")





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
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.send(resp)
        conn.close()

    except OSError as e:
        conn.close()
        print('Connection closed')