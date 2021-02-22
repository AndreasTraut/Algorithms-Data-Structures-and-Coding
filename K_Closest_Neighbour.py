# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:28:39 2021

This example is based on the folloxing LeetCode problem: 
https://leetcode.com/problems/k-closest-points-to-origin/
We have a list of points on the plane.  Find the K closest points to 
the origin (0, 0).

(Here, the distance between two points on a plane is the  Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique 
(except for the order that it is in.)

@author: Andreas Traut
"""
from jovian.pythondsa import evaluate_test_cases
from jovian.pythondsa import evaluate_test_case

#%% Define tests
tests = []
tests.append({
    'input': {
        'points': [[1,3],[-2,2]], 
        'K': 1
    },
    'output': [[-2,2]]
})
tests.append({
    'input': {
        'points': [[3,3],[5,-1],[-2,4]], 
        'K': 2
    },
    'output': [[3,3],[-2,4]]
})

#%% Define the class with its kClosests 
class Solution(object):
    def kClosest(self, points, K):
        
        # Exercise for you: 
        # Find the solution!
        
        return 0
    
#%%
k = Solution()
#evaluete if test case 0 is valid:
if (k.kClosest(tests[0]['input']['points'], tests[0]['input']['K']) == tests[0]['output']): 
    print('True')

#alternative to evaluate only one test case:
evaluate_test_case(k.kClosest, tests[0])  

#evaluate all test cases:
evaluate_test_cases(k.kClosest, tests)  #to evaluate all test cases