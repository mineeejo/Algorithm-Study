#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(p):
    
    def check_right(p): # '올바른' 괄호 문자열인지 확인
        count = 0
        i = 0
        while count >= 0 and i < len(p):
            if p[i] == '(':
                count += 1
            elif p[i] == ')':
                count -= 1
            if count < 0:
                return False
            i += 1
        if count == 0:
            return True
        else:
            return False

    def uvsplit(p): # u, v 분리하기
        countO, countC = 0,0
        for i in range(len(p)):
            if p[i] == '(':
                countO += 1
            elif p[i] == ')':
                countC += 1
            if countO == countC:
                u = p[:i+1]
                v = p[i+1:]
                break
        return (u,v)
    
    def ifNotRight(strr): # u가 올바른 괄호 문자열이 아닐 경우 (4번 수행) 
        strr = list(strr)
        for i in range(1,len(strr)):
            if strr[i] == '(':
                strr[i] = ')'
            else:
                strr[i] ='('
        new_strr = ''.join(strr[1:-1])

        return new_strr
    

    def real(w):
        if w =='':
            return ''
        
        u,v = uvsplit(w)
        if check_right(u):
            return u + real(v)
        else:
            return '('+ real(v) + ')' + ifNotRight(u)
    
    return (''.join(real(p)))

