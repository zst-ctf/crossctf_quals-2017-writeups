# BabyPS3

### Challenge
> I recently got a copy of Halo 3 but I can't play it on my PS3. Can you help me?
> Connect to 188.166.248.56:3333

[File here](./ps3_d1c35b5b33a85eac170fb6d8f8a2c83e84f9b700/)

### Solution
After searching long and hard, I found out this writeup which explains that the encryption method is [Digital Signature Algorithm (DSA)](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm). It is also "used by Sony to sign software for the PlayStation 3 game console" which explains the name.

From Wikipedia, "Using the same value twice (even while keeping k secret) ... is enough to break DSA". This brings us to this tool, [DSAregenK by tintinweb](https://github.com/tintinweb/DSAregenK).

Looking at DSAregenK `example.py`, we need `r`, `s` and `h` from at least 2 sources. I modified `ps3.py` to print those values:

	Loading Solo Fortress 2
	r = 65409437784982297110912581342752010737235883633264011939488505540228075281368
	s = 35423112485595204833342827083528820396508701138465506923287226062770205121840
	H = 23774880964385620814468110570038093688231692900518718595797672264122586266881

	Loading Miniman XV
	r = 65409437784982297110912581342752010737235883633264011939488505540228075281368
	s = 20262912165800849185854645367293864271318988525533982539211381770687917054877
	H = 47249939200444390154785799101848744001405884122924422864032756950934263851831

Now we have the 2 sources of the values, we can we can modify `example.py` to fit our needs. (See [solver-find_private_key.py](solver-find_private_key.py))
This is the result:

	DEBUG:DSAregenK:privkey reconstructed: 
	k=25768127004975721051099847404129291547143434939937043331286111399159730732336; 
	x=66982082206795733973204253209195163373920331769528646357832825612336892590101;

With this, we can start to find the signature. Thankfully, the `sign()` function is included in `ps3.py`. (See [solver-remake_signature.py](solver-remake_signature.py))

	$ python solver-remake_signature.py halo_3
	Signature of Halo 3 :
	H = 7603882095440872595656610795762553549021121988548807204733771853647578107823
	r = 65409437784982297110912581342752010737235883633264011939488505540228075281368
	s = 48461267897280688759948477905395814706543964150475414979045018649487317668401
	H = 7603882095440872595656610795762553549021121988548807204733771853647578107823
	signature valid

Finally, the signature verification is working! But this value of `s` is still not accepted.
Let's look at `ps3.py` again.

	game = m[796:]

	## truncated ##

	if v:
		print 'signature valid'
		if game == 'A' * 2017 + '\n':
			print 'submit the legitimate signature for the bootleg to get the flag!'
	else:
		print ERROR

This tells us we need to have 2017 characters after the 796th position to be 'A'. I'll fix this bodge by making a new file.
		
	with open("fixed-" + filename, "w") as myfile:
	    myfile.write(m[:796] + 'A' * 2017 + '\n')

Lastly, run [solver-remake_signature.py](solver-remake_signature.py) again
	
	Signature of Halo 3 :
	H = 101208583586539363640702709548762571470761361664933459443467780903823803922686
	r = 65409437784982297110912581342752010737235883633264011939488505540228075281368
	s = 71460979304995498564989090988448238723692184125856399038370248726828684133531
	H = 101208583586539363640702709548762571470761361664933459443467780903823803922686
	signature valid
	submit the legitimate signature for the bootleg to get the flag!

And upon submitting, we get the flag!
	
	$ nc 188.166.248.56 3333
	Please enter the signature: 71460979304995498564989090988448238723692184125856399038370248726828684133531
	CrossCTF{G30RG3_H0T7_W@S_G00D}