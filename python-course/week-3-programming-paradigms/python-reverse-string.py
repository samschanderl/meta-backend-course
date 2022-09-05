# using a slice function
# str[start:stop:step]

string = "reversal"
# slice the string leaving the start and stop empty
new_string = string[::-1]
print(string, new_string)

# using recursion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

string2 = "testing reversal"
new_string2 = string_reverse(string2)

print(string2, new_string2)