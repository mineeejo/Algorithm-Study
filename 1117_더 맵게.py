#!/usr/bin/env python
# coding: utf-8

# In[18]:


# 효율성 테스트에서 실패.
scoville = [1, 2, 3, 9, 10, 12]
K = 7

cnt = 0

while min(scoville) < K:
    cnt +=1 
    min1 = min(scoville)
    scoville.remove(min1)
    min2 = min(scoville)
    scoville.remove(min2)

    k = min1 + min2*2
    scoville.append(k)
    
cnt


# In[31]:


# 최종 답안
import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    try:
        while scoville[0] < K:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2*2)
            cnt += 1

        return cnt
    except:
        return -1


# In[32]:


solution([1, 2, 3, 9, 10, 12], 7)

