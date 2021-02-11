#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

#import text file
data = np.loadtxt('Random numbers.dat')


# create histogram of our data
n, bins, patches = plt.hist(data, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('x', fontsize = 16, color = "blue")
plt.ylabel('Probability', fontsize = 16, color = "red")
plt.title('Uniform random number')
plt.legend(['cool green bars'], loc = 'upper left')
plt.grid(True)

plt.show()
