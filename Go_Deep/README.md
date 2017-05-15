# Go Deep

### Challenge
> We intercepted this mystery message. Could you figure out what it is?
> [File here](godeep_5b4a789794a6d5fba439db1fde186765.txt)

### Solution
From the name, it sounds similar to [PACTF 2017 MegaEncryption](https://github.com/zst123/pactf-2017-writeups/tree/master/Round-1_Bartik/MegaEncryption).
However, hex decoding is needed in addition to base 64 decode.

[Running my script](godeep-solver.py), we get the flag after 24 iterations:

	iter =  24
	CrossCTF{I_5h@11_h1v3_70_90_d33p}