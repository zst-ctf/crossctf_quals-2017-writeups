# Salted Hash Challenge

### Challenge
> I've logged in with my admin credentials:

> Admin username: john
> Admin password: moreThan10CharPassword

> I am supposed to get have admin privileges, but the webpage keeps telling me I am not admin. I must have configured something wrongly, can you help me? 

> Please find the website hosted on 128.199.98.78:32769/index.php It's trivial, my dear Watson. [File here](trivial.pyc)

### Solution
**Credits to @LFlare for hinting to me that this is a [length extension attack](https://en.wikipedia.org/wiki/Length_extension_attack) and finding [this hidden source code](template-admin-login.txt) ([Original source](http://128.199.98.78:32769/template-admin-login.txt))**

With this in mind, we can use [HashPump by bwall](https://github.com/bwall/HashPump).
I also referred to these references: [#1](https://ctfcrew.org/writeup/54), [#2](https://github.com/ctfs/write-ups-2014/tree/master/plaid-ctf-2014/mtpox)

(See [solver-hash.py](solver-hash.py))

However, we do not know the key length, so we have to bruteforce it. After reaching key length of 63, we get this result!

	doing 63
	<h1>Admin</h1>Here's your flag: CrossCTF{thIs_H@5h_iz_5Alty}

Hence, the flag is `CrossCTF{thIs_H@5h_iz_5Alty}`