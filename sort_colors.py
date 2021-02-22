# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:16:59 2021

This example is based on the folloxing LeetCode problem: 
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors in 
the order red, white, and blue. We will use the integers 0, 1, and 2 to 
represent the color red, white, and blue, respectively.

@author: Andreas Traut
"""
# %% Define tests
tests = []
tests.append({
    'input': {
        'nums': [2, 0, 2, 1, 1, 0]
    },
    'output': [0, 0, 1, 1, 2, 2]
})
tests.append({
    'input': {
        'nums': [2, 0, 1]
    },
    'output': [0, 1, 2]
})
# %% Define the class with its kClosests
class Solution(object):
    def sortColors(self, nums):
        # Create a copy of the list, to avoid changing it
        tnums = list(nums)
        
        # Exercise for you: 
        # Find the solution! 
                
        for _ in range(len(tnums)):  #modify nums (instead of return), 
                                     #because of leetcode requirement
            nums[_] = tnums[_]  
# %%
k = Solution()
for test_case in range(2): 
    inp = list(tests[test_case]['input']['nums'])
    k.sortColors(inp)
    if inp == tests[test_case]['output']: 
        print('Testcase #{}: PASSED\nInput:\t\t\t{}\nExpected Output:{}\nOutput:\t\t\t{}\n'.
              format(test_case, tests[test_case]['input']['nums'], tests[test_case]['output'], inp))
