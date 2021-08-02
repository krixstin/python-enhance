def findBinary(decimal= 1, result=""):
    if decimal == 0 :
        return result
    
    # add the most recent one FRONT
    result = str(decimal % 2) + result
    return findBinary(int(decimal/2), result)

print(findBinary(213))