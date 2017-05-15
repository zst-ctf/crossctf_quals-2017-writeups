# Knights of the AAAAAAA 

### Challenge
>We have intercepted secret messages but it seems like AAAAAAAAAAA to us. Can you help us?
> [File here](flag_fffd7884e758c612ce7f23175cafc83bfb20ea66.png)

### Solution
This seems to be using symbols to represent the flag. We can try substitution solvers to solve this.

First we need to convert it into alphabets (Repeated letters means the same symbol)

	ABCDDAEF{GHIJ_FCB_LCM}
	
Next, let's use [quipqiup](http://quipqiup.com/) to solve it. Since all the flags are in the format `CrossCTF{}` we can assign the clues as:

	ABCD=CROS EF=TF

There is one legible result which is `CROSSCTF{LAME_FOR_YOU}` but it is not the correct answer.

We need to do more analysis.
Removing the dot in the rightwards-pointing triangle is a transformation from 'T' to 'F' (characters 7 and 8 in `CrossCTF{...}`).
	
	>>> ord('T') - ord('F')
	14

Hence, the difference is 14.
So comparing the 2 diamond shapes enclosed inside the braces {}, the diamond with the dot is Y (forth letter from the back in `CROSSCTF{LAME_FOR_YOU}`).

	>>> chr(ord("Y") - 14)
	'K'

Hence, let's add it to our clue

	ABCD=CROS EF=TF G=K

Finally, solving on [quipqiup](http://quipqiup.com/) gives us the correct flag!

	CROSSCTF{KING_FOR_YOU}