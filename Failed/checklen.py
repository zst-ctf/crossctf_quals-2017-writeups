import re

# http://stackoverflow.com/questions/1559751/regex-to-make-sure-that-the-string-contains-at-least-one-lower-case-char-upper
REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).+'

# http://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
def isMatch(string):
    return re.compile(REGEX).match(string)


with open("10m_passwords_307225a24bea70813d6218f4faf64780", "r") as file:
    input = file.read()

dict = {
	'0' : 0
}
for line in input.split("\n"):
    if isMatch(line):
    	try:
    		dict[str(len(line))] += 1
        except KeyError:
        	dict[str(len(line))] = 1
        #print line
    else:
        pass

print dict