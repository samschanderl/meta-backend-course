# Algorithm for a Palindrome

string = "racecar"

def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for item in str:
        print(startIndex, endIndex)
        if str[startIndex] != str[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1
    return True

print(isPalindrome(string))