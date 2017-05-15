# complexpassword

### Challenge
> We found out that evilc0rp has a password policy stating that passwords should:
- Contain upper case characters
- Contain lower case characters
- Contain digits
- Contain nonalphanumeric characters: (~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/)

> However, it'd take too long to try every possible password in the password list we found.
Can you help us develop a regex to find the correct passwords more efficiently?
p.s. We need 6 of them and I think they use really strong passwords...

> [Password list here](10m_passwords_307225a24bea70813d6218f4faf64780)

> Connect to 128.199.98.78:32768

### Solution
Searching for [how to check if a string contains upper case chars](http://stackoverflow.com/questions/1559751/regex-to-make-sure-that-the-string-contains-at-least-one-lower-case-char-upper), tells me we should use regex lookahead.

In this case, I came up with the following regex:
	
	^				# Start of string
	(?=.*[a-z])		# Lower case chars
	(?=.*[A-Z])		# Upper case chars
	(?=.*\d)		# Digits
	(?=.*[~!@#\$%\^&*_\-\+=`|\\\(\)\{\}\[\]:;"'<>,\.\?/])
			 		# These chars, (escaped the metacharacters): (~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/)
	.+ 				# Gobble up the string
	$				# End of string

This returned 1.5k entries. From the description, it says `I think they use really strong passwords` which implies that a longer length is used.
Looking through, we can find that in the 1.5k entries, only 6 entries are 25 chars or more.

Hence, the final regex is 
	
	^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#\$%\^&*_\-\+=`|\\\(\)\{\}\[\]:;"'<>,\.\?/]).{25,}$`

This is the result:

	Regex: ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#\$%\^&*_\-\+=`|\\\(\)\{\}\[\]:;"'<>,\.\?/]).{25,}$

	Filtering passwords!...
	1) Vixens.comreaper999MOR098GO
	2) Tickled.comreaper999MOR098GO
	3) Your_Guardian_Angel_050813
	4) you_have_been_hacked_gWSxH1FZfr
	5) weAaQIno0lhLHWsIfL9TQG30ZrI-~B
	6) &&wdXWabuSc7&b*QDex_6B*5v?e8V
	Congratulations! Here's your flag: CrossCTF{C0mPleX_P@s$w0rd_Is_G0oD!}

The flag is `CrossCTF{C0mPleX_P@s$w0rd_Is_G0oD!}`