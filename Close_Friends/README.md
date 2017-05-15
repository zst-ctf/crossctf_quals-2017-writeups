# Close Friends

### Challenge
> Alice and Bob are very close friends.
They share their secrets with each other and they do not want others to intercept it.
So they decided to implement their own RSA to encrypt their messages.

> [File here](./closefriends_fea963416e85bb6e872accbe1aae124d/)

### Solution
This challenge took me awhile to think of a solution. My idea is that since the provided `generate.py` takes `p` and `q` as 2 consecutive safe primes, we can calculate the square root of `n` to find the mid-point, then find the previous and next safe primes.

Let't first do the square root of `n`. [Since it is a large number, we need the Python decimal module](http://stackoverflow.com/questions/10725522/arbitrary-precision-of-square-roots).

	>>> from decimal import *
	>>> n = <use the given n, removed for brevity>
	>>> getcontext().prec = 1024
	>>> Decimal(n).sqrt()
	>>> 138390145474559979704018959433486332171236693523257121207855763257601215111860353723054861659320614622191253495207107734543180548210017641587057951631900485980496061774438791272456448896948365869073759311971254087871345404407643977893681606530042245542049352120256210758480682257393112074792796566675809641926.999<truncated for brevity>

Now we have the square root of n, I'll round it down to a whole number (remove the stuff after the decimal point) and let's calculate `p` and `q` from this. I'll calculate the next safe prime from the square root of n, and then take p = n/q (so we don't have to take too much time to find the previous prime)
(See my [solver-factorize.py](solver-factorize.py) script)

Finally, we have all we need to decrypt everything. (See my [solver-decrypt.py](solver-decrypt.py) script)

	CrossCTF{its_g00d_t0_hav3_c1o5e_friend5_i5nt_it}