#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:42:57 2017

@author: dawg
"""

from numpy import *


def compute_error_for_line_given_points(b,m,points):
    totalError = 0
    for i in range(0 , len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError += (y - (m*x + b))**2
    return totalError/float(len(points))

def gradient_descent_runner(points, start_b,start_m,lr , num_iter):
    b = start_b
    m = start_m
    
    
    for i in range(num_iter):
        
        #upadate the m and b by performing the gradient step
        b,m = step_gradient(b,m,array(points),lr)
    return [b,m]
# the main part of the code

def step_gradient(b_curr, m_curr, points, lr):
    #initialize the error like a comapss to point the direction
    b_gradient = 0
    m_gradient = 0
    n  = float(len(points))
    
    for i in range(0 ,len(points)):
        x = points[i,0]
        y = points[i,1]
        #direction wrt b and m
        #computing the partial derivatice of our error function
        b_gradient += -(2/n)*(y- ((m_curr*x) + b_curr))
        m_gradient += (2/n)*(x)*(y-((m_curr*x)*b_curr))
        
    new_b = b_curr - lr*b_gradient
    new_m = m_curr- lr*m_gradient
    return [new_b,new_m]

    
def run():
    
    points = genfromtxt('data.csv' ,delimiter = ',')
    
    learning_rate = 0.0001
    # y= mx+b (slope formula)
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    
    # step3 train our model
    print 'starting gradient descent at b = {0} , m= {1}, error = {2}'.format(initial_b,initial_m,compute_error_for_line_given_points(initial_b,initial_m,points))
        
    
    
if __name__ =='__main__':
    run()
    
    

    