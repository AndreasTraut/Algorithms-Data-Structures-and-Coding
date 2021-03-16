# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:25:21 2021

@author: Andreas Traut

Problem: 
Assume, ath we have a bag of capacity c. And assume, that we have n items, which 
each has a weight and a profit. We have the choice to select items, to be filled 
into this bag and the aim is to maximize the profit. At same time we are not 
allowed to breach the capacity of the bag, meaning, that the sum of 
the weights of the chosen items should be smaller or equal to the capacity. 

Solution: 
This problem can be solved with dynamic programming. 

Further references for learning more about this topic: 
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
https://medium.com/@fabianterh/how-to-solve-the-knapsack-problem-with-dynamic-programming-eb88c706d3cf

"""

#%% Define the test cases
test = {
    'input': {
        'capacity': 2000,
        'weights': [630, 780, 1400, 480], 
        'profits': [8, 6, 12, 7]
    },
    'output': 21
}

tests = []
tests.append(test)

tests.append({
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
})

tests.append({
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
})

tests.append({
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
})

tests.append({
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
})

tests.append({
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
})

tests.append({
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
})


#%% Define the algorithm
def knapsack_dp(capacity, weights, profits):
    n = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for idx in range(n):
        for c in range(capacity+1):
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            else:                
                results[idx+1][c] = max(results[idx][c], profits[idx] + results[idx][c-weights[idx]])
            
    return results[-1][-1]

#%% Perform the tests

# On the first test case only
from jovian.pythondsa import evaluate_test_case
evaluate_test_case(knapsack_dp, test)

#%%
# On all test cases
from jovian.pythondsa import evaluate_test_cases
evaluate_test_cases(knapsack_dp, tests)