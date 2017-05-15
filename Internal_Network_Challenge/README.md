# Internal Network Challenge

### Challenge
> We found out that winc0rp has an internal website hosted on this ip address. However, is it really internal?
> I heard the internal website is located at 'internal.proxy.winc0rp.com' 
> Please find the internal website hosted on 128.199.98.78:8080

### Solution
Visiting the page tells us this

	No flag here.
	Flag can be found on http://internal.proxy.winc0rp.com:8080/.

We can conclude that we need to point `128.199.98.78:8080` to `internal.proxy.winc0rp.com:8080` judging from the port number.

Hence we can add this to our /etc/hosts file

	128.199.98.78 internal.proxy.winc0rp.com

and we get the flag!

	Flag is: CrossCTF{B@sic_P3ntesting_Sk33ls_Requir3d}

	