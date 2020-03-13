import serial
import math
import utm
import time
import threading
ser = serial.Serial('COM4',9600)
ser1 = serial.Serial('COM6',9600)
from dronekit import connect
def angle(pointA, pointB):

    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)


    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    #compass_bearing = initial_bearing

    return initial_bearing

def pitch(p):
    ser1.write(str(p).encode())

def yaw(y):
    ser.write(str(y).encode())
print('enter start point:')
a,b = input().split()
a = float(a)
b = float(b)
u0 = utm.from_latlon(a,b)
latt1 = u0[0]
lonn1 = u0[1]
pA = (a,b)
k = 0
t3 = 0
h2 = 0
latitude = 0
longitude =0
altitude = 0

vehicle = connect('127.0.0.1:14550', wait_ready=True)    
while True:
    mode = vehicle.mode.name
    latitude = vehicle.location._lat
    longitude = vehicle.location._lon
    altitude = vehicle.location._alt
    if k == 0:
        c =latitude
        d = longitude
        
        u1 = utm.from_latlon(c,d)
        latt2 = u1[0]
        lonn2 = u1[1]
        pB = (c,d)
        a1 = angle(pA,pB)
        
        t6 = a1
        
        print('yaw angle:',a1)
        time.sleep(1.5)
        
        t3 = a1
        
        d = math.sqrt((latt2-latt1)**2+(lonn2-lonn1)**2)
        h = altitude
        t7 = math.asin(h/math.sqrt(h**2+d**2))
        t7 = math.degrees(t7)
        h = t7
        t1 = threading.Thread(target=yaw,args=(-t6,))
        print('threading starts')
        t1.start()
        t1.join()
        t2 = threading.Thread(target=pitch,args=(t7,))
        print('Pitch starts')
        t2.start()
        t2.join()
       
        print("#############Done in loop 1####################")
        
        k = k+1
        
        time.sleep(0.5) 
    else:
        c =latitude
        d = longitude
        u1 = utm.from_latlon(c,d)
        latt2 = u1[0]
        lonn2 = u1[1]
        pB = (c,d)
        a1 = angle(pA,pB)
        t6 = a1
        

        
        print('Yaw angle:',t6)    
        d = math.sqrt((latt2-latt1)**2+(lonn2-lonn1)**2)
        h = altitude
        t7 = math.asin(h/math.sqrt(h**2+d**2))
        t7 = math.degrees(t7)
        #print('t7:',t7)
        t8 = h-t7
        if t8 <=10:
            t8 = t7-10
        h = t7   
        
        
        t1 = threading.Thread(target=yaw,args=(-t6,))
        t1.start()
        t1.join()
        #time.sleep(2)
        t2 = threading.Thread(target=pitch,args=(t7,))
        t2.start()
        t2.join()
        
        time.sleep(2)
