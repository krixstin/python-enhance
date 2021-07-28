def palindrome(input):
    if len(input) == 0 or len(input) == 1:
        return True
    
    if input[0] == input[len(input)-1]:
        # shrink the input string
        return palindrome(input[1:len(input)-1])

    return False

print(palindrome("kayak"))
print(palindrome("racecar"))