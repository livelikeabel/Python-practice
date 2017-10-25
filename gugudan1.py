def numPY(s):
    pCount = 0
    yCount = 0

    for i in s:
        if i == 'p' or i == 'P':
            pCount += 1
        if i == 'y' or i == 'Y':
            yCount += 1

    if pCount != yCount:
        return False
    return True

print( numPY("pPoooyY") ) #True
print( numPY("Pyy") ) #False