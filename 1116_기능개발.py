#!/usr/bin/env python
# coding: utf-8

# In[22]:


import math

def solution(progresses, speeds):
    days = []
    cnt = 0
    counts = []

    for p, s in zip(progresses,speeds):
        days.append(math.ceil((100-p)/s))

    maxS = days[0]

    for i in range(len(days)):
        if maxS >= days[i]:
            cnt += 1
        else:
            counts.append(cnt)
            cnt = 1
            maxS = days[i]

    counts.append(cnt)

    return counts


# In[27]:


# 다른 사람 풀이
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
        print(count, time)
    answer.append(count)
    return answer

