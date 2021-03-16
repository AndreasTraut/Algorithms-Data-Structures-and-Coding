# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:16:59 2021

@author: Andreas Traut

Problem: 
This example is based on the folloxing LeetCode problem: 
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors in 
the order red, white, and blue. We will use the integers 0, 1, and 2 to 
represent the color red, white, and blue, respectively.

Solution: 
Iterating over the array and swapping.

Please do NOT share this solution!!

"""
# %% Define tests
tests = []
# Testcase 0: some colours occur several times
tests.append({
    'input': {
        'nums': [2, 0, 2, 1, 1, 0]
    },
    'output': [0, 0, 1, 1, 2, 2]
})

# Testcase 1: only three colours
tests.append({
    'input': {
        'nums': [2, 0, 1]
    },
    'output': [0, 1, 2]
})

# Testcase 2: Only colour 2 and 1. No colour 0
tests.append({
    'input': {
        'nums': [2, 2, 2, 1, 2, 2, 2, 1, 1]
    },
    'output': [1, 1, 1, 2, 2, 2, 2, 2, 2]
})

# %% Define the class with its kClosests
class Solution(object):
    def sortColors(self, nums):
        # Create a copy of the list, to avoid changing it
        tnums = list(nums)
        
        # Repeat the process n-1 times
        for _ in range(len(tnums) - 1):     
            # Iterate over the array (except last element)
            for i in range(len(tnums) - 1):          
                # Compare the number with  
                if tnums[i] > tnums[i+1]:
                    # Swap the two elements
                    tnums[i], tnums[i+1] = tnums[i+1], tnums[i]
        
        for _ in range(len(tnums)):  #modify nums (instead of return), 
                                     #because of leetcode requirement
            nums[_] = tnums[_]  
#%% Perform the tests
k = Solution()
for test_case in range(len(tests)): 
    inp = list(tests[test_case]['input']['nums'])
    k.sortColors(inp)
    if inp == tests[test_case]['output']: 
        print('Testcase #{}: PASSED\nInput:\t\t\t{}\nExpected Output:{}\nOutput:\t\t\t{}\n'.
              format(test_case, tests[test_case]['input']['nums'], tests[test_case]['output'], inp))
