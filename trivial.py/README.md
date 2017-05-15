# trival.py

### Challenge
> It's trivial, my dear Watson. [File here](trivial.pyc)

### Solution
Since we are given a `.pyc` file, we need to decompile it to `.py`.

I found an easy to use decompiler, [Decompyle++](https://ltops9.wordpress.com/2014/04/17/decompyle-a-great-python-dissasemblerdecompiler/), which worked for me.

To install:

	git clone git://github.com/zrax/pycdc
	cd pycdc
	cmake CMakeLists.txt
	make

And to decompile:

	./pycdc trivial.pyc > trival.py

So from the check function of `trival.py`, we see this code

	if final['check_code'] != 'AK4782':
	    return False
	if None['flag_content']['numbers'] * 2 != 18529313:
	    return False
	if None['flag_content']['change'] != 'standardisation'[::2]:
	    return False
	if None['flag_content']['settled'] != 'CrossCTF{%s_%d_%s}':
	    return False
	temp = None['flag_content']
	return temp['settled'] % (temp['change'], temp['numbers'], final['check_code'])

We can find `change` and `numbers` using the python interpreter

	>>> 'standardisation'[::2]
	'sadriain'
	>>> 18529313 / 2
	9264656

We can construct the flag with 

	"CrossCTF{%s_%d_%s}" % (sadriain, 9264656, AK4782)

Hence, the flag is `CrossCTF{sadriain_9264656_AK4782}`
