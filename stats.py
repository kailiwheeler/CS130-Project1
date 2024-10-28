#stats.pi
import matplotlib.pyplot as plt
import pytest

try:
  fhand=open('StudentExercise.csv')
except:
  print('File cannot be opened')
  exit()

next(fhand)   #skips the header in the data file

hours = []

for line in fhand: 
  pieces=line.split(',')
  if(pieces[0] != ""):
      hours.append(float(pieces[0]))

hours.sort()
n_bins = 10
fig, ax = plt.subplots()
ax.hist(hours,bins=n_bins)
ax.set(xlabel="hours",title="hours of exercise")
#plt.show()




def average(array):
    length = len(array)
    total = 0.0
    for hour in array:
        total = total + hour
    return round(total/length,2)

def prop_above(array):
    av = average(array)
    count = 0
    total = 0
    for hours in array:
        total += 1
        if(hours > av):
            count += 1
    return round(count/total*100,2)

def median(array):
    length = int(len(array))
    if(length%2 == 0):
        return round((array[round(length/2)] + array[(round(length/2))-1])/2,2)
    else:
        return round(array[round(length/2)],2)

print("average hours:",average(hours))
print(f"percent above the average: {prop_above(hours)}%")
print("median hours:",median(hours))

#the average was higher than the median by about 1 hour, this means that there is most likely a couple really high numbers in the data
#this is also show in the histogram plot, graph skewed left   
    
