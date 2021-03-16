# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:28:39 2021

@author: Andreas Traut

Problem: 
This example is based on the folloxing LeetCode problem: 
https://leetcode.com/problems/k-closest-points-to-origin/
We have a list of points on the plane.  Find the K closest points to 
the origin (0, 0). Here, the distance between two points on a plane is 
the Euclidean distance.

Solution: 
The distance to the origin in the Euclidian distance which is the 
root of the squared x- and y-axis: squareroot( x^2 + y^2 )
As the squareroot function is monotone and continuously increasing for positive 
values, we can eliminate the squareroot it in the solution (remember: the sum of 
squares x^2 and y^2 is always positive). 
Therefore we have to
1. calculate the sum of squares x^2 + y^2 for all points and put them in a list, 
2. then sort this list ascending and 
3. take the first K elements of the list


Perform the tests: 
I will use the Jovian "evaluate_test_cases" function, which is a very nice
feature to test many test cases. 

Please do NOT share this solution!

"""
from jovian.pythondsa import evaluate_test_cases
from jovian.pythondsa import evaluate_test_case

#%% Define testcases
tests = []

# Testcase 0: two points and take only the nearest (K=1)
tests.append({
    'input': {
        'points': [[1,3],[-2,2]], 
        'K': 1
    },
    'output': [[-2,2]]
})

# Testcase 1: three points and take the two nearest points (K=2)
tests.append({
    'input': {
        'points': [[3,3],[5,-1],[-2,4]], 
        'K': 2
    },
    'output': [[3,3],[-2,4]]
})

# Testcase 2: many points and take the two nearest points (K=2)
tests.append({
    'input': {
        'points': [[1,1],[10,2],[9,11],[5,-1],[-2,4],[5,9],[9,13],[13,7]], 
        'K': 2
    },
    'output': [[1,1],[-2,4]]
})

#%% Define the class with its kClosests 
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
  
#%% Perform the tests
k = Solution()

# Evaluete if test case 0 is valid:
if (k.kClosest(tests[0]['input']['points'], tests[0]['input']['K']) == tests[0]['output']): 
    print('True')

# Alternative to evaluate only one test case:
evaluate_test_case(k.kClosest, tests[0])  

# Evaluate all test cases:
evaluate_test_cases(k.kClosest, tests)  #to evaluate all test cases