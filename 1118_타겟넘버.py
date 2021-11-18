#!/usr/bin/env python
# coding: utf-8

# In[41]:


import collections

def solution(nums, target):
    answer = 0
    queue = collections.deque([(0,0)])
    
    while queue:
        currSum, idx = queue.popleft()
        
        if idx == len(nums):
            if currSum == target:
                answer += 1
        else:
            queue.append((currSum + nums[idx], idx+1))
            queue.append((currSum - nums[idx], idx+1))
    
    return answer

