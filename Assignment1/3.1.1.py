# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:08:18 2020

@author: bjeli, fernando, lucas
"""
import numpy as np
import matplotlib.pyplot as plt
import time
from DataGeneration import linearly_separable_data

CONVERGENCE = 0.001
ITERATIONS = 50
SAMPLES = 100

def plot_data(X, t):
    plt.scatter(X[0,:], X[1,:], c=t[0,:])
    plt.show()

def calculateBoundary(x, w):
    return (-w[:,0] * x - w[:,2]) / w[:,1] # Wx = 0

mA = [ 1.0, 0.5]
mB = [-1.0, 0.0] 
sigmaA = 0.5
sigmaB = 0.5
x, t = linearly_separable_data(mA, sigmaA, mB, sigmaB)

__x = np.arange(min(x[0,:]), max(x[0,:]), (max(x[0,:]) - min(x[0,:])) / SAMPLES)
eta = 0.001
w = np.random.rand(t.shape[0], x.shape[0])

for i in range(ITERATIONS):
    delta_w = -eta * np.dot(np.dot(w, x) - t, np.transpose(x))
    w += delta_w

    plt.clf()
    axes = plt.gca()
    axes.set_xlim(min(x[0,:]) - 0.5, max(x[0,:]) + 0.5)
    axes.set_ylim(min(x[1,:]) - 0.5, max(x[1,:]) + 0.5)
    plt.plot(__x, calculateBoundary(__x, w), label="Boundary", color='red')
    plt.title("Simple Perceptron: Iteration %i" %(i+1))
    plt.xlabel("X-Coord")
    plt.ylabel("Y-Coord")
    plt.legend()
    plt.scatter(x[0,:], x[1,:], c=t[0,:])
    if (i == 0 or i == ITERATIONS - 1):
        plt.show(block=True)
    else:
        plt.show(block=False)
        plt.pause(0.05)