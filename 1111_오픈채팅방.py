#!/usr/bin/env python
# coding: utf-8

# In[34]:


def solution(record):
    logs = {}
    answer = []
    
    for rec in reversed(record):
        order = rec.split()[0]
        if order == 'Leave':
            continue
        usrID = rec.split()[1]
        name = rec.split()[2]
        
        if usrID not in logs:
            logs[usrID] = name

    for rec in record:
        order = rec.split()[0]
        usrID = rec.split()[1]

        if order == 'Enter':
            answer.append(logs[usrID]+'님이 들어왔습니다.')
        elif order == 'Leave':
            answer.append(logs[usrID]+'님이 나갔습니다.')
    
    return answer

