import array
import servoM

s1=servoM.Servo(15) #15 is probaby D3
s1.move(90)

k = 1

rock = 0
paper = 90
scissors = 180

# returns the value rock, paper or scisors based on a
def ready(r_training, p_training, s_training, val):
  
    # initialize arrays
  
    r_man_dist = [ None for x in r_training ]
    p_man_dist = [ None for x in p_training ]
    s_man_dist = [ None for x in s_training ]
    
    r_weighted = [ None for x in range(k) ]
    p_weighted = [ None for x in range(k) ]
    s_weighted = [ None for x in range(k) ]    
    
    
    # Determine Distance from value for each Datapoint
    
    for i in range(len(r_training)):
        r_man_dist[i] = abs(val - r_training[i])
        
    for i in range(len(p_training)):
        p_man_dist[i] = abs(val - p_training[i])
    
    for i in range(len(s_training)):
        s_man_dist[i] = abs(val - s_training[i])
    
    
    # Sorting weighted arrays
    
    r_man_dist.sort(reverse=True)
    p_man_dist.sort(reverse=True)
    s_man_dist.sort(reverse=True)
    
    
    # Weighting & Summing Weighted Scores
    
    r_weighted_sum = 0
    p_weighted_sum = 0
    s_weighted_sum = 0
    
    for i in range(len(r_weighted)):
        r_weighted[i] = r_man_dist[i] * ( (k-i) / k )
        r_weighted_sum = r_weighted_sum + r_weighted[i]
        
    for i in range(len(p_weighted)):
        p_weighted[i] = p_man_dist[i] * ( (k-i) / k )
        p_weighted_sum = p_weighted_sum + p_weighted[i]
        
    for i in range(len(s_weighted)):
        s_weighted[i] = s_man_dist[i] * ( (k-i) / k )
        s_weighted_sum = s_weighted_sum + s_weighted[i]
    
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
    
    else:
        print("*#")
        return 0
    

# Test Run w/ fake standard deviation data... should return scissors

v = 0

"""

rt = [2.3, 2.2, 1.9, 2.4, 2.2]
st = [1.4, 1.7, 2.8, 1.5, 1.4]
pt = [-2.2, -2.0, -2.4, -1.9, -2.0]

ready(rt, pt, st, v)

"""

# Test run w/ data file
    
r = []
p = []
s = []

file = open('testData.csv', 'r')
line = file.readline()
print
while line:
    words = line.split(',')
    value = words[0]
    category = (words[1])[0]
    line = file.readline()
    
    if category == str(0):
        r.append(float(value))
    elif category == str(1):
        p.append(float(value))
    elif category == str(2):
        s.append(float(value))
        
file.close()

ready(r, p, s, v)


    
        
    