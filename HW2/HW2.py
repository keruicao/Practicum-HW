# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:02:32 2020

@author: Harry
"""
import re
import time
import matplotlib.pyplot as plt
import argparse

# Set the command input environment

# Set the input frame
inp = argparse.ArgumentParser()

# Set input parameters
inp.add_argument("-in", "--file",help="which file to process")
inp.add_argument("-oplot", "--plot",help="where to save the plot")

# Creat a input object
i = inp.parse_args()

# Below is actually not necessary
if __name__=='__main__':
    file = i.file
    plot = i.plot
    

start = time.perf_counter()

# set counter for lines
a = 0

# set list to record GPU cores
gpu = []

# Open the file
with open(file,'r',encoding='latin1') as f:
    # read line by line to resuce the usage of memory
    for lines in f:
        # count how many lines are read
        a += 1
        
        # extract number of CPU cores
        c = re.findall(pattern="-pe\somp\s(.*?)\s",string=lines)
        # if CPU cores is provided, convert it into float
        if c:
            c = float(c[0])
        # if no CPU cores found here, it is default number, which is 1
        else:
            c = 1
        # extract number of GPU cores
        g = re.findall(pattern="-l\sgpus=(.*?),",string=lines)
        # if GPU cores is provided, multiply by number of CPU cores to 
        # obtain the number of GPU cores
        if g:
            g = round(float(g[0])*c)
            gpu.append(g)
#             gpu.append([c,float(g[0])])
            
end = time.perf_counter()

per = (len(gpu)/a) * 100
mea = sum(gpu)/len(gpu)
ti = end - start

print("jobs with GPU:{}%".format(per))
print("avg number of cores used with GPU:{}".format(mea))
print("time to process the file: {} seconds".format(ti))

# Creat plot frame
fig, ax = plt.subplots()

# Draw the plot
patches = ax.hist(gpu, density=1)

# Save the plot
plt.savefig(plot)