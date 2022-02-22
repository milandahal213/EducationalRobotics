import time
from math import  sqrt
from lsm6dsox import LSM6DSOX
from machine import Pin, I2C
import gc
import RGB
k = 3
rock = 0
paper = 90
scissors = 180
blank = 0

# Test run w/ data file

r = []
p = []
s = []
b = []

file = open('testData.csv', 'r')
line = file.readline()

while line:
    words = line.split(',')
    value = words[0]
    category = (words[1])[0]
    line = file.readline()
    print(category)
    if category == str(0):
        r.append(float(value))
    elif category == str(1):
        p.append(float(value))
    elif category == str(2):
        s.append(float(value))
    elif category == str(4):
        b.append(float(value))
        
file.close()
# initialize arrays

r_man_dist = [ None for x in r ]
p_man_dist = [ None for x in p ]
s_man_dist = [ None for x in s ]
b_man_dist = [ None for x in b ]

r_weighted = [ None for x in range(k) ]
p_weighted = [ None for x in range(k) ]
s_weighted = [ None for x in range(k) ]
b_weighted = [ None for x in range(k) ] 




# returns the value rock, paper or scisors based on a
def decide(val):

        # Determine Distance from value for each Datapoint

    for i in range(len(r)):
        r_man_dist[i] = abs(val - r[i])
        
    for i in range(len(p)):
        p_man_dist[i] = abs(val - p[i])

    for i in range(len(s)):
        s_man_dist[i] = abs(val - s[i])
        
    for i in range(len(b)):
        b_man_dist[i] = abs(val - b[i])


    # Sorting weighted arrays

    r_man_dist.sort(reverse=True)
    p_man_dist.sort(reverse=True)
    s_man_dist.sort(reverse=True)
    b_man_dist.sort(reverse=True)
        

    # Weighting & Summing Weighted Scores
    
    r_weighted_sum = 0
    p_weighted_sum = 0
    s_weighted_sum = 0
    b_weighted_sum = 0
    
    for i in range(len(r_weighted)):
        r_weighted[i] = r_man_dist[i] * ( (k-i) / k )
        r_weighted_sum = r_weighted_sum + r_weighted[i]
        
    for i in range(len(p_weighted)):
        p_weighted[i] = p_man_dist[i] * ( (k-i) / k )
        p_weighted_sum = p_weighted_sum + p_weighted[i]
        
    for i in range(len(s_weighted)):
        s_weighted[i] = s_man_dist[i] * ( (k-i) / k )
        s_weighted_sum = s_weighted_sum + s_weighted[i]

    for i in range(len(b_weighted)):

        b_weighted[i] = b_man_dist[i] * ( (k-i) / k )
        b_weighted_sum = b_weighted_sum + b_weighted[i]

    
    # Decision
    
    decision = [r_weighted_sum, p_weighted_sum, s_weighted_sum]
    decision.sort()
    
    if(decision[0] == r_weighted_sum):
        print("*Rock#")
        print("est error = ")
        return rock
    
    elif(decision[0] == p_weighted_sum):
        print("*Paper#")
        print("est error = ")
        return paper
    
    elif(decision[0] == s_weighted_sum):
        print("*Scissors#")
        print("est error = ")
        return scissors
    
    elif(decision[0] == b_weighted_sum):
        print("*Blank#")
        print("est error = ")
        return blank
    
    else:
        print("something fucked up")
        return 0
    

# Test Run w/ fake standard deviation data... should return scissors

v = 0

"""

rt = [2.3, 2.2, 1.9, 2.4, 2.2]
st = [1.4, 1.7, 2.8, 1.5, 1.4]
pt = [-2.2, -2.0, -2.4, -1.9, -2.0]

decide(rt, pt, st, v)

"""



#decide(r, p, s, v) 
lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))

n = 100
playerData = [0]*n
targetTime = 1000
def read_accel():
    gc.collect()
    start = time.ticks_ms()
    while(lsm.read_accel()[2]>0.9):
        current = time.ticks_ms()
        if((current-start)>2000):
            break
        pass
    #global playerData
    
    for i in range(len(playerData)):
        accel = lsm.read_accel()
        zaccel = accel[2]
        #print(zaccel)
        playerData[i] = zaccel
        time.sleep_ms(targetTime//n)

    #end = time.ticks_ms()
    #print(end-start)
    #print("ool")
        
def find_std():

    mean = sum(playerData) / len(playerData)   # mean
    var  = sum(pow(x-mean,2) for x in playerData) / len(playerData)  # variance
    std  = sqrt(var)  # standard deviation
    print("*SD#", str(std),"&")
    #print('var: '+str(var))
    #print('std: '+str(std))
    return std

def ready():
    #print("Tap")
    RGB.GREEN(1)
    read_accel()
    playerChoice = find_std()
    #decide(playerChoice) 
    RGB.GREEN(0)
    gc.collect()

print("Ready")       
    