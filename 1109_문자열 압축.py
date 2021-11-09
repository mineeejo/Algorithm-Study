def solution(x):
    resultx = ''
    minLen = len(x)

    for num in range(1,len(x)+1):
        i = 0
        while i < len(x):
            count = 1
            while (i+num) < len(x) and x[i:i+num] == x[i+num:i+2*num]:
                count += 1
                i += num

            if count == 1:
                resultx += x[i:i+num]
                i += num
            else:
                resultx += str(count)+x[i:i+num]
                i += num

        if minLen > len(resultx):
            minLen = len(resultx)
        resultx = ''

    return minLen
