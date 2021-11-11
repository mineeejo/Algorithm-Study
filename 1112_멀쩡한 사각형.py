#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def solution(w,h):
    answer = w * h - (w + h - math.gcd(w,h))
    
    # gcd로 나눈 사각형을 보면,
    # 한 개의 선을 지날 때마다 한 개의 사각형을 지나감.
    # 가로선과 세로선 각각 w'-1, h'-1개를 지나침
    # 처음 1개의 사각형을 더하면, 총 1 + (w'-1) + (h'-1) = w' + h' -1 개의 사각형 지나침
    # 여기에 다시 gcd를 곱하면, 총 w + h - gcd 개의 사각형을 지나치는 것이므로 정답 도출.
   

    return answer

