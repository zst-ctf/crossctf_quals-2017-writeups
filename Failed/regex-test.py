import re

# http://stackoverflow.com/questions/1559751/regex-to-make-sure-that-the-string-contains-at-least-one-lower-case-char-upper
'''
REGEX = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).+"

^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{26,}

^(?=(?:.*[A-Z].*){2,})(?=(?:.*[a-z].*){2,})(?=(?:.*\d.*){2,})(?=.*\W).+

^(?=(?:.*[A-Z].*){2,})(?=(?:.*[a-z].*){2,})(?=(?:.*\d.*){2,})(?=.*\W).+
^(?=(?:.*[A-Z].*){3,})(?=(?:.*[a-z].*){3,})(?=(?:.*\d.*){3,})(?=.*\W).+
^(?=(?:.*[A-Z].*){5,})(?=(?:.*[a-z].*){5,})(?=(?:.*\d.*){5,})(?=.*\W).+
'''

'''
(?=.*[a-z])         # - Contain lower case characters
(?=.*[A-Z])           # - Contain upper case characters
(?=.*\d)              # Contain digits
(?=.*\W)              # Contain non-alphanumeric
'''

# ^(?=.*[~!@#\$%\^&*_\-\+=`|\\\(\)\{\}\[\]:;"'<>,\.\?/]).+
# ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#\$%\^&*_\-\+=`|\\\(\)\{\}\[\]:;"'<>,\.\?/]).+$
REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{5,}'
# http://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
def isMatch(string):
    return re.compile(REGEX).match(string)


with open("10m_passwords_307225a24bea70813d6218f4faf64780", "r") as file:
    input = file.read()

count = 0
l = input.split("\n")
l = filter(str.isalnum, l)

for line in l:
    if isMatch(line):
    	count +=1
        print line
    else:
        pass

print "count =", count